from check_slot import EmptySlot
from input_converter import ConvertCoordinates
from board import Board

class Gravity(Board, ConvertCoordinates, EmptySlot):
    def __init__(self):
        pass

    def gravity_check(self, new_coord):
        """the function checks whether there is an empty space below the coordinate chosen by the user (input)"""
        super().__init__(new_coord)
        space = [None][None]
        space[0] = new_coord[0] + 1 #index 0 refers to the rows, adding one brings us one below the input
        space[1] = new_coord[1]
        if space[0] == 6:
            return True
        if EmptySlot.check_slot_space(space) == False:
            return True
        return False
