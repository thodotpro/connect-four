from board import Board
from input_converter import ConvertCoordinates
from check_slot import EmptySlot
from check_gravity import Gravity
from check_winner import CheckWinner
class Multiplayer:
    def __init__(self):
        pass

    def adapt_board(self, coord, turn):
        self.coord = coord
        self.turn = turn
        Board.printBoard([self.coord[0]][self.coord[1]]) = turn

    counter = 0
    while True:
        if counter % 2 == 0:
            Board.printBoard()
            while True:
                place_token = input("\nPLAYER 1 - choose where to place your token: ")
                coord = ConvertCoordinates.input_converter(place_token)
                try:
                    if EmptySlot.check_slot_space(coord) and Gravity.gravity_check(coord) == True:
                        adapt_board(coord, "🔴")
                        break
                    else:
                        print("Invalid Coordinate!")
                except:
                print("ERROR - Please try again.")
            winner = CheckWinner.win_assessment("🔴")
            counter += 1
        else:
            while True:
                place_token = input("\nPLAYER 2 - choose where to place your token: ")
                coord = ConvertCoordinates.input_converter(place_token)
                try:
                    if EmptySlot.check_slot_space(coord) and Gravity.gravity_check(coord) == True:
                        adapt_board(coord, "🟡")
                        break
                    else:
                        print("Invalid Coordinate!")
                except:
                print("ERROR - Please try again.")
            winner = CheckWinner.win_assessment("🟡")
            counter += 1

        if winner == True:
            Board.printBoard()
            break

