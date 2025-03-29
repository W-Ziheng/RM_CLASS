set(_AMENT_PACKAGE_NAME "vision_node")
set(vision_node_VERSION "0.1.0")
set(vision_node_MAINTAINER "Your Name <your@email.com>")
set(vision_node_BUILD_DEPENDS "rclcpp" "sensor_msgs" "image_transport" "cv_bridge" "OpenCV")
set(vision_node_BUILDTOOL_DEPENDS "ament_cmake")
set(vision_node_BUILD_EXPORT_DEPENDS "rclcpp" "sensor_msgs" "image_transport" "cv_bridge" "OpenCV")
set(vision_node_BUILDTOOL_EXPORT_DEPENDS )
set(vision_node_EXEC_DEPENDS "rclcpp" "sensor_msgs" "image_transport" "cv_bridge" "OpenCV")
set(vision_node_TEST_DEPENDS "ament_lint_auto" "ament_lint_common")
set(vision_node_GROUP_DEPENDS )
set(vision_node_MEMBER_OF_GROUPS )
set(vision_node_DEPRECATED "")
set(vision_node_EXPORT_TAGS)
list(APPEND vision_node_EXPORT_TAGS "<build_type>ament_cmake</build_type>")
list(APPEND vision_node_EXPORT_TAGS "<ament_cmake><dependencies>
        rclcpp
        sensor_msgs
        image_transport
        cv_bridge
      </dependencies></ament_cmake>")
