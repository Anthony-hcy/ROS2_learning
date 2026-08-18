import rclpy
from rclpy.node import Node
from pkg_04_interface.msg import Learningmsg

class Subscriber(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        self.subscriber_ = self.create_subscription(Learningmsg,'topic',self.Sub_callback,100)
        self.get_logger().info("Waiting pub...")

    def Sub_callback(self,msg):
        self.get_logger().info(f"收到：'{msg.message}'")

def main():
    rclpy.init()
    node = Subscriber('topic_sub')
    rclpy.spin(node)
    rclpy.shutdown()
