import arcade
import constants
from game_classes.Target import Target

class StandardTarget(Target):
    def __init__(self):
        super().__init__(1,5,-2,5)
        

    def draw(self):
        arcade.draw_circle_filled(0,self.y,constants.TARGET_RADIUS,constants.TARGET_COLOR)

