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
        self.current= Hilo().card()
        self.total_score = 0
        self.correct = True

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
        self.nextcard=Hilo().card()
        self.hl=input('Higher or lower?(h/l) ')
        if self.current<self.nextcard and self.hl=='h':
            self.correct = True
        elif self.current>self.nextcard and self.hl=='l':
            self.correct = True
        else:
            self.correct = False
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if self.correct:
            self.points+=10
        else:
            self.points-=10


        
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if self.correct:
            print(f'You guessed! The card was {self.current}')
        else:
            print('Try again!')
        print(f'Score: {self.points}')