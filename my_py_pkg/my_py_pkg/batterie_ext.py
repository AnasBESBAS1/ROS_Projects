#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import time


class BatterieExt(Node):

    def __init__(self):
        super().__init__("batterie_ext")
        self.get_logger().info("La batterie_node a été démarré")
        self.battery_state = [0,0,0]

        client = self.create_client(SetBool, "reset_counter_server")
        while not client.await_for_service(1.0):
            self.get_logger().warn("En attente du serveur number server..")
        self.publisher_ = self.create_publisher(Int64,"number_count",10)
        self.timer_ = self.create_timer(0.5,self.publish_counter)
        self.get_logger().info("Le number_counter node a été démarré")
        self.i = 0

    def callback_counter(self,msg):
        self.i += 1


    def publish_counter(self):
        msg2 = Int64()
        msg2.data = self.i
        self.publisher_.publish(msg2)
        self.get_logger().info('Publishing: "%s"' % msg2.data)

def main(args=None):
    rclpy.init(args=args)
    node = BatterieExt()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
