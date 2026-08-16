import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node('node_01')
    node.get_logger().info('Hello Ros2 !')
    node.get_logger().warn('Hi Ros2 !')
    rclpy.spin(node)
    rclpy.shutdown()
