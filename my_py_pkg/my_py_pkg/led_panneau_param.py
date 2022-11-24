#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool
from std_msgs.msg import String
from std_msgs.msg import Int64

class Panneau(Node):
    led_pannel = []

    def __init__(self):
        super().__init__("led_panneau")
        self.declare_parameter('led_states',[0,0,0])
        self.service_ = self.create_service(SetBool, 'set_led', self.set_led_callback)
        self.get_logger().info('the set_led server is on')
        self.timer_ = self.create_timer(0.5,self.publish_led_status)
        self.publisher_ = self.create_publisher(String,"led_states",10)
        self.led_pannel = self.get_parameter('led_states').get_parameter_value()


    def publish_led_status(self):
        message = String()
        message.data = "{}".format(self.led_pannel)
        self.publisher_.publish(message)


    def set_led_callback(self, request, response):
        self.activated_ = request.data
        response.success = True
        if self.activated_:
            response.message = "service exe success "
            self.led_pannel = [0,0,1]
            self.get_logger().info('LED is on {}, Batterie en charge...'.format(self.led_pannel))
        else:
            self.led_pannel = [0,0,0]
            self.get_logger().info('LED is OFF  {}'.format(self.led_pannel))
            response.message = "LED is off"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Panneau()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
