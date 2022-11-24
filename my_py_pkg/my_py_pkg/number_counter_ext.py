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
        self.i = 0

    def callback_counter(self,msg):
        self.i += 1


    def publish_counter(self):
        msg2 = Int64()
        msg2.data = self.i
        self.publisher_.publish(msg2)
        self.get_logger().info('Publishing: "%s"' % msg2.data)


    def callback_add_two_ints_server(self):
        client = self.create_client(SetBool, "reset_counter_server")
        while not client.await_for_service(1.0):
            self.get_logger().warn("En attente du serveur number server..")

        request = SetBool.Request()
        request.success = True
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_add_two_ints,success=success))

    def callback_call_add_two_ints(self, future,success):
        try:
            response = future.result()
            if (success == True):
                self.i = 0
        except Exception as e:
            self.get_logger().error("Appel defailant au service %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = CounterReset()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
