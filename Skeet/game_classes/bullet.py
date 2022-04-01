import constants
from game_classes.flying_object import FlyingObject
import arcade
import math
from game_classes.shared.point import Point

class Bullet(FlyingObject):
    """
    Small flying circle representing a bullet
    """

    def __init__(self):
        super().__init__()
        self._speed= constants.BULLET_SPEED
        self.radius= constants.BULLET_RADIUS


    def draw(self):
        arcade.draw_circle_filled(self.center.get_x(),self.center.get_y(),self.radius,constants.BULLET_COLOR)

    def fire(self,angle):
        """
        Sets the direction for the bullet according to the given angle
        :param angle: angle in degrees
        """
        dx = math.cos(math.radians(angle)) * self._speed
        dy = math.sin(math.radians(angle)) * self._speed
        self.velocity=Point(dx,dy)

