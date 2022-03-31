from game_classes.Target import Target
import arcade
import constants

class SafeTarget(Target):
    
    def __init__(self):
        super().__init__(1,5,-2,5)
        self.points=-10

    def draw(self):
        arcade.draw_rectangle_filled(self.center.get_x(),self.center.get_y(),40,40,constants.TARGET_SAFE_COLOR)