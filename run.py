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
        numbers = "12345"
        letters = "abcde"

        row = input("select a row (1-5)")
        while row not in numbers:
            print("cmon man, you missed the ocean, 1-5 please!")
            row = input("select a row (1-5)")

        col = input("select a column (A-E)").lower()
        while col not in letters:
            print("cmon man, you missed the ocean, A-E please!")
            col = input("select a column (A-E)").lower()
        
        guess = (int(row), letters.index(col))
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

    def update_guesses(self):     
        self.guesses.append(self.guess)

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
        print("you have already tried that")
        check_for_hit(player, opponent)

    if guess in opponent.ship_locations:
        opponent.hit(guess)
        player.update_guesses(guess)
        print(f"hit! one of {opponent.name}'s ship has sunk.")
        opponent.ship_locations.remove(guess)

    else:
        opponent.miss(guess)
        player.update_guesses(guess)
        print("miss...") 

def play(player1, player2):
    """
    function that starts the game of battleship between 2 players.
    """
    player.print_board()
    computer.print_board()
    check_for_hit(player1, player2)


#create instance of players.
player = Player("Anton", "human")
computer = ArtificialPlayer("Computer", "computer")


#place ships on board.
computer.place_ships()
player.place_ships()

#visual representation of the ships
player.reveal_ships()
#load gameplay
play(player, computer)


#player_board = BoardMaker("Player", "human")
#computer_board = BoardMaker("Computer", "computer")

#computer_board.print_board()
#player_board.place_ships()
#computer_board.place_ships()
#print(player_board.ship_locations)
