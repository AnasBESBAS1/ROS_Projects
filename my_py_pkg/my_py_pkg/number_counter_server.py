#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool
from example_interfaces.srv import AddTwoInts
from std_msgs.msg import Int64

class CounterReset(Node):
    def __init__(self):
        super().__init__("reset_counter_client")
        self.subscription = self.create_subscription(Int64, "number", self.callback_counter,10)
        self.subscription
        self.publisher_ = self.create_publisher(Int64,"number_count",10)
        self.timer_ = self.create_timer(0.5,self.publish_counter)
        self.get_logger().info("Le number_counter node a été démarré")
        self.service_ = self.create_service(SetBool, 'reset_number_count', self.set_to_zero_callback)
        self.get_logger().info('the reset_number_count server is on')
        self.counter = 0

    # server callback
    def set_to_zero_callback(self, request, response):
        self.activated_ = request.data
        response.success = True
        if self.activated_:
            response.message = "service exe success "
            self.counter = 0
            self.get_logger().info('reset_counter is on ')
        else:
            response.message = "reset_counter is on off"
        return response

    #subscription callback
    def callback_counter(self,msg):
        self.counter += 1

    # publisher callback
    def publish_counter(self):
        msg2 = Int64()
        msg2.data = self.counter
        self.publisher_.publish(msg2)
        self.get_logger().info('Publishing: "%s"' % msg2.data)


def main(args=None):
    rclpy.init(args=args)
    node = CounterReset()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
