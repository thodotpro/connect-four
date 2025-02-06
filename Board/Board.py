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

    def welcome(self):
        print("CONNECT FOUR")
        print("---------------------------")

    def printBoard(self):
        print("\n     A    B    C    D    E    F    G  ", end="")
        for r in range(self.rows):
            print("\n   +----+----+----+----+----+----+----+", end="")
            print(r, " |", end="")


if __name__ == "__main__":
    board = Board()
    board.printBoard()