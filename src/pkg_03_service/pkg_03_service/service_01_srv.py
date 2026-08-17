import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Server(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.srv = self.create_service(AddTwoInts,'add_two_ints',self.callback)
        self.get_logger().info(f'{node_name}已启动，等待请求...')

    def callback(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info(f'收到：{request.a} + {request.b} = {response.sum}')
        return response

def main():
    rclpy.init()
    node = Server('service_server')
    rclpy.spin(node)
    rclpy.shutdown()
