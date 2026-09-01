import rclpy                                                                
from rclpy.node import Node                                                  
from geometry_msgs.msg import TransformStamped                              
import tf_transformations                                                   
from tf2_ros import TransformBroadcaster  

class DynamicTFBroadcaster(Node):
    def __init__(self, name):
        super().__init__(name)                                                  
        self.tf_broadcaster = TransformBroadcaster(self)   
        self.timer_ = self.create_timer(0.01, self.publish_dynamic_tf)     

    def publish_dynamic_tf(self):
        dynamic_transformStamped = TransformStamped()                           
        dynamic_transformStamped.header.stamp = self.get_clock().now().to_msg()  
        dynamic_transformStamped.header.frame_id = 'house'                      
        dynamic_transformStamped.child_frame_id  = 'work'                       
        dynamic_transformStamped.transform.translation.x = 20.0                 
        dynamic_transformStamped.transform.translation.y = 10.0                    
        dynamic_transformStamped.transform.translation.z = 0.0
        quat = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)          
        dynamic_transformStamped.transform.rotation.x = quat[0]                  
        dynamic_transformStamped.transform.rotation.y = quat[1]
        dynamic_transformStamped.transform.rotation.z = quat[2]
        dynamic_transformStamped.transform.rotation.w = quat[3]
        self.tf_broadcaster.sendTransform(dynamic_transformStamped)    
                 
def main():
    rclpy.init()                                
    node = DynamicTFBroadcaster("dynamic_tf_bro") 
    rclpy.spin(node)                                     
    rclpy.shutdown()
