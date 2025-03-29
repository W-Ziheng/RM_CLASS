import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
import numpy as np

class ImageProcessorNode(Node):

    def __init__(self):
        super().__init__('image_processor_node')
        
        # 创建一个CvBridge对象
        self.bridge = CvBridge()
        
        # 订阅原始图像话题
        self.subscription = self.create_subscription(
            Image,
            'camera/image_raw',
            self.listener_callback,
            10)
        self.subscription  # 防止警告未使用
        
        # 创建一个发布者发布处理后的图像
        self.publisher_ = self.create_publisher(Image, '/image_processor/output_image', 10)

    def listener_callback(self, msg):
        # 将ROS2图像消息转换为OpenCV图像
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # 将图像转换为HSV颜色空间（更好的颜色分离）
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 定义绿色的HSV范围（需要根据实际情况调整）
        lower_green = np.array([40, 100, 100])
        upper_green = np.array([100, 255, 255])
    
        # 创建绿色掩膜
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # 图像预处理
        mask = cv2.GaussianBlur(mask, (9, 9), 2)

        # 定义结构元素
        kernel = np.ones((5, 5), np.uint8)

        # 膨胀操作
        mask = cv2.dilate(mask, kernel, iterations=1)

        # 侵蚀操作
        mask = cv2.erode(mask, kernel, iterations=1)

        # 边缘检测
        edges = cv2.Canny(mask, 50, 150)

        # 查找轮廓
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 遍历每一个轮廓
        for contour in contours:
            # 轮廓近似
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 如果轮廓近似后的顶点数为3，则绘制三角形
            if len(approx) == 3:
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)
        
        # 在图像右上角绘制白色的矩形
        height, width, _ = frame.shape
        cv2.rectangle(frame, (width-100, 0), (width, 100), (255, 255, 255), 2)

        # 显示结果
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        # 按q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rclpy.shutdown()  # 关闭ROS2，防止无限循环

        # 将处理后的图像转换回ROS2消息格式
        output_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        # 发布处理后的图像
        self.publisher_.publish(output_msg)

def main(args=None):
    rclpy.init(args=args)
    image_processor_node = ImageProcessorNode()
    rclpy.spin(image_processor_node)
    image_processor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
