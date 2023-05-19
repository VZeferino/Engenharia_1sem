#Aconteceu alguma coisa no código que eu não consegui identificar o que é e quando eu rodo o turtlesim ele simplismente começa a ir para frente... não sei por que... Não consegui identificar qual foi o problema exatamente. Entretanto entrego até onde consegui completar e desenvolver.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

MAX_DIFF = 0.1

positions = [
    [0.0,0.5],
    [0.5,0.0],
    [0.0,0.5],
    [0.5,0.0],
    [0.0,1.0],
    [1.0,0.0]
]

class turtlesim(Node):
    def __init__(self):
        super().__init__("turtlecontroller")
        self.talker = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.listen = self.create_subscription(Pose, "/turtle1/pose", self.odometria, 10)

    def odometria(self, pose:Pose): 
        valor = 0
        x = pose.x
        y = pose.y
        ang = pose.theta
        
        difference_x = positions[valor][0] - x
        difference_y = positions[valor][1] - y

        mathematics = math.atan2(difference_y, difference_x)

        dif_ang_total = ang - mathematics
        message = Twist()

        if abs(dif_ang_total) > MAX_DIFF:
            message.angular.z = 0.3
            message.linear.x = 0.0

        if (abs(positions[valor][0] - x) > 0.25) and (abs(positions[valor][1] - y) > 0.25):
            message.linear.x = 0.5
            message.angular.z = 0.0
        else:
            message.linear.x = 0.0
            message.angular.z = 0.0
            if abs(dif_ang_total) < MAX_DIFF:
                valor += 1
            if valor == len(positions):
                valor -= 1
        
        self.talker.publish(message)
        self.get_logger().info(f"x={round(x, 2)},y={round(y, 2)}, dif_ang_total={abs(round(dif_ang_total, 2))}")

def main(args=None):
    rclpy.init(args=args)
    node = turtlesim()
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == "__main__":
    main()