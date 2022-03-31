import constants
from game_classes.shared.point import Point
import random
from game_classes.flying_object import FlyingObject

class Target(FlyingObject):

    def __init__(self,x1,x2,y1,y2):
        super().__init__()
        self.y=random.randint(constants.SCREEN_HEIGHT/2,constants.SCREEN_HEIGHT)
        velocityx=random.randint(x1,x2)
        velocityy=random.randint(y1,y2)
        self.velocity=Point(velocityx,velocityy)
        self.center=Point(5,self.y)
        self.alive=True
        self.lives=1
        self.radius=constants.TARGET_RADIUS
        self.points=1

    def hit(self):
        self.lives-=1
        if self.lives==0:
            self.alive=False
        return int(self.points)
