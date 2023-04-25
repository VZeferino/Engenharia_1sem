#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(3, self.move_turtle)
        self.twist_msg_ = Twist()

    def move_turtle(self):
        self.pos_turtle(3.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, -3.0, 0.0) 
        sleep(2)
        self.pos_turtle(-3.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 3.0, 0.0) 
        sleep(2)
        self.pos_turtle(3.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, -3.0, 0.0) 
        sleep(2)
        self.pos_turtle(-1.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 1.0, 0.0) 
        sleep(2)
        self.pos_turtle(-1.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, -1.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.5, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 1.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, -0.5, 0.0) 
        sleep(2)
        self.pos_turtle(0.1, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(-0.2, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.1, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, -0.5, 0.0) 
        sleep(2)
        self.pos_turtle(1.5, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 3.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 0.0, 2.094) 
        sleep(2)
        self.pos_turtle(3.0, 0.0, 0.0) 
        sleep(2)
        self.pos_turtle(0.0, 0.0, 2.094) 
        sleep(2)
        self.pos_turtle(3.0, 0.0, 0.0) 
        sleep(2)
        self.stop_turtle()
        

    def pos_turtle(self, x, y, z):
        self.twist_msg_.linear.x = x
        self.twist_msg_.linear.y = y
        self.twist_msg_.angular.z = z
        self.publisher_.publish(self.twist_msg_)

    def stop_turtle(self):
        while True:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.linear.y = 0.0
            self.twist_msg_.linear.z = 0.0


def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
