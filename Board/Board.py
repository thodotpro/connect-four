class Board:


    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]

    def printBoard(self):
        for rows in range(self.rows):
            for columns in range(self.columns):
                print(self.board[rows][columns], "x")

if __name__ == "__main__":
    board = Board()
    board.printBoard()