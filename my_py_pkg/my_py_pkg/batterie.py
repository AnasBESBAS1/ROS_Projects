#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool
from std_msgs.msg import Int64
import time

class Batterie(Node):

    def __init__(self):
        super().__init__("batterie")
        self.get_logger().info("La batterie_node a été démarré")
        self.battery_state = [0,0,0]
        self.cli = self.create_client(SetBool, "set_led")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetBool.Request()

    # server callback
    def send_request(self,state):
        self.req.data = state
        self.future = self.cli.call_async(self.req)
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    node = Batterie()
    while True:
        time.sleep(4)
        print("Batterie is working ")
        response = node.send_request(True)
        node.battery_state = [0,0,0]
        print("Batterie est vide : ", node.battery_state, response.success)
        time.sleep(6)
        node.battery_state = [1,1,1]
        response = node.send_request(False)
        print("Batterie est plein : ", node.battery_state, response.success)

    rclpy.shutdown()


if __name__=="__main__":
    main()
