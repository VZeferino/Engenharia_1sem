import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry as Odometry
from time import sleep
from tf_transformations import euler_from_quaternion
import math

MAX_DIFF = 0.1

global positions
positions = [
            [2.0,0.0],
            [0.0,-3.0],
            [2.0,-3.0]
            ]

class LESGO(Node):
    def __init__(self, control_period = 0.02):
        super().__init__("controller")
        self.valor = 0
        self.odom = Odometry()
        self.odom_x = self.odom.pose.pose.position.x
        self.odom_y = self.odom.pose.pose.position.y

        self.prox_x = self.odom.pose.pose.position.x
        self.prox_y = self.odom.pose.pose.position.y

        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.subscriber = self.create_subscription(Odometry, "/odom", self.callback_position, 10)
        self.control_timer = self.create_timer(control_period, self.callback_control)
        
    def callback_position(self, message):
        x = message.pose.pose.position.x
        y = message.pose.pose.position.y
        a = message.pose.pose.orientation
        _, _, self.theta = euler_from_quaternion([a.x, a.y, a.z, a.w])

        self.odom_x = x
        self.odom_y = y

        self.get_logger().info(f"Posição do robô: X = {x}, Y = {y}, A = {a}")

    def callback_control(self):
        message = Twist()
        self.prox_x = positions[self.valor+1][0]
        self.prox_y = positions[self.valor+1][1]

        diference_x = self.prox_x - self.odom_x
        diference_y = self.prox_y - self.odom_y

        mathematics = math.atan2(diference_y, diference_x)

        # diference_a = mathematics - self.theta

        if abs(diference_x) < MAX_DIFF and abs(diference_y) < MAX_DIFF:
            self.valor += 1

        if abs(mathematics - self.theta) > MAX_DIFF:
            message.linear.x = 0.0
            message.angular.z = 0.1 if (mathematics - self.theta) > 0 else -0.1
        else: message.linear.x = 0.2

        if self.valor == len(positions):
            self.valor = 0

def main():
    rclpy.init(args=None)
    run = LESGO()
    rclpy.spin(run)
    run.destroy_node()
    rclpy.shutdown()