# list that holds the character that represents the board in the terminal
board = [["."] * 5 for times in range(0,5)]


def print_board(board):
    row_count = 1
    print("   A B C D E")
    for row in board:
        print(f"{row_count}  " +" ".join(row))
        row_count += 1


print_board(board)
