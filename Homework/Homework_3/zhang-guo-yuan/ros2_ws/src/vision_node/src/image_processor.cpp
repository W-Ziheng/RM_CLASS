#include "rclcpp/rclcpp.hpp"
#include <image_transport/image_transport.hpp>
#include "cv_bridge/cv_bridge.h"
#include "opencv2/opencv.hpp"
#include "sensor_msgs/msg/camera_info.hpp"

using namespace std::chrono_literals;

class ImageProcessor : public rclcpp::Node
{
public:
  ImageProcessor() : Node("image_processor_node")
  {
    // 参数配置
    declare_parameter("debug_mode", false);
    debug_mode_ = get_parameter("debug_mode").as_bool();

    // 初始化图像传输接口
    it_ = std::make_shared<image_transport::ImageTransport>(shared_from_this());

    // 创建订阅者（带相机信息）
    cam_sub_ = it_->subscribeCamera(
        "input_image", 10,
        std::bind(&ImageProcessor::imageCallback, this, 
                  std::placeholders::_1, 
                  std::placeholders::_2));

    // 创建发布者
    img_pub_ = it_->advertise("output_image", 10);

    // 初始化OpenCV窗口（调试模式）
    if(debug_mode_){
      cv::namedWindow("Debug View", cv::WINDOW_NORMAL);
      cv::resizeWindow("Debug View", 640, 480);
    }

    RCLCPP_INFO(get_logger(), "Node initialized");
  }

  ~ImageProcessor(){
    if(debug_mode_) cv::destroyAllWindows();
  }

private:
  void imageCallback(
      const sensor_msgs::msg::Image::ConstSharedPtr &img_msg,
      const sensor_msgs::msg::CameraInfo::ConstSharedPtr &info_msg)
  {
    try {
      // Step 1: 转换为OpenCV格式
      cv_bridge::CvImagePtr cv_ptr = cv_bridge::toCvCopy(
          img_msg, 
          sensor_msgs::image_encodings::BGR8);

      // Step 2: 图像处理流程
      processImage(cv_ptr->image);

      // Step 3: 在右上角绘制矩形
      drawInfoBox(cv_ptr->image);

      // Step 4: 显示调试窗口
      if(debug_mode_){
        cv::imshow("Debug View", cv_ptr->image);
        cv::waitKey(1);
      }

      // Step 5: 转换回ROS消息并发布
      auto out_msg = cv_ptr->toImageMsg();
      img_pub_.publish(out_msg);

    } catch (const cv_bridge::Exception& e) {
      RCLCPP_ERROR(get_logger(), "cv_bridge exception: %s", e.what());
    }
  }

  void processImage(cv::Mat &frame)
  {
    // 绿色三角形识别算法
    cv::Mat hsv, mask;
    
    // 转换到HSV色彩空间
    cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);
    
    // 定义绿色范围（根据实际环境调整）
    cv::Scalar lower_green(35, 50, 50);
    cv::Scalar upper_green(85, 255, 255);
    cv::inRange(hsv, lower_green, upper_green, mask);

    // 形态学操作（去噪）
    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_ELLIPSE, cv::Size(5,5));
    cv::morphologyEx(mask, mask, cv::MORPH_CLOSE, kernel, cv::Point(-1,-1), 2);
    cv::morphologyEx(mask, mask, cv::MORPH_OPEN, kernel, cv::Point(-1,-1), 1);

    // 查找轮廓
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    // 识别三角形
    for(auto &contour : contours){
      double area = cv::contourArea(contour);
      if(area < 500) continue; // 过滤小面积噪声

      std::vector<cv::Point> approx;
      cv::approxPolyDP(contour, approx, 0.04*cv::arcLength(contour, true), true);

      if(approx.size() == 3){
        // 绘制轮廓和中心点
        cv::drawContours(frame, std::vector<std::vector<cv::Point>>{approx}, 
                        -1, cv::Scalar(0,255,0), 3);
        
        // 计算中心坐标
        cv::Moments m = cv::moments(approx);
        cv::Point center(m.m10/m.m00, m.m01/m.m00);
        cv::circle(frame, center, 5, cv::Scalar(255,0,0), -1);
      }
    }
  }

  void drawInfoBox(cv::Mat &frame)
  {
    const int box_w = 200;
    const int box_h = 40;
    const cv::Point start_pt(frame.cols - box_w - 10, 10);
    const cv::Point end_pt(frame.cols - 10, box_h + 10);
    
    // 绘制半透明背景
    cv::Mat overlay;
    frame.copyTo(overlay);
    cv::rectangle(overlay, start_pt, end_pt, cv::Scalar(50,50,50), -1);
    cv::addWeighted(overlay, 0.6, frame, 0.4, 0, frame);

    // 添加文字
    std::string status = "Triangles: " + std::to_string(triangle_count_);
    cv::putText(frame, status, 
               cv::Point(frame.cols - box_w + 5, 35), 
               cv::FONT_HERSHEY_SIMPLEX, 0.8, 
               cv::Scalar(255,255,255), 2);
  }

  // 成员变量
  std::shared_ptr<image_transport::ImageTransport> it_;
  image_transport::CameraSubscriber cam_sub_;
  image_transport::Publisher img_pub_;
  bool debug_mode_;
  int triangle_count_ = 0;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<ImageProcessor>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
