cmake_minimum_required(VERSION 3.11)
project(Publisher2Listener)

# ROS2相关的CMake依赖
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(publisher src/publisher.cpp)
ament_target_dependencies(publisher rclcpp std_msgs)

add_executable(listener src/listener.cpp)
ament_target_dependencies(listener rclcpp std_msgs)

install(TARGETS
  publisher
  listener
  DESTINATION lib/${PROJECT_NAME})

ament_package()