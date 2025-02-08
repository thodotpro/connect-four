from input_converter import ConvertCoordinates
from board import Board

class EmptySlot(Board, ConvertCoordinates):
    def __init__(self):
        pass

    def check_slot_space(self, new_coord):
        """function checks if the user input does not equal to a spot where a token has already been placed"""
        self.new_coord = new_coord
        if self.board[self.new_coord[0]][self.new_coord[1]] == "🔴":
            return False
        elif 