#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class NumberPublisher(Node):

    def __init__(self):
        super().__init__("number_publisher")
        self.publisher_ = self.create_publisher(Int64,"number",10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("number node a été démarrée")

    def publish_news(self):
        msg = Int64()
        msg.data = 1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
