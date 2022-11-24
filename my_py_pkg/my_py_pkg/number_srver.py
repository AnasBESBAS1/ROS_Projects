from example_interfaces.srv import SetBool
import rclpy
from rclpy.node import Node


class InisializerService(Node):
    def __init__(self):
        super().__init__('reset_counter_server')
        self.srv = self.create_service(SetBool, 'reset_counter_server', self.set_to_zero_callback)
        self.get_logger().info('the reset_counterr server is on')

    def set_to_zero_callback(self, request, response):
        response.success = True
        
        self.get_logger().info('Incoming request')

        return response

def main(args=None):
    rclpy.init(args=args)
    service = InisializerService()
    rclpy.spin(service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
