import rclpy
from rclpy.node import Node
from pkg_04_interface.msg import Learningmsg  #自定义接口

class Publisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        self.publisher_ = self.create_publisher(Learningmsg,'topic',10)
        self.count_ = 0
        self.timer_ = self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        msg = Learningmsg()
        msg.message = f"Hell, ROS 2! {self.count_}"
        self.count_ += 1
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.message}"')

def main():
    rclpy.init()
    node = Publisher('topic_pub')
    rclpy.spin(node)
    rclpy.shutdown()