import imp
import random
from game.director import Director

# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Hilo:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Hilo with a value and points attribute.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value=0
        self.points=0

    def guess(self):
        """Creates a variable holding the guess of the player.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.hl=input('Higher or lower? ')
        if self.value<self.card:
            correct='l'

# 3) Create the roll(self) method. Use the following method comment.
    def card(self):
        """Generates a new random card
        
        Args:
            self (Die): An instance of Die.
        """
        self.value=random.randrange(1,14)

