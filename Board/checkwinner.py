from Board.board import Board

class CheckWinner(Board):
    """In order to establish a winner, we need to check the rows for previously placed token. The game Connect 4
    is won, if 4 token are placed next to each other, either in a row, column, or diagonally.
    We will use a method which takes the parameter 'token' and implements four 'for' loops to check whether
    there are 3 adjacent tokens to the last one placed."""

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])

    def win_assessment(self, token):
        # Check for horizontal win
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == token and self.board[row][col + 1] == token and self.board[row][col + 2] == token and self.board[row][col + 3] == token:
                    print(f"\n{token} WINS!")
                    return True
        return False

    def win_assessment_vertical(self, token):
        # Check for vertical win
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == token and self.board[row + 1][col] == token and self.board[row + 2][col] == token and self.board[row + 3][col] == token:
                    print(f"\n{token} WINS!")
                    return True
        return False

    def win_assessment_diagonal_lr(self, token):
        # Check for diagonal win
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == token and self.board[row + 1][col + 1] == token and self.board[row + 2][col + 2] == token and self.board[row + 3][col + 3] == token:
                    print(f"\n{token} WINS!")
                    return True
        return False


    def win_assessment_diagonal_rl(self, token):
        # Check for counter diagonal win
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == token and self.board[row - 1][col + 1] == token and self.board[row - 2][col + 2] == token and self.board[row - 3][col + 3] == token:
                    print(f"\n{token} WINS!")
                    return True
        return False

    def check_win(self, token):
        # Check for win
        if (self.win_assessment(token) or
                self.win_assessment_vertical(token) or
                self.win_assessment_diagonal_lr(token) or
                self.win_assessment_diagonal_rl(token)):
            return True
        return False

    if __name__ == '__main__':
        pass
