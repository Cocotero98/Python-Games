from game_classes.Target import Target
import arcade
import constants

class StrongTarget(Target):
    
    def __init__(self):
        super().__init__(1,3,-2,3)
        self.lives=3
        if self.lives>1:
            self.points=1
        else:
            self.points=0

    def draw(self):
        arcade.draw_circle_outline(0, self.y, self.radius, constants.TARGET_COLOR)
        text_x = 0 - (self.radius / 2)
        text_y = self.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, constants.TARGET_COLOR, font_size=20)

