from pkg_01_node.node_02 import PersonNode
import rclpy

class WriterNode(PersonNode):
    def __init__(self, node_name:str, age:int,book:str) -> None:
        print('WriterNode被调用了')
        super().__init__(node_name, age)
        self.book = book
        
    def write(self):
        self.get_logger().warning(f'我是{self.name},{self.age}岁,爱看{self.book}')

def main():
    rclpy.init()
    node = WriterNode('ZhangSan',20,'English')
    node.eat('water')
    node.write()
    rclpy.spin(node)
    rclpy.shutdown()
