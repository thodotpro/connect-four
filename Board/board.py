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
                      ["🔴", "", "", "", "", "", ""],
                      ["🟡", "🔴", "", "", "", "", ""]]
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.player1 = "🔴"
        self.player2 = "🟡"
        self.turn = 1
        self.token = self.player1

    def print_board(self):
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



    def next_turn(self):
        # odd turn: token changes to player 2, turn adds 1
        if self.turn % 2 == 1:
            self.turn += 1
            self.token = self.player2
        # even turn: token changes to player 1, turn adds 1
        elif self.turn % 2 == 0:
            self.turn += 1
            self.token = self.player1


if __name__ == "__main__":
    board = Board()
    board.print_board()