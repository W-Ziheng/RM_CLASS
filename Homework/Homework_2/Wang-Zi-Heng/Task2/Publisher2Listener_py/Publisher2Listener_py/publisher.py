# publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'welcome_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 每秒发布一次消息
        self.get_logger().info("Publisher node has started.")

    def timer_callback(self):
        msg = String()
        msg.data = "Welcome to RM!"  # 发布的消息
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: '{msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()