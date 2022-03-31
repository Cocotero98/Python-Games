from game_classes.Target import Target
import arcade
import constants

class SafeTarget(Target):
    
    def __init__(self):
        super().__init__(1,5,-2,5)
        self.points=-10

    def draw(self):
        arcade.draw_rectangle_filled(0,self.y,20,20,constants.TARGET_SAFE_COLOR,0)