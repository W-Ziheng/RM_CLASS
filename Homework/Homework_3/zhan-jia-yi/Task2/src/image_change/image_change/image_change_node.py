#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageSubscriberAndPublisher(Node):
    def __init__(self):
        super().__init__('image_subscriber_and_publisher')

        # 创建 CvBridge 实例，用于 ROS 图像消息和 OpenCV 图像之间的转换
        self.bridge = CvBridge()

        # 订阅摄像头发布的图像话题
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',  # 请根据实际情况修改为正确的摄像头图像话题
            self.image_callback,
            10)
        self.subscription  # 防止未使用变量警告

        # 创建图像发布者，用于发布处理后的图像消息
        self.publisher = self.create_publisher(Image, '/processed_image', 10)

    def image_callback(self, msg):
        try:
            # 将 ROS 图像消息转换为 OpenCV 图像
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

            # 获取图像的高度和宽度
            height, width = cv_image.shape[:2]

            # 在图像右上角绘制红色矩形
            cv2.rectangle(cv_image, 
                          (width - 120, 20), 
                          (width - 20, 120),
                          (0, 0, 255), 2)

            # 将处理后的 OpenCV 图像转换回 ROS 图像消息
            ros_image = self.bridge.cv2_to_imgmsg(cv_image, 'bgr8')

            # 发布处理后的图像消息
            self.publisher.publish(ros_image)

        except Exception as e:
            self.get_logger().error(f'处理图像时出错: {str(e)}')


def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriberAndPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点关闭')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()