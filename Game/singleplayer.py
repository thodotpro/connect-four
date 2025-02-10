import time
import random
from Board.board import Board
from Board.checkwinner import CheckWinner

class Singleplayer(Board):
    '''
    In singleplayer mode the user can play connect 4 against a computer. The computer picks a move based on the best available move.
    The computer should favor winning before blocking the opponent.
    '''
    def __init__(self):
        super().__init__()
        self.player1 = "🔴"
        self.player2 = "🟡"
        self.x = -1
        self.y = -1
        self.all_moves = list()
        self.all_poss_moves = list()
        self.best_moves = {
            5: [(4, 3), (3, 4), (3, 3), (3, 5), (2, 2), (2, 3), (2, 4)],
            4: [(5, 3), (4, 2), (4, 4), (5, 2)],
            3: [(5, 4), (1, 3), (1, 3), (1, 4)],
            2: [(5, 1), (5, 5), (4, 1), (4, 5), (3, 1), (3, 5), (2, 1), (2, 5), (1, 1), (1, 5)],
            1: [(5, 0), (5, 6), (4, 0), (4, 6), (3, 0), (3, 6), (2, 0), (2, 6), (1, 0), (1, 6),
                (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]}
        self.score = int()
        self.best_score = int()
        self.best_move = tuple()
        self.pick = tuple()
        self.turn = 1

    def moves(self):
        # Appends all moves as tuple into a list
        self.all_moves = [(r, c) for r in range(len(self.board)) for c in range(len(self.board[r]))]
        return self.all_moves

    def poss_moves(self):
        # Appends all possible moves as tuple into a list
        self.all_poss_moves = []
        for c in range(len(self.board[0])):
            for r in range(len(self.board) - 1, -1, -1):
                if self.board[r][c] == "":
                    self.all_poss_moves.append((r, c))
                    break
        return self.all_poss_moves

    def score_moves(self):
        scored_moves = []
        for move in self.all_poss_moves:
            x, y = move
            move_score = 0
            for score, moves in self.best_moves.items():
                if (x, y) in moves:
                    move_score = score
                    scored_moves.append((move, move_score))
                    break
        return scored_moves

    def pick_best_move(self):
        scored_moves = self.score_moves()
        if not scored_moves:
            self.best_move = random.choice(self.all_poss_moves)
            return self.best_move
        self.best_move = max(scored_moves, key=lambda x: x[1])[0]
        return self.best_move

    def valid(self, pick: tuple):
        x, y = pick
        if self.board[x][y] != "":
            return False
        return True

    def pick_square(self):
        # Player 1's move (human)
        if self.turn % 2 == 1:
            print(f"Player 1's (🔴) turn!")
            self.pick = input("Select square for placement (e.g., a5 | q for quit): ").upper()

            if self.pick == "Q":    # quit
                print("Quitting...")
                time.sleep(2)
                quit()

            for x in range(len(self.letters)):
                if self.letters[x] == self.pick[0]:
                    self.y = int(x)
                    break
            else:
                print("Invalid input.")
                return self.pick_square()  # Prompt again if invalid

            if not self.pick[1:].isdigit() or int(self.pick[1]) < 0 or int(self.pick[1]) >= len(self.board):
                print("Invalid input.")
                return self.pick_square()  # Prompt again if invalid row

            self.x = int(self.pick[1])  # Row position

            # Ensure the move is within the board boundaries
            if (self.x, self.y) not in self.poss_moves():
                print("Invalid move.")
                return self.pick_square()  # Prompt again if invalid move

            return self.x, self.y

        # AI's move (Player 2)
        elif self.turn % 2 == 0:
            print("AI's turn (🟡)!")
            self.best_move = self.pick_best_move()
            self.x, self.y = self.best_move
            return self.x, self.y

    def place_pick(self):
        if self.turn % 2 == 1:  # Player 1's turn
            if (self.x, self.y) in self.poss_moves():
                self.token = "🔴"
                self.board[self.x][self.y] = self.player1
            else:
                print("Invalid move.")
        elif self.turn % 2 == 0:
            if (self.x, self.y) in self.poss_moves():
                self.token = "🟡"
                self.board[self.x][self.y] = self.player2
            else:
                print("Invalid move.")

    def score_board(self):
        scored_moves = []

        for move in self.all_poss_moves:
            x, y = move
            move_score = 0

            # Evaluate the score for each direction (horizontal, vertical, diagonal)
            move_score += self.check_direction(x, y, 0, 1)  # Horizontal (right)
            move_score += self.check_direction(x, y, 1, 0)  # Vertical (down)
            move_score += self.check_direction(x, y, 1, 1)  # Diagonal (bottom-right)
            move_score += self.check_direction(x, y, 1, -1)  # Diagonal (bottom-left)

            scored_moves.append((move, move_score))

        return scored_moves

    def check_direction(self, x, y, dx, dy):
        """Check for consecutive tokens in one direction (horizontal, vertical, or diagonal)."""
        player = self.board[x][y]
        count = 1  # Include the current piece

        # Check in the positive direction (dx, dy)
        for i in range(1, 4):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and self.board[nx][ny] == player:
                count += 1
            else:
                break

        # Check in the negative direction (-dx, -dy)
        for i in range(1, 4):
            nx, ny = x - dx * i, y - dy * i
            if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and self.board[nx][ny] == player:
                count += 1
            else:
                break

        # Assign score based on count of consecutive tokens
        if count == 4:
            return 1000  # Win
        elif count == 3:
            return 500  # Potential win
        elif count == 2:
            return 100  # Good potential
        return 0  # No significant potential




    def check_for_two(self):
        # block opponent: +10
        # get two: +15
        pass

    def check_for_three(self):
        # block opponent: +25
        # get three: +30
        pass

    def check_for_four(self):
        # block opponent: +80
        # get four: +100
        pass

    def main():
        board = Singleplayer()

        check_winner = CheckWinner(board.board)

        while board.turn <= 42:
            time.sleep(1)
            board.print_board()
            board.moves()
            board.poss_moves()
            print(f"Turn {board.turn}:")
            board.pick_square()  # This will now properly ask for input or select AI's move.
            board.place_pick()

            if check_winner.check_win(board.token):
                board.print_board()
                break

            if board.turn == 42:
                print("DRAW!")
                board.print_board()
                break
            time.sleep(1)
            board.turn += 1  # Increment turn


if __name__ == "__main__":
    Singleplayer.main()
