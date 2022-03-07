from game.scripting.action import Action
from game.scripting.move_actors_action import MoveActorsAction
import constants

class Grow(Action):
    def execute(self, cast, script):
        snake = cast.get_first_actor("snakes")
        player2 = cast.get_first_actor("player2")
        snake.grow_tail(1,constants.GREEN)
        player2.grow_tail(1,constants.BLUE)