#include<iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
int main(){
    cv::Mat image = cv::imread("../armor.png");

    if(image.empty()){
        std::cout<<"can't read the picture,detect the way of it";
        return -1;
    }
    cv::Mat gray_image;
    cv::cvtColor(image , gray_image,cv::COLOR_BGR2GRAY);
    cv::imshow("Original Image" , image);
    cv::imshow("Gray Image" , gray_image);
    cv::waitKey(0);
    cv::destroyAllWindows();
    cv::imwrite("armor_gray.png" , gray_image);
    return 0;
}
