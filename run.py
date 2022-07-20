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

    def create_cordinate()
        pass

    def place_ships(self, cordinate:
        pass

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