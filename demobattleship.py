import sys

# Board 1


def program_end():
    sys.exit('Exit')


def print_board_1(board_1):
    chars = [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(" ".join(chars))

    for index, row in enumerate(board_1):
        print(str(index) + " " + " ".join(row))


board_1 = []

# Board 2


def print_board_2(board_2):
    chars = [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(" ".join(chars))

    for index, row in enumerate(board_2):
        print(str(index) + " " + " ".join(row))


board_2 = []

# player 1 make ship


def player_1shipmake():
    print('Player 1 board: ', '\n')

    for i in range(10):
        board_1.append(["<"] * 10)

    print_board_1(board_1)
    while True:
        try:
            for turn in range(1):
                place_row_1 = int(input("P1 choose row to make ship:"))
                break
        except ValueError:
            print('Number please!')
            continue
        break

    while True:
        try:
            for turn in range(1):
                place_col_1 = int(input("P1 choose col to make ship:"))
                print('\n')
                board_1[place_row_1][place_col_1] = ">"
                print_board_1(board_1)
                print('\n')
                break
        except ValueError:
            print('Number please!')
            continue
        break
    return [place_row_1, place_col_1]

# player 2 make ship


def player_2shipmake():
    print('Player 2 board: ', '\n')

    for i in range(10):
        board_2.append([">"] * 10)

    print_board_2(board_2)
    while True:
        try:
            for turn in range(1):
                place_row_2 = int(input("P2Choose Row to make ship:"))
                break
        except ValueError:
            print('Number please!')
            continue
        break

    while True:
        try:
            for turn in range(1):
                place_col_2 = int(input("P2Choose Col to make ship:"))
                print('\n')
                board_2[place_row_2][place_col_2] = "<"
                print_board_2(board_2)
                print('\n')
                break
        except ValueError:
            print('Number please!')
            continue
        break
    return [place_row_2, place_col_2]

# player 1 guess


def player_1guess():
    while True:
        try:
            for turn in range(1):
                place_row_2 = int(input("P1 guess a Row:"))
                break
        except ValueError:
            print('Number please!')
            continue
        break

    while True:
        try:
            for turn in range(1):
                place_col_2 = int(input("P1 guess a col :"))
                print('\n')
                board_2[place_row_2][place_col_2] = "X"
                print_board_2(board_2)
                print('\n')
                break
        except ValueError:
            print('Number please!')
            continue
        break
    return [place_row_2, place_col_2]

# player 2 guess


def player_2guess():
    while True:
        try:
            for turn in range(1):
                guess_row_2 = int(input("P2 guess row to fire:"))
                break
        except ValueError:
            print('Number please!')
            continue
        break

    while True:
        try:
            for turn in range(1):
                guess_col_2 = int(input("P1 guess col to fire:"))
                print('\n')
                board_1[guess_row_2][guess_col_2] = "X"
                print_board_1(board_1)
                print('\n')
                break
        except ValueError:
            print('Number please!')
            continue
        break
    return [guess_row_2, guess_col_2]

# main


shipP1 = player_1shipmake()
shipP2 = player_2shipmake()
guessP1 = player_1guess()
if guessP1 == shipP2:
    print('PLayer 1 sunk Player 2 boat')
    program_end()
else:
    print("You missed it...")
    player_1guess()
guessP2 = player_2guess()
if guessP2 == shipP1:
    print('PLayer 2 sunk Player 1 boat')
    program_end()
else:
    print("You missed it...")
    player_2guess()
