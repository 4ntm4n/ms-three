from random import randint

class BoardMaker:
    def __init__(self, name, type):
        """
        Initializing a playing board
        """
        self.name = name
        self.board = [["."] * 5 for times in range(5)]
        self.type = type
        self.ship_locations = []
        self.guesses = []

    def place_ships(self):
        """
        method that creates a coordinate in tuple format and 
        append it until the self.ship_locations list contains 
        5 unique coordinates
        """
        while len(self.ship_locations) < 4:
            random_coordinate = (randint(0,4), randint(0,4))
            if random_coordinate not in self.ship_locations:
                self.ship_locations.append(random_coordinate)
            

    def print_board(self):
        """
        Method that prints the board to the console.
        """
        print(f"\n{self.name}'s board: \n")
        print("   A B C D E")
        row_count = 1
        for row in self.board:
             print(f"{row_count}  " + " ".join(row),) 
             row_count += 1
        print("\n\n")

    def reveal_ships(self):
        """
        method that update ship_location list so that 
        remaining ships can be printed
        """
        for ship in self.ship_locations:
            self.board[ship[0]][ship[1]] = "@"    

class Player(BoardMaker):
    """
    Subclass of the BoardMaker that represents a human player.
    Player has access to the board made in BoardMaker, a guess method and
    that collects user input and stores old guesses.
    """
    def __init__(self, name, type):
        super().__init__(name, type)
    
    def guess(self):
        """
        Method that collects a human guess, appends it to 
        self.guesses and returns the current guess as a tuple.
        """
        letters = "abcde"
        numbers = "12345"
        false_input = "'''"

        col = input("select a column [A-E]  ").lower()
        while col not in letters or col in false_input:
            print("you need to type a letter from A-E")
            col = input("select a column [A-E]  ").lower()

        row = input("select a row [1-5]  ")
        while row not in numbers or row in false_input:
            print("\ncmon man, you missed the ocean, 1-5 please!")
            row = input("select a row (1-5)  ")

        guess = (int(row) -1, letters.index(col))
        return guess
    
    def update_guesses(self, guess):     
        self.guesses.append(guess)   
    
    def miss(self, guess):
        self.board[guess[0]][guess[1]] = "0"

    def hit(self, guess):
        self.board[guess[0]][guess[1]] = "x"           


class ArtificialPlayer(BoardMaker):
    """
    Subclass of the BoardMaker that represents a artificial player.
    Artificial player has access to the board, makes random guesses and stores
    previous guesses.
    """
    def __init__(self, name, type):
        super().__init__(name, type)

    def guess(self):
        guess = (randint(0,4), randint(0,4))
        return guess

    def update_guesses(self, guess):     
        self.guesses.append(guess)

    def miss(self, guess):
        self.board[guess[0]][guess[1]] = "0"

    def hit(self, guess):
        self.board[guess[0]][guess[1]] = "x"    


def check_for_hit(player, opponent):
    """
    Function that evaluates a guess made from either player1 or player2.
    """
    print(player.guesses)
    guess = player.guess()
    print(guess)
    if guess in player.guesses:
        if player.type == "human":
            print("\n\nyou have already tried that")
        check_for_hit(player, opponent)

    if guess in opponent.ship_locations:
        opponent.hit(guess)
        player.update_guesses(guess)
        opponent.ship_locations.remove(guess)
        print(f"\n\nhit! one of {opponent.name}'s ship has sunk.\nOnly {len(opponent.ship_locations)} more ships to go for {player.name}")
        

    else:
        opponent.miss(guess)
        player.update_guesses(guess)
        print(f"\n\n{player.name} missed... so sad.") 

def play(player1, player2):
    """
    function that starts the game of battleship be
    tween 2 players.
    """

    turns = 10

    while turns > 0:
        player.print_board()
        input(f"{player2.name} is taking it's shot... \n(press any key to continue)")
        check_for_hit(player2, player1)
        player.print_board()

        computer.print_board()
        input("your turn.. lets choose a coordinate in the sea...")
        check_for_hit(player1, player2)
        computer.print_board()
        

        if len(player1.ship_locations) == 0:
            input("\n\nYou just lost the worlds slowest coinflip. Thanks for playing!")
            break
        elif turns == 0:
            if len(player1.ship_locations) > len(player2.ship_locations):
                input(f"\n\nGAME OVER! \n {player2} sank the most ships")
                break
            else:
                input(f"\n\nGAME OVER! \n {player2} sank the most ships")
                break   
        elif len(player2.ship_locations) == 0:
            print("\n\nYou just won the worlds slowest coinflip. congratulations!")
            break
#create instance of players.
player = Player("Anton", "human")
computer = ArtificialPlayer("Computer", "computer")


#place ships on board.
computer.place_ships()
player.place_ships()

#visual representation of the ships
player.reveal_ships()
computer.reveal_ships()
#load gameplay
play(player, computer)


#player_board = BoardMaker("Player", "human")
#computer_board = BoardMaker("Computer", "computer")

#computer_board.print_board()
#player_board.place_ships()
#computer_board.place_ships()
#print(player_board.ship_locations)
