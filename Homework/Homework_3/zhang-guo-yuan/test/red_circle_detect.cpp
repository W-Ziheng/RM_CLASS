#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

int main() {
    // 初始化摄像头
    cv::VideoCapture cap(0); // 数字根据摄像头编号调整
    if (!cap.isOpened()) {
        std::cerr << "无法打开摄像头！" << std::endl;
        return -1;
    }

    while (true) {
        // 读取视频帧
        cv::Mat frame;
        cap >> frame;
        if (frame.empty()) {
            std::cerr << "无法获取视频帧！" << std::endl;
            break;
        }

        // 将图像转换为HSV颜色空间
        cv::Mat hsv;
        cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);

        // 定义红色的HSV范围
        cv::Scalar lower_red1(0, 100, 100);
        cv::Scalar upper_red1(10, 255, 255);
        cv::Scalar lower_red2(160, 100, 100);
        cv::Scalar upper_red2(180, 255, 255);

        // 创建红色掩膜
        cv::Mat mask1, mask2, mask;
        cv::inRange(hsv, lower_red1, upper_red1, mask1);
        cv::inRange(hsv, lower_red2, upper_red2, mask2);
        cv::bitwise_or(mask1, mask2, mask);

        // 图像预处理
        cv::erode(mask, mask, cv::Mat(), cv::Point(-1, -1), 2);
        cv::dilate(mask, mask, cv::Mat(), cv::Point(-1, -1), 2);
        cv::GaussianBlur(mask, mask, cv::Size(9, 9), 2);

        // 霍夫圆检测
        std::vector<cv::Vec3f> circles;
        cv::HoughCircles(mask, circles, cv::HOUGH_GRADIENT, 1.2, 100,
                         50, 30, 20, 200);

        // 如果检测到圆形
        if (!circles.empty()) {
            for (size_t i = 0; i < circles.size(); ++i) {
                cv::Point2f center(circles[i][0], circles[i][1]);
                float radius = circles[i][2];

                // 绘制圆形和中心点
                cv::circle(frame, center, radius, cv::Scalar(0, 255, 0), 4);
                cv::circle(frame, center, 2, cv::Scalar(0, 0, 255), 3);

                // 显示圆心坐标
                std::string text = "(" + std::to_string(int(center.x)) + ", " +
                                   std::to_string(int(center.y)) + ")";
                cv::putText(frame, text, cv::Point(center.x - 50, center.y - 20),
                            cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 255, 255), 2);
            }
        }

        // 显示结果
        cv::imshow("Frame", frame);
        cv::imshow("Mask", mask);

        // 按q退出
        if (cv::waitKey(1) & 0xFF == 'q') {
            break;
        }
    }

    // 释放资源
    cap.release();
    cv::destroyAllWindows();

    return 0;
}
