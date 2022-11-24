#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool
from std_msgs.msg import String
from std_msgs.msg import Int64

class Panneau(Node):
    panneau_ = [0,0,0]

    def __init__(self):
        super().__init__("led_panneau")
        self.service_ = self.create_service(SetBool, 'set_led', self.set_led_callback)
        self.get_logger().info('the set_led server is on')
        self.timer_ = self.create_timer(0.5,self.publish_led_status)
        self.publisher_ = self.create_publisher(String,"led_states",10)

    # publisher callback on led_states topic
    def publish_led_status(self):
        msg = String()
        msg.data = "{}".format(self.panneau_)
        self.publisher_.publish(msg)

    
    def set_led_callback(self, request, response):
        self.activated_ = request.data
        response.success = True
        if self.activated_:
            response.message = "service exe success "
            self.panneau_ = [0,0,1]
            self.get_logger().info('LED is on {}'.format(self.panneau_))
        else:
            self.panneau_ = [0,0,0]
            self.get_logger().info('LED is OFF  {}'.format(self.panneau_))
            response.message = "LED is off"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Panneau()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
