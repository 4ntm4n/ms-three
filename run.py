# list that holds the character that represents the board in the terminal
from random import randint

class BoardMaker:
    def __init__(self, owner, type):
        """
        Initializing a playing board
        """
        self.owner = owner
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
        while len(self.ship_locations) < 5:
            random_coordinate = (randint(0,4), randint(0,4))
            if random_coordinate not in self.ship_locations:
                self.ship_locations.append(random_coordinate)
            

    def print_board(self):
        """
        Method that prints the board to the console.
        """
        print(f"{self.owner}'s board: \n")
        print("   A B C D E")
        row_count = 1
        for row in self.board:
             print(f"{row_count}  " + " ".join(row))
             row_count += 1






player_board = BoardMaker("Player", "human")
computer_board = BoardMaker("Computer", "computer")

computer_board.print_board()
player_board.place_ships()
computer_board.place_ships()
print(player_board.ship_locations)
