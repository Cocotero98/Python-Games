import constants
from game_classes.shared.point import Point
import random
import arcade

class FlyingObject:

    def __init__(self):
        self.center=Point(0,0)
        self.velocity= Point(0,0)
        self.radius= 3
        self.alive=True
        pass

    def advance(self):
        # print(self.center.get_x(),self.center.get_y())
        x = (self.center.get_x() + self.velocity.get_x())
        y = (self.center.get_y() + self.velocity.get_y())
        self.center = Point(x, y)
        # print(x,y)
        pass

    def draw(self) : None

    def is_off_screen(self,screen_width, screen_height):
        if screen_width < self.center.get_x() or screen_height < self.center.get_y():
            return True
            


