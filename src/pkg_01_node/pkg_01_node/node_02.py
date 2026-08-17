import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name:str,age:int) -> None:
        print('PersonNode __init__被调用')
        super().__init__(node_name)
        self.name = node_name
        self.age = age

    def eat(self,food_name:str):
        self.get_logger().info(f'我是{self.name},{self.age}岁,爱吃{food_name}')

def main():
    rclpy.init()
    node = PersonNode('LiHua',18)
    node.eat('薯片')
    rclpy.spin(node)
    rclpy.shutdown()
