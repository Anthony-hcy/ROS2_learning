from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf_path = '/home/hcy/ros_ws/src/learning_urdf/urdf/first_robot.urdf'
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_path).read()}]
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