import rclpy
from rclpy.node import Node
from pkg_04_interface.action import Learningaction
from rclpy.action import ActionServer
import time

class CountdownServer(Node):
    def __init__(self):
        super().__init__('action_server')
        self._action_server = ActionServer(self,Learningaction,'countdown',self.execute_callback)
        self.get_logger().info(f'动作服务端已启动，等待目标...')

    def execute_callback(self,goal_handle):
        duration = goal_handle.request.duration
        self.get_logger().info(f'收到倒计时目标：{duration} 秒')
        feedback = Learningaction.Feedback()
        result = Learningaction.Result()

        for i in range(duration, 0, -1):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().warn('动作被取消')
                result.success = False
                return result
            feedback.current_number = i
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f'反馈：倒计时 {i}')
            time.sleep(1)
        goal_handle.succeed()
        result.success = True
        self.get_logger().info('倒计时完成！')
        return result

def main():
    rclpy.init()
    node = CountdownServer()
    rclpy.spin(node)
    rclpy.shutdown()
