import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from pkg_04_interface.action import Learningaction

class CountdownClient(Node):
    def __init__(self):
        super().__init__('action_client')
        self.action_client = ActionClient(self, Learningaction, 'countdown')
        self.get_logger().info('动作客户端已初始化')

    def send_goal(self, duration):
        self.action_client.wait_for_server()
        self.get_logger().info(f'发送目标：倒计时 {duration} 秒')
        goal = Learningaction.Goal()
        goal.duration = duration
        send_goal_future = self.action_client.send_goal_async(goal, feedback_callback=self.feedback_callback)
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().info('目标被拒绝')
            return
        self.get_logger().info('目标已被接受，等待执行结束...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        result = result_future.result().result
        if result.success:
            self.get_logger().info('结果：倒计时成功完成！')
        else:
            self.get_logger().warn('结果：倒计时未成功（或被取消）')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        current = feedback_msg.feedback.current_number
        self.get_logger().info(f'收到反馈：当前倒计时 {current}')

def main():
    rclpy.init()
    node = CountdownClient()
    import sys
    duration = 5
    if len(sys.argv) > 1:
        duration = int(sys.argv[1])
    node.send_goal(duration)
