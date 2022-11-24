#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import sys


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station_para")
        self.declare_parameter('robot_name')
        self.publisher_ = self.create_publisher(String,"robot_news",10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("La station Robot News a démarrée")

    def publish_news(self):
        msg = String()
        msg.data = "Bonjour, c'est " + self.get_parameter('robot_name').get_parameter_value().string_value + " de la station Robot News!"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
