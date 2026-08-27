from launch import LaunchDescription 
from launch_ros.actions import Node

def generate_launch_description():             
    return LaunchDescription([                 
        Node(                                  
            package='pkg_02_topic',          
            executable='topic_01_pub', 
        ),
        Node(                                  
            package='pkg_02_topic',          
            executable='topic_01_sub', 
        ),
    ])
