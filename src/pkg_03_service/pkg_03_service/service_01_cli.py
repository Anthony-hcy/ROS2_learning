import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class Client(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.cli = self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1):
            self.get_logger().info('等待服务启动...')
        self.req = AddTwoInts.Request()

    def call_service(self,a,b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req) 
        #rclpy.spin_until_future_complete(self, self.future)   
        #return self.future.result()                           
        while rclpy.ok():
            rclpy.spin_once(self)          
            if self.future.done():         
                if self.future.result() is not None:
                    return self.future.result()
                else:
                    return None

def main():
    rclpy.init()
    node = Client('service_client')
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    response = node.call_service(a, b)
    node.get_logger().info(f'{a} + {b} = {response.sum}')
    rclpy.shutdown()
