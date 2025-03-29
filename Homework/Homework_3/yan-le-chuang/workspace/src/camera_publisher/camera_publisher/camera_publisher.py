import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):

    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)
        timer_period = 0.1  # 发布周期秒数
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.br = CvBridge()
        self.cap = cv2.VideoCapture(0)  # 使用第一个摄像头

    def timer_callback(self):
        ret, frame = self.cap.read()  # 读取摄像头图像
        if ret:
            msg = self.br.cv2_to_imgmsg(frame,encoding='bgr8')  # 转换图像为ROS消息
            self.publisher_.publish(msg)  # 发布消息
            self.get_logger().info('Publishing image')
        else:
            self.get_logger().info('Failed to read frame')

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()  # 释放摄像头资源

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
