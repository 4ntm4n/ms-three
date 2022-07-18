from random import randint

def ship_location():
    return [[" "] * 5 for x in range(5)]

hidden_board = ship_location()
guessing_board = ship_location()


def print_board(board): 
    print ("    A B C D E")
    print("   -----------")
    row_number = 1
    for row in board:
        print("{}  |{}|".format(row_number,"|".join(row)))
        row_number += 1


print_board(hidden_board)

def get_ship_location():
    pass

def count_hits():
    pass

def create_ships():
    pass

    turns = 10
    #while turns > 0: