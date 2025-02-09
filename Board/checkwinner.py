from Board.board import Board
class CheckWinner(Board):
    """In order to establish a winner, we need to check the rows for previously placed token. The game Connect 4
    is won, if 4 token are placed next to each other, either in a row, column or diagonally - thus, we need
    to check all four (diagonally top right to bottom left and top left to bottom right) possible connections.

    We will use a method, which takes the parameter 'token' and implement four 'for' loops to check whether there
    are 3 adjacent tokens to the last one placed."""
    def __init__(self):
        super().__init__()


    #horizontal
    class CheckWinner(Board):
        def __init__(self):
            super().__init__()

        def win_assessment(self, token):
            self.token = token
            # Horizontal Check: Ensure we don't go out of bounds (stop at self.columns - 4)
            for vert in range(self.rows):
                for hor in range(self.columns - 3):  # Ensure hor + 3 stays within bounds
                    if self.board[vert][hor] == self.token and self.board[vert][hor + 1] == self.token and \
                            self.board[vert][hor + 2] == self.token and self.board[vert][hor + 3] == self.token:
                        print(f"\n{token} WINS!")
                        return True

            # Vertical Check: Ensure we don't go out of bounds (stop at self.rows - 4)
            for vert in range(self.rows - 3):  # Ensure vert + 3 stays within bounds
                for hor in range(self.columns):
                    if self.board[vert][hor] == self.token and self.board[vert + 1][hor] == self.token and \
                            self.board[vert + 2][hor] == self.token and self.board[vert + 3][hor] == self.token:
                        print(f"\n{token} WINS!")
                        return True

            # Diagonal (Top-Right to Bottom-Left) Check
            for vert in range(self.rows - 3):  # Ensure vert + 3 stays within bounds
                for hor in range(3, self.columns):  # Ensure hor - 3 stays within bounds
                    if self.board[vert][hor] == self.token and self.board[vert + 1][hor - 1] == self.token and \
                            self.board[vert + 2][hor - 2] == self.token and self.board[vert + 3][hor - 3] == self.token:
                        print(f"\n{token} WINS!")
                        return True

            # Diagonal (Top-Left to Bottom-Right) Check
            for vert in range(self.rows - 3):  # Ensure vert + 3 stays within bounds
                for hor in range(self.columns - 3):  # Ensure hor + 3 stays within bounds
                    if self.board[vert][hor] == self.token and self.board[vert + 1][hor + 1] == self.token and \
                            self.board[vert + 2][hor + 2] == self.token and self.board[vert + 3][hor + 3] == self.token:
                        print(f"\n{token} WINS!")
                        return True

            return False
