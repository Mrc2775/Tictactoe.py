import random

def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1, choose X or O: ").upper()
    player1 = marker
    player2 = 'O' if marker == 'X' else 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def is_space_free(board, position):
    return board[position] == ' '

def check_win(board, marker):
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diags
    ]
    for combo in combos:
        if all(board[i] == marker for i in combo):
            return True
    return False

def is_full(board):
    return ' ' not in board

def player_choice(board):
    while True:
        try:
            pos = int(input("Choose a position (1-9): ")) - 1
            if pos in range(9) and is_space_free(board, pos):
                return pos
            else:
                print("Position is invalid or already taken.")
        except:
            print("Please enter a number between 1 and 9.")

def replay():
    choice = input("Play again? (yes/no): ").lower()
    return choice.startswith('y')

def play_game():
    print("Welcome to Tic Tac Toe!")

    while True:
        board = [' '] * 9
        player1, player2 = player_input()
        current_player = random.choice(['Player 1', 'Player 2'])
        print(f"{current_player} goes first.")

        playing = True

        while playing:
            display_board(board)

            marker = player1 if current_player == 'Player 1' else player2
            print(f"{current_player}'s turn ({marker})")

            pos = player_choice(board)
            place_marker(board, marker, pos)

            if check_win(board, marker):
                display_board(board)
                print(f"{current_player} wins!")
                playing = False
            elif is_full(board):
                display_board(board)
                print("It's a draw!")
                playing = False
            else:
                current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'

        if not replay():
            print("Thanks for playing!")
            break


play_game()







