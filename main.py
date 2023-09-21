import random

def print_layout():
    print("  0  |  1  |  2  \n-----+-----+-----\n  3  |  4  |  5  \n-----+-----+-----\n  6  |  7  |  8  ")


def print_board():
    print()
    print(f"{board[0]}\t\t0  |  1  |  2")
    print(f"{board[1]}\t\t3  |  4  |  5")
    print(f"{board[2]}\t\t6  |  7  |  8")
    print()


def print_intro():
    print("\nLet's play tic-tac-toe! You're X's\n")
    print("The spots on the board are numbered like this:")
    print_layout()
    print("Make moves by typing in the number of the spot you wish to mark\n")


def convert(index):
    # may have to typecast index as an int
    row = int(index) // 3
    col = int(index) % 3

    return row, col


def human_turn(board):
    valid_move = False
    move = input("What's your move?\n")

    while valid_move == False:
        try:
            if (int(move) < 0) or (int(move) > 8):
                move = input("Out of bounds, try again\n")
            else:
                row, col = convert(move)

                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    valid_move = True
                else:
                    move = input("That spot's taken, try again\n")
        except:
            move = input("Invalid move, try again\n")


def robot_turn(board):
    # make a list of available spot numbers
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                available_moves.append(row*3 + col)

    # pick a number between 0 and the length of the list
    print(f"available moves for robot: {available_moves}")
    number_of_choices = len(available_moves)
    move = random.randint(0,number_of_choices-1)

    # make a move on the i'th index of the list
    location = available_moves[move]
    print(f"move selected: {location}")
    row, col = convert(location)
    board[row][col] = 'O'


def winner(board):
    win = ['X', 'X', 'X']
    lose = ['O', 'O', 'O']

    # check rows
    for row in range(3):
        if board[row] == win:
            print("You win!")
            return True
        elif board[row] == lose:
            print("You lose!")
            return True

    # check columns
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if column == win:
            print("You win!")
            return True
        if column == lose:
            print("You lose!")
            return True

    # check diagonals
    diagonal_one = [board[0][0], board[1][1], board[2][2]]
    if diagonal_one == win:
        print("You win!")
        return True
    elif diagonal_one == lose:
        print("You lose!")
        return True

    diagonal_two = [board[0][2], board[1][1], board[2][0]]
    if diagonal_two == win:
        print("You win!")
        return True
    elif diagonal_two == lose:
        print("You lose!")
        return True

    # check for cat
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                available_moves.append(row*3 + col)
    
    if len(available_moves) == 0:
        print("Cat!")
        return True

    return False


if __name__ == "__main__":
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    print_intro()

    player_turn = 0

    while(winner(board) == False):
        if (player_turn % 2):
            robot_turn(board)
        else:
            human_turn(board)
        
        player_turn += 1
        print_board()