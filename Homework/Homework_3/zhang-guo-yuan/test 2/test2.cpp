#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>
int main(){
    cv::Mat img_bgr = cv::imread("../image.png");
    
    if(img_bgr.empty()){
        std::cerr << "Error : Unable to load image!"<<std::endl;
        return -1;
    }
    cv::Mat img_rgb;
    cv::cvtColor(img_bgr , img_rgb,cv::COLOR_BGRA2BGR);
    
    std::vector<cv::Mat>channels(3);
    cv::split(img_rgb , channels);

    cv::Mat img_red;
    cv::merge(channels , img_red);

    cv::imshow("Originak Image" , img_bgr);
    cv::imshow("Red Image" , img_red);

    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}