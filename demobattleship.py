import sys

# 2D matrix for boards
board_one = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
             ["A", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["B", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["C", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["D", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["E", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["F", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["G", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["H", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["I", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
board_one_hidden = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ["A", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["B", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["C", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["D", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["E", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["F", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["G", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["H", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["I", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
board_two = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
             ["A", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["B", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["C", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["D", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["E", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["F", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["G", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["H", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
             ["I", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
board_two_hidden = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ["A", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["B", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["C", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["D", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["E", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["F", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["G", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["H", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["I", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]

# list for changing alphabet to numbers
alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}

# empty list for ships(player one)
player_one_ships = [[], [], []]

# empty list for guesses(player one)
player_one_guesses = [[], [], []]

# empty list for ships(player two)
player_two_ships = [[], [], []]

# empty list for guesses(player two)
player_two_guesses = [[], [], []]

# variable for points
player_one = 0
player_two = 0

# variable for checking every item
n = 0
m = 0


# creating a beautiful board
def print_board(board):
    n = 0
    for i in range(10):
        print(str(" ".join(board[n])))
        n += 1
    return(board)


def ship_instructions(board, ship):
    while True:
        try:
            x = input("Choose row: ")
            for key, value in alphabet.items():
                if x == key:
                    row = value
        except ValueError:
            print('Wrong input!')
            continue
        break

    while True:
        try:
            y = int(input("Choose col: "))
            break
        except ValueError:
            print('Wrong input!')
            continue
        break
    ship.append(row)
    ship.append(y)
    board[ship[0]][ship[1]] = "!"
    return(ship)


def compare(player, board, ship, guess):
    if ship == guess:
        board[ship[0]][ship[1]] = "Y"
        player = player + 1
    elif ship != guess:
        board[ship[0]][ship[1]] = "N"
    else:
        board[ship[0]][ship[1]] = "~"


def main():
    print("Welcome to Battleship game 2.0")
    print("player one is placing the boats")
    print_board(board_one)
    ship_instructions(board_one, player_one_ships[0])
    ship_instructions(board_one, player_one_ships[1])
    ship_instructions(board_one, player_one_ships[2])
    print_board(board_one)
    print("player two is placing the boats")
    print_board(board_two)
    ship_instructions(board_two, player_two_ships[0])
    ship_instructions(board_two, player_two_ships[1])
    ship_instructions(board_two, player_two_ships[2])
    print_board(board_two)
    print('\n')
    print("....Guessing Time....")
    print("Player one is guessing: ")
    print_board(board_two_hidden)
    ship_instructions(board_two_hidden, player_one_guesses[0])
    ship_instructions(board_two_hidden, player_one_guesses[1])
    ship_instructions(board_two_hidden, player_one_guesses[2])
    compare(player_one, board_two_hidden, player_two_ships[0], player_one_guesses[0])
    compare(player_one, board_two_hidden, player_two_ships[0], player_one_guesses[1])
    compare(player_one, board_two_hidden, player_two_ships[0], player_one_guesses[2])
    compare(player_one, board_two_hidden, player_two_ships[1], player_one_guesses[0])
    compare(player_one, board_two_hidden, player_two_ships[1], player_one_guesses[1])
    compare(player_one, board_two_hidden, player_two_ships[1], player_one_guesses[2])
    compare(player_one, board_two_hidden, player_two_ships[2], player_one_guesses[0])
    compare(player_one, board_two_hidden, player_two_ships[2], player_one_guesses[1])
    compare(player_one, board_two_hidden, player_two_ships[2], player_one_guesses[2])
    print(player_one)
    print_board(board_two_hidden)
    print("Player two is guessing: ")
    print_board(board_one_hidden)
    ship_instructions(board_one_hidden, player_two_guesses[0])
    ship_instructions(board_one_hidden, player_two_guesses[1])
    ship_instructions(board_one_hidden, player_two_guesses[2])
    compare(player_two, board_one_hidden, player_one_ships[0], player_two_guesses[0])
    compare(player_two, board_one_hidden, player_one_ships[0], player_two_guesses[1])
    compare(player_two, board_one_hidden, player_one_ships[0], player_two_guesses[2])
    compare(player_two, board_one_hidden, player_one_ships[1], player_two_guesses[0])
    compare(player_two, board_one_hidden, player_one_ships[1], player_two_guesses[1])
    compare(player_two, board_one_hidden, player_one_ships[1], player_two_guesses[2])
    compare(player_two, board_one_hidden, player_one_ships[2], player_two_guesses[0])
    compare(player_two, board_one_hidden, player_one_ships[2], player_two_guesses[1])
    compare(player_two, board_one_hidden, player_one_ships[2], player_two_guesses[2])
    print(player_two)
    print_board(board_one_hidden)
    

main()