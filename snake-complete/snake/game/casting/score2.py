from turtle import pos
from game.casting.score import Score
from game.shared.point import Point
from game.casting.actor import Actor

class Score2(Score):
    def __init__(self):
        super().__init__()
        position=Point(400, 15)
        self.set_position(position)

    def set_position(self, position):
        
        Actor().set_position(position)

    def add_points(self, points):
        return super().add_points(points)