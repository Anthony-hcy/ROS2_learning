from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    xacro_file = PathJoinSubstitution([
        FindPackageShare('learning_urdf'),
        'urdf',
        'fishbot',
        'fishbot.urdf.xacro'
    ])
    robot_description = Command(['xacro ',xacro_file])
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        ExecuteProcess(
            cmd=['rviz2', '-d', '/opt/ros/humble/share/urdf_tutorial/rviz/urdf.rviz'],
            output='screen'
        )
    ])
