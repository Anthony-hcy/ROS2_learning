import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class Publisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1)
        self.publisher_ = self.create_publisher(String,'dds',qos_profile)
        self.count_ = 0
        self.timer_ = self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"Hell, ROS 2! {self.count_}"
        self.count_ += 1
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main():
    rclpy.init()
    node = Publisher('dds_pub')
    rclpy.spin(node)
    rclpy.shutdown()
