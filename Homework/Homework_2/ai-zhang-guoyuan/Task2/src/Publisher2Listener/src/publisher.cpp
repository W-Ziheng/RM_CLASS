#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

using namespace std::chrono_literals;

class PublisherNode : public rclcpp::Node
{
public:
    PublisherNode() : Node("publisher_node")
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("welcome_topic", 10);
        timer_ = this->create_wall_timer(
            1s, std::bind(&PublisherNode::timer_callback, this));  // 每秒发布一次消息
    }

private:
    void timer_callback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Welcome to RM!";  // 发布的消息
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PublisherNode>());
    rclcpp::shutdown();
    return 0;
}