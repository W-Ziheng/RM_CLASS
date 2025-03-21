#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>
int main(){
    cv::Mat img_bgr = cv::imread("../image.png");
    if(img_bgr.empty()){
        std::cerr<<"Error : Unable to load image!"<<std::endl;
        return -1;

    }
    cv::Mat img_hsv;
    cv::cvtColor(img_bgr , img_hsv , cv::COLOR_BGR2HSV);
    
    std::vector<cv::Mat> channels(3);
    cv::split(img_hsv , channels);

    cv::Mat mask_red1 , mask_red2 , mask_red;

    cv::Scalar lower_red1(0,50,50);
    cv::Scalar upper_red1(10, 255, 255);
    cv::Scalar lower_red2(170, 50, 50);
    cv::Scalar upper_red2(180, 255, 255);

    cv::inRange(img_hsv, lower_red1, upper_red1, mask_red1);
    cv::inRange(img_hsv, lower_red2, upper_red2, mask_red2);
 
    cv::bitwise_or(mask_red1 , mask_red2 , mask_red);

    cv::imshow("Original Image" , img_bgr);
    cv::imshow("Red Mask" , mask_red);

    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}