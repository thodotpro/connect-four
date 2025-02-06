class Board:


    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""]]

    def printBoard(self):
        pass


if __name__ == "__main__":
    board = Board()
    board.printBoard()