import sys
sys.path.insert(0, "/home/tho/Desktop/connect-four/connect-four/Board")
import time


from Board.board import Board
from Board.checkwinner import CheckWinner

class Singleplayer(Board):
    # 5: score += 5
    # 4: score += 4
    # 3: score += 3
    # 2: score += 2
    # 1: score += 1
    best_moves = {5: [(4,3), (3,4), (3,3), (3, 5), (2,2), (2,3), (2,4)],
                  4: [(5,3), (4,2), (4,4), (5,2)],
                  3: [(5,4), (1,3), (1,3), (1,4)],
                  2: [(5,1), (5,5), (4,1), (4,5), (3,1), (3,5), (2,1), (2,5), (1,1), (1,5)],
                  1: [(5,0), (5,6), (4,0), (4,6), (3,0), (3,6), (2,0), (2,6), (1,0), (1,6), (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6)]}
    score = int()
    best_score = int()
    pick = tuple()

    def __init__(self):
        super().__init__()
        self.player1 = "🔴"
        self.player2 = "🟡"
        self.x = -1
        self.y = -1
        self.moves = list()
        self.poss_moves = list()

    def __repr__(self):
        pass

    def moves(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.moves.append((r, c))
        print(self.moves)
        return

    def poss_moves(self):
        self.poss_moves = []  # Clear possible moves list
        for c in range(len(self.board[0])):  # Iterate over columns
            for r in range(len(self.board) - 1, -1, -1):  # Start from the bottom row
                if self.board[r][c] == "":  # If this row is empty
                    self.poss_moves.append((r, c))  # Add the position as a possible move
                    break  # Once found, move to the next column
        print(self.poss_moves)

    def checkThree(self):
        pass

    def checkTwo(self):
        pass

    def evalBoard(self):
        pass

    def score_moves(self):
        scored_moves = []

        # Iterate over possible moves and score them
        for move in self.poss_moves:
            x, y = move
            move_score = 0

            # Check if the move is in any of the predefined score groups in `best_moves`
            for score, moves in Singleplayer.best_moves.items():
                if (x, y) in moves:
                    move_score = score  # Assign the score based on the predefined list
                    scored_moves.append((move, move_score))  # Store the move and its score
                    break  # Stop once a score is found for the move

        return scored_moves


    def pick_best_move(self):
        # winning move +50
        # opponnent winning move -50
        # block opponent winning move +60
        # block opponent three +30
        # opponent three -30
        # have three +35
        # have two +20
        # opponent two -10
        # block opponent two +10
        # else best move scores
        # Get the list of valid moves with their scores
        scored_moves = self.score_moves()

        # If no valid moves are found (i.e., the board is full), return None
        if not scored_moves:
            print("No valid moves available.")
            return None

        # Find the move with the highest score
        best_move = max(scored_moves, key=lambda x: x[1])[0]  # x[0] is the move, x[1] is the score

        print(f"Best move selected: {best_move}")
        return best_move

    def valid(self, pick: tuple):
        for r in range(self.rows):
            # returns if selected square is already taken
            if self.board[self.x][self.y] != "":
                print("This square is already taken. Please select another one.")
                return False

            # returns if the square, below selected, is empty
            if self.board[self.x] == self.board[4] and self.board[5] == "":
                print("The square below is empty. Please select another one.")
                return False
            elif self.board[self.x] == self.board[3] and self.board[4] == "":
                print("The square below is empty. Please select another one.")
                return False
            elif self.board[self.x] == self.board[3] and self.board[2] == "":
                print("The square below is empty. Please select another one.")
                return False
            elif self.board[self.x] == self.board[2] and self.board[1] == "":
                print("The square below is empty. Please select another one.")
                return False
            elif self.board[self.x] == self.board[1] and self.board[0]== "":
                print("The square below is empty. Please select another one.")
                return False

    # AI's pick function would now call `pick_best_move` to make the selection:
    def pick(self):
        global pick
        # If it's Player 1's turn, take input from the user (you can keep this as-is)
        if self.turn % 2 == 1:
            pick = input("Select square for placement (e.g.: a5 | q for quit): ").upper()
            for x in range(len(self.letters)):
                if self.letters[x] == pick[0]:
                    self.y = int(x)
            self.x = int(pick[1])
            pick = (self.x, self.y)
            return self.x, self.y

        # If it's Player 2's (AI's) turn, use the best possible move
        elif self.turn % 2 == 0:
            best_move = self.pick_best_move()
            if best_move:
                self.x, self.y = best_move
                return self.x, self.y
            else:
                # No valid move found, return a default (this case should rarely happen)
                return None, None

    def place_pick(self):
        # Check if the selected position is valid
        if self.turn % 2 == 1:  # Player 1's turn
            # Check if the move is in the possible moves
            if (self.x, self.y) in self.poss_moves:
                self.token = "🔴"
                # Place player1's emoji at the position
                self.board[self.x][self.y] = self.player1
            else:
                print("Invalid move. Please select another one.")

        elif self.turn % 2 == 0:  # Player 2's turn (AI)
            # Check if the move is in the possible moves
            if (self.x, self.y) in self.poss_moves:
                self.token = "🟡"
                # Place player2's emoji at the position
                self.board[self.x][self.y] = self.player2
            else:
                print("Invalid move. Please select another one.")

    def nextMove(self):
        pass

    def updateBoard(self):
        pass

    def nextRound(self):
        pass

    def main(self):
        # Initialize the game and start the loop
        board = Singleplayer()
        check_win = CheckWinner()
        while board.turn <= 42:
            time.sleep(1)
            board.print_board()
            Singleplayer.moves(board)
            Singleplayer.poss_moves(board)  # Get possible moves
            board.pick()  # Player or AI makes a move
            board.valid(pick)  # Validate the move
            board.place_pick()  # Place the move on the board
            board.print_board()  # Display the board
            # Check if there's a winner after the move is made
            if check_win.win_assessment(board.token):
                print(f"Player {board.turn % 2 + 1} wins!")
                break  # Exit the game if there is a winner
            if board.turn == 42:
                print("It's a tie!")
                break  # Exit if all spots are filled and there's no winner

            board.next_turn()  # Increment turn

            # Init board
            # while Game
                # print board
                # moves
                # poss moves
                # pick
                # place
                # check win
                # turn +1



if __name__ == "__main__":
    Singleplayer.main(Singleplayer)
