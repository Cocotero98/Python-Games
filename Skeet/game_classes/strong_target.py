from game_classes.Target import Target
import arcade
import constants

class StrongTarget(Target):
    
    def __init__(self):
        super().__init__(1,3,-2,3)
        self.lives=3

    def draw(self):
        arcade.draw_circle_outline(self.center.get_x(), self.center.get_y(), self.radius, constants.TARGET_COLOR)
        text_x = self.center.get_x() - (self.radius / 2)
        text_y = self.center.get_y() - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, constants.TARGET_COLOR, font_size=20)

    def hit(self):
        if self.lives==1:
            self.points=5
        return super().hit()