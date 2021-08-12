from player import HumanPlayer, RandomComputerPlayer
from game import TicTacToe, play


def hvc():
    is_correct = False
    while not is_correct:
        play_letter = input("Enter the letter of player. 'X' or 'O': ").upper()
        if play_letter == 'X':
            x_player = HumanPlayer('X')
            o_player = RandomComputerPlayer('O')
        elif play_letter == 'O':
            o_player = HumanPlayer('O')
            x_player = RandomComputerPlayer('X')
        else:
            print("Enter a valid input.")

