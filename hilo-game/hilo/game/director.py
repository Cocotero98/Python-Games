from game.hil import Hilo


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.points = 300
        self.cards=[]
        self.is_playing = True
        self.current= self.card()
        self.total_score = 0

        for i in range(1,14):
            self.cards.append(i)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.print_current_card()
            self.guess()
            self.next_card()
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def print_current_card(self):
        print(f'The card is:{self.current}')


    def get_inputs(self):
        """Ask the user if they want to play.

        Args:
            self (Director): An instance of Director.
        """
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")
        
    
    def next_card(self):
        self.current=self.nextcard
        print(f'Next card was: {self.nextcard}')

    
    def guess(self):
        self.nextcard=self.card()
        self.hl=input('Higher or lower?(h/l) ')
        if self.current<self.nextcard and self.hl=='h':
            correct='addpoints'
        elif self.current>self.nextcard and self.hl=='l':
            correct='addpoints'
        else:
            incorrect='menos'
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """


        


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)