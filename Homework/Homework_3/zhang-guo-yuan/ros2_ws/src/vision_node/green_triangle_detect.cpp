#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "sensor_msgs/msg/camera_info.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>
#include <image_transport/image_transport.hpp>

class TriangleDetector : public rclcpp::Node {
public:
  TriangleDetector() : Node("green_triangle_detector") {
    // 参数声明
    declare_parameter("hue_low", 50);
    declare_parameter("hue_high", 70);
    declare_parameter("min_area", 100.0);
    declare_parameter("max_area", 10000.0);

    // 初始化摄像头
    cap_.open(0);
    if (!cap_.isOpened()) {
      RCLCPP_ERROR(get_logger(), "无法打开摄像头！");
      return;
    }

    // 初始化相机信息
    init_camera_info();

    // 创建图像发布者
    publisher_ = image_transport::create_camera_publisher(
      this, 
      "processed_image",
      rclcpp::QoS(10).best_effort().get_rmw_qos_profile()
    );

    // 创建处理定时器
    timer_ = create_wall_timer(
      std::chrono::milliseconds(33),
      std::bind(&TriangleDetector::process_frame, this));
  }

private:
  void init_camera_info() {
    camera_info_ = std::make_shared<sensor_msgs::msg::CameraInfo>();
    camera_info_->header.frame_id = "camera_optical_frame";
    camera_info_->width = 640;  // 根据实际分辨率调整
    camera_info_->height = 480;
    // 简化的相机内参（需要根据实际标定数据修改）
    camera_info_->k = {700.0, 0.0, 320.0,
                      0.0, 700.0, 240.0,
                      0.0, 0.0, 1.0};
    camera_info_->p = {700.0, 0.0, 320.0, 0.0,
                      0.0, 700.0, 240.0, 0.0,
                      0.0, 0.0, 1.0, 0.0};
  }

  void process_frame() {
    cv::Mat frame;
    cap_ >> frame;
    if (frame.empty()) return;

    // 核心识别逻辑
    process_image(frame);

    // 转换并发布图像
    publish_result(frame);
  }

  void process_image(cv::Mat& frame) {
    // 获取动态参数
    const int hue_low = get_parameter("hue_low").as_int();
    const int hue_high = get_parameter("hue_high").as_int();
    const double min_area = get_parameter("min_area").as_double();
    const double max_area = get_parameter("max_area").as_double();

    // HSV颜色空间转换
    cv::Mat hsv, mask;
    cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);
    
    // 创建颜色掩膜
    cv::inRange(hsv, 
               cv::Scalar(hue_low, 100, 100),
               cv::Scalar(hue_high, 255, 255),
               mask);

    // 形态学操作
    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_ELLIPSE, {5,5});
    cv::morphologyEx(mask, mask, cv::MORPH_CLOSE, kernel);
    cv::morphologyEx(mask, mask, cv::MORPH_OPEN, kernel);

    // 查找轮廓
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    // 轮廓处理
    for (auto& contour : contours) {
      // 多边形近似
      std::vector<cv::Point> approx;
      cv::approxPolyDP(contour, approx, 
                      cv::arcLength(contour, true)*0.02, 
                      true);

      // 三角形检测
      if (approx.size() == 3) {
        const double area = cv::contourArea(contour);
        if (area > min_area && area < max_area) {
          // 绘制轮廓
          cv::polylines(frame, {approx}, true, {0,255,0}, 3);
          
          // 计算中心点
          cv::Moments m = cv::moments(contour);
          if (m.m00 != 0) {
            const cv::Point center(m.m10/m.m00, m.m01/m.m00);
            
            // 绘制中心点
            cv::circle(frame, center, 5, {255,0,0}, -1);
            
            // 显示坐标
            std::string coord_text = 
              "(" + std::to_string(center.x) + 
              ", " + std::to_string(center.y) + ")";
            cv::putText(frame, coord_text,
                       {center.x - 50, center.y - 20},
                       cv::FONT_HERSHEY_SIMPLEX, 0.5,
                       {0,0,0}, 2);
          }
        }
      }
    }
  }

  void publish_result(const cv::Mat& frame) {
    // 转换OpenCV图像到ROS消息
    auto img_msg = cv_bridge::CvImage(
      std_msgs::msg::Header(),
      "bgr8",
      frame
    ).toImageMsg();

    // 同步时间戳
    const auto stamp = now();
    img_msg->header.stamp = stamp;
    camera_info_->header.stamp = stamp;
    img_msg->header.frame_id = camera_info_->header.frame_id;

    // 发布消息
    publisher_.publish(img_msg, camera_info_);
  }

  // 成员变量
  cv::VideoCapture cap_;
  image_transport::CameraPublisher publisher_;
  sensor_msgs::msg::CameraInfo::SharedPtr camera_info_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<TriangleDetector>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
