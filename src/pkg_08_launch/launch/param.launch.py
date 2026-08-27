import launch
import launch_ros

def generate_launch_description():
    # 1.声明一个launch参数
    action_declare_arg_background_g = launch.actions.DeclareLaunchArgument\
    ('launch_arg_bg', default_value='150')
    # 2.把launch的参数手动传递给某个节点
    """产生launch描述"""
    action_node_turtlesim_node = launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[{'background_g': launch.substitutions.LaunchConfiguration('launch_arg_bg', default='150')}],      
    )
    action_node_topic_01_pub = launch_ros.actions.Node(
        package='pkg_02_topic',
        executable='topic_01_pub',    
    )
    action_node_topic_01_sub = launch_ros.actions.Node(
        package='pkg_02_topic',
        executable='topic_01_sub',     
    )
    return launch.LaunchDescription([
        # actions 动作
        action_declare_arg_background_g,
        action_node_turtlesim_node,
        action_node_topic_01_pub,
        action_node_topic_01_sub,
    ])
