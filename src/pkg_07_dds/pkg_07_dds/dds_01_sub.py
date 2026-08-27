import rclpy
from rclpy.node import Node
from std_msgs.msg import String                
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class Subscriber(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        qos_profile = QoSProfile(
                    reliability=QoSReliabilityPolicy.RELIABLE,
                    history=QoSHistoryPolicy.KEEP_LAST,
                    depth=1)
        self.subscriber_ = self.create_subscription(String,'dds',self.Sub_callback,qos_profile)
        self.get_logger().info("Waiting pub...")

    def Sub_callback(self,msg):
        self.get_logger().info(f"收到：'{msg.data}'")

def main():
    rclpy.init()
    node = Subscriber('dds_sub')
    rclpy.spin(node)
    rclpy.shutdown()
