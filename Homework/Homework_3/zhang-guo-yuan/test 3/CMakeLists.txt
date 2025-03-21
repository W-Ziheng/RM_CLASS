cmake_minimum_required(VERSION 3.22)

project(Test)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(Test test3.cpp)
# 链接OpenCV库
target_link_libraries(Test PRIVATE ${OpenCV_LIBS})