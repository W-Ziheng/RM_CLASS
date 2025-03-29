cmake_minimum_required(VERSION 3.22)

project(Detect)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(Detect red_circle_detect.cpp)
add_executable(Detect_2 green_tricle_detect.cpp)
# 链接OpenCV库
target_link_libraries(Detect PRIVATE ${OpenCV_LIBS})
target_link_libraries(Detect_2 PRIVATE ${OpenCV_LIBS})