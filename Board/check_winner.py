from board import Board
class CheckWinner(Board):
    def __init__(self):
        """In order to establish a winner, we need to check the rows for previously placed token. The game Connect 4
        is won, if 4 token are placed next to each other, either in a row, column or diagonally - thus, we need
        to check all four (diagonally top right to bottom left and top left to bottom right) possible connections.

        We will use a method, which takes the parameter 'token' and implement four 'for' loops to check whether there
        are 3 adjacent tokens to the last one placed."""
        pass

    #horizontal
    def win_assessment(self, token):
        self.token = token
        for vert in range(Board.rows):
            for hor in range(Board.columns - 3):
                if Board.printBoard[hor][vert] == self.token and Board.printBoard[hor + 1][vert] == self.token and Board.printBoard[hor + 2 ][vert] == self.token and Board.printBoard[hor + 3][vert] == self.token:
                    print(f"\n{token}WINS!")
                    return True
    #vertical
        for vert in range(Board.rows):
            for hor in range(Board.columns - 3):
                if Board.printBoard[hor][vert] == self.token and Board.printBoard[hor][vert + 1] == self.token and Board.printBoard[hor][vert + 2] == self.token and Board.printBoard[hor][vert + 3] == self.token:
                    print(f"\n{token}WINS!")
                    return True
    #diagonal (top right - bottom left)
        for vert in range(Board.rows - 3):
            for hor in range(3, Board.columns):
                if Board.printBoard[hor][vert] == self.token and Board.printBoard[hor + 1][vert - 1] == self.token and Board.printBoard[hor + 2 ][vert - 2] == self.token and Board.printBoard[hor + 3][vert - 3] == self.token:
                    print(f"\n{token}WINS!")
                    return True
    #diagonal (top left - bottom right)
        for vert in range(Board.rows -  3):
            for hor in range(Board.columns - 3):
                if Board.printBoard[hor][vert] == self.token and Board.printBoard[hor + 1][vert + 1] == self.token and Board.printBoard[hor + 2 ][vert + 2] == self.token and Board.printBoard[hor + 3][vert + 3] == self.token:
                    print(f"\n{token}WINS!")
                    return True
        return False