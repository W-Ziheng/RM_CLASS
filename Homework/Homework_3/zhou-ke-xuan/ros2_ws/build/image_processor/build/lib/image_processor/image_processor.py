#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        
        # 初始化摄像头捕获
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # 创建图像发布者
        self.publisher = self.create_publisher(Image, '/processed_image', 10)
        self.bridge = CvBridge()
        
        # 定时器回调
        self.timer = self.create_timer(0.033, self.capture_callback)  # 30Hz

    def capture_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # 绘制红色矩形
            height, width = frame.shape[:2]
            cv2.rectangle(frame, 
                        (width-120, 20), 
                        (width-20, 120),
                        (0, 0, 255), 2)
            
            # 转换并发布ROS消息
            ros_image = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
            self.publisher.publish(ros_image)
            
        else:
            self.get_logger().error('摄像头读取失败')

    def __del__(self):
        self.cap.release()

def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('节点关闭')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
