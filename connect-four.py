from Game.singleplayer import Singleplayer

rows = 6
columns = 7
board = [["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""]]

def print_board():
    """for the layout we decided to go as simple and easy as possible -  after researching several different options
    we decided to have our program print the layout instead of using pandas for graphic support.

    The dimensions of a standard Connect4 board is 6x7 (6 rows and 7 columns) - in order to label our board
    correctly we will use the letters A-G for the columns and numbers 0-5 for the rows. The visualisation of the
    grid itself, we will achieve by using the symbols '+', '-', and '|'

    the function board uses a 'for' loop for the graphical representation of the board - including labels for
    rows and columns"""

    print("\n      A    B    C    D    E    F    G  ", end="") #'end=""' breaks the line
    for hor in range(rows):
        print("\n   +----+----+----+----+----+----+----+") #print horizontal line
        print(f"{hor}  |", end="") #printing row labels and vertical line
        for vert in range(columns):
            if board[hor][vert] == "🔴": #if a token is set - print grid around it (repeat for yellow token)
                print("", board[hor][vert], end=" |")
            elif board[hor][vert] == "🟡":
                print("", board[hor][vert], end=" |")
            else:
                print(" ", board[hor][vert], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

#################################################################################################################################

def input_converter(inp:str):
    """this function allows us to convert the player input (strint) to the allocated index-based coordinates of our game board
    e.g. input 'A0' will be converted to the coordinate (0|0)"""
    inp = inp
    coord = [None, None]
    if inp[0] == "A":
        coord[1] = 0
    elif inp[0] == "B":
        coord[1] = 1
    elif inp[0] == "C":
        coord[1] = 2
    elif inp[0] == "D":
        coord[1] = 3
    elif inp[0] == "E":
        coord[1] = 4
    elif inp[0] == "F":
        coord[1] = 5
    elif inp[0] == "G":
        coord[1] = 6
    else:
        print("Invalid Choice!")
    coord[0] = int(inp[1]) #as the second part of the input will be a nuber in string format we just need to make this an integer
    return coord

#################################################################################################################################

def check_slot_space(new_coord):
    """function checks if the user input does not equal to a spot where a token has already been placed"""
    if board[new_coord[0]][new_coord[1]] == "🔴":
        return False
    elif board[new_coord[0]][new_coord[1]] == "🟡":
        return False
    else:
        return True

#################################################################################################################################

def gravity_check(new_coord):
    """the function checks whether there is an empty space below the coordinate chosen by the user (input)"""
    space = [None, None]
    space[0] = new_coord[0] + 1 #index 0 refers to the rows, adding one brings us one below the input
    space[1] = new_coord[1]
    if space[0] == 6:
        return True
    if not check_slot_space(space):
        return True
    return False

#################################################################################################################################


def win_assessment(token):
    """In order to establish a winner, we need to check the rows for previously placed token. The game Connect 4
    is won, if 4 token are placed next to each other, either in a row, column or diagonally - thus, we need
    to check all four (diagonally top right to bottom left and top left to bottom right) possible connections.

    We will use a method, which takes the parameter 'token' and implement four 'for' loops to check whether there
    are 3 adjacent tokens to the last one placed."""

    # Horizontal
    for y in range(rows):
        for x in range(columns - 3):
            if (board[y][x] == token and board[y][x + 1] == token and
                    board[y][x + 2] == token and board[y][x + 3] == token):
                print(f"\n{token} WINS!")
                return True

    # Vertical
    for y in range(rows - 3):
        for x in range(columns):
            if (board[y][x] == token and board[y + 1][x] == token and
                    board[y + 2][x] == token and board[y + 3][x] == token):
                print(f"\n{token} WINS!")
                return True

    # Diagonal (bottom-left to top-right)
    for y in range(rows - 3):
        for x in range(columns - 3):
            if (board[y][x] == token and board[y + 1][x + 1] == token and
                    board[y + 2][x + 2] == token and board[y + 3][x + 3] == token):
                print(f"\n{token} WINS!")
                return True

    # Diagonal (top-left to bottom-right)
    for y in range(3, rows):
        for x in range(columns - 3):
            if (board[y][x] == token and board[y - 1][x + 1] == token and
                    board[y - 2][x + 2] == token and board[y - 3][x + 3] == token):
                print(f"\n{token} WINS!")
                return True

    return False


#################################################################################################################################

def adapt_board(coord, turn):
    """this function will update our game board after every turn"""
    turn = turn
    board[coord[0]][coord[1]] = turn

#################################################################################################################################

def multiplayer():
    """the multiplayer function will be called when user requests the multiplayer mode via the console
    it allows two players to play against each other on one"""
    counter = 0
    while True:
        if counter % 2 == 0:
            print_board()
            while True:
                place_token = input("\nPLAYER 1 - choose where to place your token: ")
                coord = input_converter(place_token)
                if check_slot_space(coord) and gravity_check(coord) == True:
                    adapt_board(coord, "🔴")
                    break
                else:
                    print("Invalid Coordinate!")
            winner = win_assessment("🔴")
            if winner == True:
                break
            else:
                counter += 1
        else:
            while True:
                print_board()
                place_token = input("\nPLAYER 2 - choose where to place your token: ")
                coord = input_converter(place_token)
                if check_slot_space(coord) and gravity_check(coord) == True:
                    adapt_board(coord, "🟡")
                    break
                else:
                    print("Invalid Coordinate!")
            winner = win_assessment("🟡")
            if winner == True:
                break
            else:
                counter += 1


if __name__ == "__main__":
    print("Welcome to Connect4!")
    print("***************************************************************************************")
    print("Please choose between Single- and Multiplayer Mode, by typing S or M in the console: ")

    if input().upper() == "M":
        multiplayer()
    elif input().upper() == "S":
        Singleplayer.main()
    else:
        print("Invalid Input, please enter 'S' for Single- or 'M' for Multiplayer Mode: ")
    # print_board()
