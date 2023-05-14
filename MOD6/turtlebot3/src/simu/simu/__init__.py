import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry as Odometry
from tf_transformations import euler_from_quaternion
import math

#valor máximo de diferença para mostrar que o robô atingiu a posição.
MAX_DIFF = 0.1

#essa é a lista de posições que o robô deve percorrer, ela forma um Z de Zeferino.
positions = [
    [0.0, 2.0],
    [-2.0, 0.0],
    [-2.0, 2.0]
]

#a classe que cria o publicador da velocidade, o que vai "ouvir" e um controlador de tempo para chamar a função
class LESGO(Node):
    def __init__(self, control_period=0.02):
        super().__init__("controller")
        self.valor = 0
        self.odom_x = 0.0
        self.odom_y = 0.0
        self.prox_x = 0.0
        self.prox_y = 0.0
        self.theta = 0.0

        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.subscriber = self.create_subscription(Odometry, "/odom", self.callback_position, 10)
        self.control_timer = self.create_timer(control_period, self.callback_control)

    #essa função serve para termos as posições atuais do robô, atualiza suas coordenadas e também printa
    #no console a posição do robô
    def callback_position(self, message):
        x = message.pose.pose.position.x
        y = message.pose.pose.position.y
        a = message.pose.pose.orientation
        self.theta = euler_from_quaternion([a.x, a.y, a.z, a.w])[2]

        self.odom_x = x
        self.odom_y = y

        self.get_logger().info(f"Posição do robô: X = {x}, Y = {y}, A = {a}")

    #função que faz alguns calculos utilizando as posições para controlar o robô
    #além de fazer verificações se ele está próximo do ponto, mandar para o próximo ponto de destino
    #e também controlar a velocidade pelo message
    def callback_control(self):
        message = Twist()
        self.prox_x = positions[self.valor][0]
        self.prox_y = positions[self.valor][1]

        difference_x = self.prox_x - self.odom_x
        difference_y = self.prox_y - self.odom_y

        mathematics = math.atan2(difference_y, difference_x)

        difference_a = mathematics - self.theta

        if abs(difference_x) < MAX_DIFF and abs(difference_y) < MAX_DIFF:
            self.valor += 1

        if abs(difference_a) > MAX_DIFF:
            message.linear.x = 0.0
            message.angular.z = 0.4 if difference_a > 0.0 else -0.4
        else:
            message.linear.x = 0.8
            message.angular.z = 0.0
        self.publisher.publish(message)

        if self.valor == len(positions):
            self.valor = 0



def main():
    rclpy.init(args=None)
    run = LESGO()
    rclpy.spin(run)
    run.destroy_node()
    rclpy.shutdown()
