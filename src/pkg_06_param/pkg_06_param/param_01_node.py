import rclpy
from rclpy.node import Node

class ParamNode(Node):
    def __init__(self):
        super().__init__('param_node')
        self.declare_parameter('my_name','World')
        self.name = self.get_parameter('my_name').value
        self.get_logger().info(f'节点启动，当前名字: {self.name}')
        self.add_on_set_parameters_callback(self.param_callback)
        self.timer = self.create_timer(1.5,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f'Hello {self.name}!')

    def param_callback(self,params):
        for param in params:
            if param.name == 'my_name':
                self.name = param.value
                self.get_logger().info(f'名字已更新为: {self.name}')
        return True

def main():
    rclpy.init()
    node = ParamNode()
    rclpy.spin(node)
    rclpy.shutdown()
