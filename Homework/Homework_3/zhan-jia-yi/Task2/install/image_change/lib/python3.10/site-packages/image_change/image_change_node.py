#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os

class ImageProcessor(Node):
    def __init__(self):
        # 调用父类 Node 的构造函数，创建名为 'image_processor' 的节点
        super().__init__('image_processor')

        # 摄像头参数
        self.camera_index = 0
        self.frame_width = 640
        self.frame_height = 480

        # 矩形绘制参数
        self.rect_x1 = 20
        self.rect_y1 = 20
        self.rect_x2 = 120
        self.rect_y2 = 120
        self.rect_color = (0, 0, 255)
        self.rect_thickness = 2

        # 摄像头初始化标志
        self.camera_initialized = False

        # 检查摄像头设备是否存在
        camera_device = f"/dev/video{self.camera_index}"
        if not os.path.exists(camera_device):
            self.get_logger().error(f"摄像头设备 {camera_device} 不存在")
        else:
            try:
                # 使用指定的摄像头索引打开摄像头
                self.cap = cv2.VideoCapture(self.camera_index)
                if not self.cap.isOpened():
                    # 如果摄像头无法打开，记录错误信息
                    self.get_logger().error('无法打开摄像头')
                else:
                    # 设置摄像头捕获的图像宽度
                    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
                    # 设置摄像头捕获的图像高度
                    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
                    self.get_logger().info('摄像头已成功初始化')
                    self.camera_initialized = True
            except Exception as e:
                # 捕获初始化过程中的异常，记录错误信息
                self.get_logger().error(f'摄像头初始化失败: {str(e)}')

        if not self.camera_initialized:
            # 如果摄像头初始化失败，清理资源并关闭节点
            self.cleanup_and_shutdown()
            return

        # 创建一个图像发布者，发布的消息类型为 Image，话题名称为 '/processed_image'，队列大小为 10
        self.publisher = self.create_publisher(Image, '/processed_image', 10)
        # 创建 CvBridge 对象，用于在 OpenCV 图像和 ROS 2 图像消息之间进行转换
        self.bridge = CvBridge()

        # 创建一个定时器，每隔 0.033 秒（约 30Hz）调用一次 capture_callback 函数
        self.timer = self.create_timer(0.033, self.capture_callback)

        # 显示窗口名称
        self.window_name = 'Processed Image'
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

    def capture_callback(self):
        if not self.camera_initialized:
            return

        try:
            # 从摄像头读取一帧图像
            ret, frame = self.cap.read()
            if ret:
                # 获取图像的高度和宽度
                height, width = frame.shape[:2]

                # 动态计算矩形的位置
                rect_start = (width - self.rect_x2, self.rect_y1)
                rect_end = (width - self.rect_x1, self.rect_y2)

                # 在图像上绘制矩形
                cv2.rectangle(frame, rect_start, rect_end, self.rect_color, self.rect_thickness)

                # 显示处理后的图像
                cv2.imshow(self.window_name, frame)
                cv2.waitKey(1)

                # 将 OpenCV 图像转换为 ROS 2 的 Image 消息，图像格式为 'bgr8'
                ros_image = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
                # 发布处理后的图像消息到 /processed_image 话题
                self.publisher.publish(ros_image)
            else:
                # 如果读取失败，记录错误信息
                self.get_logger().error('无法从摄像头读取图像帧')
        except Exception as e:
            # 捕获捕获和处理图像过程中的异常，记录错误信息
            self.get_logger().error(f'处理图像时发生错误: {str(e)}')

    def cleanup_and_shutdown(self):
        # 释放摄像头资源
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        # 关闭所有 OpenCV 窗口
        cv2.destroyAllWindows()
        # 销毁节点
        if self.context.ok():
            self.destroy_node()
            # 关闭 ROS 2
            rclpy.shutdown()

    def __del__(self):
        # 避免在析构函数中进行复杂操作
        pass

def main(args=None):
    # 初始化 ROS 2
    rclpy.init(args=args)
    node = None
    try:
        # 创建 ImageProcessor 类的实例
        node = ImageProcessor()
        try:
            # 进入节点的主循环，等待回调函数被调用
            rclpy.spin(node)
        except KeyboardInterrupt:
            # 捕获用户按下 Ctrl+C 的信号，记录节点关闭信息
            if node:
                node.get_logger().info('节点因用户中断而关闭')
        finally:
            # 清理资源
            if node:
                node.cleanup_and_shutdown()
    except Exception as e:
        # 捕获创建节点过程中的异常，记录错误信息
        rclpy.logging.get_logger('main').error(f'创建节点时发生错误: {str(e)}')
        if node:
            node.cleanup_and_shutdown()
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    # 当脚本作为主程序运行时，调用 main 函数
    main()