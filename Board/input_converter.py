class ConvertCoordinates:
    def __init__(self, inp:str):
        self.inp = inp
        pass

    def input_converter(self, inp:str):
        """this function allows us to convert the player input (strint) to the allocated index-based coordinates of our game board
        e.g. input 'A0' will be converted to the coordinate (0|0)"""
        coord = [None][None]
        if inp[0] == "A":
            coord[1] = 0
        elif inp[0] == "B":
            coord[1] = 1
        elif inp[0] == "C":
            coord[1] = 2
        elif inp[0] == "D":
            coord[1] = 3
        elif inp[0] == "E":
            coord[1] = 4
        elif inp[0] == "F":
            coord[1] = 5
        elif inp[0] == "G":
            coord[1] = 6
        else:
            print("Invalid Choice!")
        coord[0] = int(inp[1]) #as the second part of the input will be a nuber in string format we just need to make this an integer
        return coord