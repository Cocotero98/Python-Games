import constants
from game_classes.shared.point import Point
import random
from game_classes.flying_object import FlyingObject

class Target(FlyingObject):

    def __init__(self,x1,x2,y1,y2):
        """
        Sets up a target attributes
        :param int x1: first number in range for horizontal speed 
        :param int x2: last number in range for horizontal speed range
        :param int y1: first number in range for vertical speed 
        :param int y2: last number in range for vertical speed 
        """
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
        self.message=''

    def hit(self):
        """
        Subtract lives from the target and returns an ammount of points
        according to the target
        """
        self.lives-=1
        self.show_message()
        if self.lives==0:
            self.alive=False
        return int(self.points)

    def show_message(self):
        '''
        Shows a randome self.message according to target hit
        '''
        number=random.randint(1,3)
        if self.points==-10:
            if number==1:
                self.message='Ups...'
            elif number==2:
                self.message='Be careful!'
            else:
                self.message='Oh no!'
        else:
            if number==1:
                self.message=' Good Shot! '
            elif number==2:
                self.message='That was awesome!'
            else:
                self.message='You are good at this!'
        return self.message
