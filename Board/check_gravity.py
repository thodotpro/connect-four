from check_slot import EmptySlot
from input_converter import ConvertCoordinates
from board import Board

class Gravity(Board, ConvertCoordinates, EmptySlot):
    def __init__(self):
        pass

    def gravity_check(self, new_coord):
        """the function checks whether there is an empty space below the intended coordinate chosen by the user"""
        super().__init__(new_coord)
        space = [None][None]
        space[0] = new_coord[0]