from Board.board import Board
import random

board = Board()
# print(len(board.board))
# # board.printBoard()
# moves = []
#
# for r in range(len(board.board)):
#     for c in range(len(board.board[r])):
#         moves.append((r, c))
#
# print(moves)

pick = ()

best_moves = {5: [(4,3), (3,4), (3,3), (3, 5), (2,2), (2,3), (2,4)],
                  4: [(5,3), (4,2), (4,4), (5,2)],
                  3: [(5,4), (1,3), (1,3), (1,4)],
                  2: [(5,1), (5,5), (4,1), (4,5), (3,1), (3,5), (2,1), (2,5), (1,1), (1,5)],
                  1: [(5,0), (5,6), (4,0), (4,6), (3,0), (3,6), (2,0), (2,6), (1,0), (1,6), (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6)]}

for k, v in best_moves.items():
    best_move = random.choice(best_moves[4]) or random.choice(best_moves[4]) or random.choice(best_moves[3]) or random.choice(best_moves[2]) or random.choice(best_moves[1])
    pick = best_move
print(pick)

