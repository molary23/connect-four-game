import sys

from controller.ConnectController import ConnectController

if __name__ == '__main__':
    restart = True
    while restart:
        ConnectController.main(sys.argv)
        play_again = input("Would you like to play again (Y/N)? ")
        if play_again.lower() != "y":
            restart = False
