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
            random_coordinate = (randint(0, 4), randint(0, 4))
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
            print(
                f"{row_count}  " + " ".join(row),
            )
            row_count += 1
        print("\n")

    def reveal_ships(self):
        """
        method that update ship_location list so that
        remaining ships can be printed
        """
        for ship in self.ship_locations:
            self.board[ship[0]][ship[1]] = "@"

    def reset_board(self):
        """
        resets the board to empty state.
        """
        # reset guesses and locations and board 
        self.board = [["."] * 5 for times in range(5)]
        self.guesses = []
        self.ship_location = []


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
        false_input = "''"

        col = input("select a column [A-E]: ").lower()
        while col not in letters or col in false_input:
            print("\n...a column on the board would be preferable. [A-E]")
            col = input("select a column [A-E]: ").lower()

        row = input("select a row [1-5]: ")
        while row not in numbers or row in false_input:
            print("\n the ships are hiding within row 1-5... try again.")
            row = input("select a row [1-5]: ")

        guess = (int(row) - 1, letters.index(col))
        return guess

    def update_guesses(self, guess):
        """
        append guess to previus guesses memory
        """
        self.guesses.append(guess)

    def miss(self, guess):
        """
        visually update a miss to the board
        """
        self.board[guess[0]][guess[1]] = "0"

    def hit(self, guess):
        """
        visually update a hit to the board
        """
        self.board[guess[0]][guess[1]] = "x"

    def answer(self, question):
        """
        answer is a Player method that
        returns yes or no to a question asked to it.
        """
        if self.type == "human":
            check = input(f"{question} [Y/N]").lower()
            try:
                if check == "y":
                    return True
                elif check == "n":
                    return False
                else:
                    print("Answer 'Y' for Yes and 'N' for no")
                    return self.answer(question)
            except Exception:
                print("Invalid response")
        else:
            print(
                "I am not real, you cant ask me questions, I don't care..."
                )


class ArtificialPlayer(Player):
    """
    Subclass of the Player that represents
    a artificial player. ArtificialPlayer is a player that but
    with a random guess function.
    """

    def __init__(self, name, type):
        super().__init__(name, type)

    def guess(self):
        guess = (randint(0, 4), randint(0, 4))
        return guess


def check_for_hit(player, opponent):
    """
    Function that evaluates a guess made from either player1 or player2.
    """
    guess = player.guess()
    if guess in player.guesses:
        if player.type == "human":
            print("\nyou have already tried that")
        return check_for_hit(player, opponent)

    if guess in opponent.ship_locations:
        opponent.hit(guess)
        player.update_guesses(guess)
        opponent.ship_locations.remove(guess)
        print("\n" * 24)
        if len(opponent.ship_locations) == 0:
            return (
                f"Hit! That was {opponent.name}'s last "
                f"ship. Haha! {opponent.name} is looser! "
                )
        else:
            return (
                f"Hit! LOL @ {opponent.name}. "
                f"Only {len(opponent.ship_locations)} "
                f"more ships to go for {player.name}"
            )
    else:
        if opponent.board[guess[0]][guess[1]] == "x":
            pass
        else:
            opponent.miss(guess)
            player.update_guesses(guess)
            print("\n" * 24)
            return f"\n{player.name} missed..."


def play(player1, player2):
    """
    function that starts the game of battleship be
    tween 2 players.
    """
    # place ships
    player1.place_ships()
    player2.place_ships()

    # visual representation of the ships
    player1.reveal_ships()
    # if you name your player this, the opponents ships will be revealed.
    if player1.name == "developer1337":
        print("\nCH34T 4CTiV4T3D...")
        player2.reveal_ships()

    turns = 1
    input(
        f"\nHey there {player1.name}, let's play the worlds "
        f"slowest coinflip against {player2.name}. \n"
        "Press any key to reveal the boards."
    )
    while turns <= 10:
        # make sure terminal is clear before each round
        print("\n" * 24)
        print(f"{player2.name} playing round number {turns}")
        player1.print_board()
        player2.print_board()

        input(f"{player2.name} will start. Press any key when you are ready ")
        print("\n" * 24)

        # player2 playing the round (computer)
        print(check_for_hit(player2, player1))
        player1.print_board()
        player2.print_board()

        input("You are up next. Press any key to make your guess ")
        print("\n" * 24)
        print(f"{player1.name} playing round number {turns}")
        # player1 playing the round (human)
        player1.print_board()
        player2.print_board()

        print(check_for_hit(player1, player2))
        player1.print_board()
        player2.print_board()
        input("press any key to play the next round")

        if len(player1.ship_locations) == 0:
            player2.reveal_ships()  # add @ to the board based on ship location
            input(
                f"\nYou just lost against"
                f"{player2.name}. Thanks for playing!"
            )
            break
        elif turns == 10:
            print("\n" * 24)
            if len(player1.ship_locations) > len(player2.ship_locations):
                print(f"\nGAME OVER! \n {player1.name} sank the most ships")
                print(
                    f"{player2.name}'s board looked"
                    f"like this. better luck next time."
                )
                player2.reveal_ships()
                player2.print_board()
                break
            elif len(player2.ship_locations) < len(player2.ship_locations):
                print(f"\nGAME OVER! \n {player2.name} sank the most ships")
                player2.reveal_ships()
                print(
                    f"{player2.name}'s board looked like this. "
                    f"better luck next time."
                )
                player2.print_board()
                break
            else:
                input("you guys had equal amount of bad luck.")
                player2.reveal_ships()
                player1.print_board()
                player2.print_board()
        elif len(player2.ship_locations) == 0:
            print("\n" * 24)
            print(
                f"\nYou did it! you wiped the floor"
                f" with {player2.name}. Congratulations!"
            )
            if player1.answer(
                "\nWould you like to forever "
                "append your name to list of lucky people?"
            ):
                feeling = input(
                    "\nCool, but first; "
                    "Tell me how you feel right now: "
                )

                with open("lucky_folks.txt", "a") as luckers_file:
                    luckers_file.write(f"\n{player1.name}, {feeling},")

                with open("lucky_folks.txt") as luckers_file:
                    print(luckers_file.read())
                break
            else:
                print("You do you.")
            break

        turns += 1

    if player1.answer("\nWould you like a rematch?"):
        print("\n" * 24)
        player1.reset_board()
        player2.reset_board()
        play(player1, player2)
    else:
        print("\n" * 24)
        print("Take care.")


def rules():
    """
    Method that prints out the rules to the console.
    """
    with open("rules.txt") as rules_file:
        print(rules_file.read())


def main():
    print("Welcome to **Battle Ships**\n")
    # create instance of players
    player_name = input("Please enter your name: ")
    while player_name == "":
        print("You have an name don't you?")
        player_name = input("Please enter your name: ")

    opponent_name = input("Please name your opponent: ")
    while opponent_name == "":
        print("Your opponent needs a name too!")
        opponent_name = input("Please name your opponent: ")

    player = Player(player_name, "human")
    computer = ArtificialPlayer(opponent_name, "computer")

    if player.answer("\nWould you like to see the rules before you play?"):
        print("\n" * 24)
        rules()

    play(player, computer)


main()
