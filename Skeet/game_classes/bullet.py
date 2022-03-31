import constants
from game_classes.flying_object import FlyingObject
import arcade
import math
from game_classes.shared.point import Point

class Bullet(FlyingObject):

    def __init__(self):
        super().__init__()
        self._speed= constants.BULLET_SPEED
        self.radius= constants.BULLET_RADIUS


    def draw(self):
        arcade.draw_circle_filled(0,0,constants.BULLET_RADIUS,constants.BULLET_COLOR)

    def fire(self,angle):
        dx = math.cos(math.radians(angle)) * self._speed
        dy = math.sin(math.radians(angle)) * self._speed
        self.velocity=Point(dx,dy)

