#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>
int main() {
    cv::Mat img_bgr = cv::imread("../image.png");
    if (img_bgr.empty()) {
        std::cerr << "Error: Unable to load image!" << std::endl;
        return -1;
    }
    cv::Mat img_hsv, img_lab, img_ycrcb;
    cv::cvtColor(img_bgr, img_hsv, cv::COLOR_BGR2HSV);
    cv::cvtColor(img_bgr, img_lab, cv::COLOR_BGR2Lab);
    cv::cvtColor(img_bgr, img_ycrcb, cv::COLOR_BGR2YCrCb);

    cv::Mat img_hsv_bgr, img_lab_bgr, img_ycrcb_bgr;
    cv::cvtColor(img_hsv, img_hsv_bgr, cv::COLOR_HSV2BGR);
    cv::cvtColor(img_lab, img_lab_bgr, cv::COLOR_Lab2BGR);
    cv::cvtColor(img_ycrcb, img_ycrcb_bgr, cv::COLOR_YCrCb2BGR);

    cv::imshow("RGB", img_bgr);  
    cv::imshow("HSV", img_hsv_bgr);
    cv::imshow("LAB", img_lab_bgr);
    cv::imshow("YCrCb", img_ycrcb_bgr);

    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}