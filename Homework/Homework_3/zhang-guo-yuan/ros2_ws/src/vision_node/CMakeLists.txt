cmake_minimum_required(VERSION 3.22)
project(vision_node)

# 查找依赖
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(image_transport REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED COMPONENTS core imgproc highgui)

# 添加可执行文件
add_executable(green_triangle_detector 
  green_triangle_detect.cpp
)

# 链接依赖
target_link_libraries(green_triangle_detector
  ${OpenCV_LIBS}
  ${rclcpp_LIBRARIES}
  ${image_transport_LIBRARIES}
  ${cv_bridge_LIBRARIES}
)

# 配置ament依赖
ament_target_dependencies(green_triangle_detector
  rclcpp
  sensor_msgs
  image_transport
  cv_bridge
)

# 安装配置
install(TARGETS green_triangle_detector
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
