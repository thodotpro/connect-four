class Board:
    """for the layout we decided to go as simple and easy as possible -  after researching several different options
    we decided to have our program print the layout instead of using pandas for graphic support.

    The dimensions of a standard Connect4 board is 6x7 (6 rows and 7 columns) - in order to label our board
    correctly we will use the letters A-G for the columns and numbers 0-5 for the rows. The visualisation of the
    grid itself, we will achieve by using the symbols '+', '-', and '|'"""

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
        """the function board uses a 'for' loop for the graphical representation of the board - including labels for
        rows and columns"""
        print("\n      A    B    C    D    E    F    G  ", end="") #'end=""' breaks the line
        for hor in range(self.rows):
            print("\n   +----+----+----+----+----+----+----+") #print horizontal line
            print(f"{hor}  |", end="") #printing row labels and vertical line
            for vert in range(self.columns):
                if self.board[hor][vert] == "🔴": #if a token is set - print grid around it (repeat for yellow token)
                    print("", self.board[hor][vert], end=" |")
                elif self.board[hor][vert] == "🟡":
                    print("", self.board[hor][vert], end=" |")
                else:
                    print(" ", self.board[hor][vert], end="  |")
        print("\n   +----+----+----+----+----+----+----+")


if __name__ == "__main__":
    board = Board()
    board.printBoard()