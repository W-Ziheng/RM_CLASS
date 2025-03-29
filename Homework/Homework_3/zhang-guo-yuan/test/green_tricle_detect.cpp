#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <vector>

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

        // 定义绿色的HSV范围
        cv::Scalar lower_green(50, 100, 100);
        cv::Scalar upper_green(70, 255, 255);

        // 创建绿色掩膜
        cv::Mat mask;
        cv::inRange(hsv, lower_green, upper_green, mask);

        // 图像预处理
        cv::erode(mask, mask, cv::Mat(), cv::Point(-1, -1), 1);
        cv::dilate(mask, mask, cv::Mat(), cv::Point(-1, -1), 1);
        cv::GaussianBlur(mask, mask, cv::Size(5, 5), 2);

        // 查找轮廓
        std::vector<std::vector<cv::Point>> contours;
        std::vector<cv::Vec4i> hierarchy;
        cv::findContours(mask, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

        // 遍历轮廓并检测三角形
        for (size_t i = 0; i < contours.size(); ++i) {
            // 使用多边形近似轮廓
            std::vector<cv::Point> approx;
            cv::approxPolyDP(cv::Mat(contours[i]), approx, cv::arcLength(cv::Mat(contours[i]), true) * 0.02, true);

            // 如果轮廓近似为三角形（3个顶点）
            if (approx.size() == 3) {
                // 计算轮廓面积
                double area = cv::contourArea(contours[i]);
                if (area > 100 && area < 10000) { // 假设合理面积范围为100到10000
                    // 绘制三角形
                    cv::drawContours(frame, std::vector<std::vector<cv::Point>>{approx}, -1, cv::Scalar(0, 255, 0), 4);

                    // 计算三角形的中心点
                    cv::Moments M = cv::moments(contours[i]);
                    if (M.m00 != 0) {
                        int cx = M.m10 / M.m00;
                        int cy = M.m01 / M.m00;

                        // 绘制中心点
                        cv::circle(frame, cv::Point(cx, cy), 2, cv::Scalar(255, 0, 0), 3);

                        // 显示中心点坐标
                        std::string text = "(" + std::to_string(cx) + ", " + std::to_string(cy) + ")";
                        cv::putText(frame, text, cv::Point(cx - 50, cy - 20), cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 0, 0), 2);
                    }
                }
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
