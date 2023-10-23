import sys


class ConnectView:
    def __init__(self):
        pass

    def show_board(self, board):
        print("1\t2\t3\t4\t5\t6\t7")
        for row in board:
            for square in row:
                print("{}\t".format("⚪" if square == 0 else square), end="")
            print("")

    def show_menu(self):
        while True:
            try:
                print("Which column would you like to place a token in (1-7)?")
                inp = sys.stdin.readline().strip()
                out = int(inp)
                out -= 1
                return out
            except ValueError:
                print("Invalid input! Please enter a number")
            except Exception:
                print("Unable to read input")
                return -1

    def show_turn(self, player):
        if player == "🟡":
            who = 1
        else:
            who = 2
        print("It is player {}'s turn!".format(who))

    def show_end_game(self, winner):
        if winner == 0:
            print("The game is a draw!")
        elif winner == "🟡":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    def show_error(self, error):
        print("Error: {}".format(error))
