# Tic-Tac-Toe game in Python

# Create a 3x3 board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Define the players
player1 = 'X'
player2 = 'O'

# Start the game
current_player = player1

# Game loop
while True:

    # Print the board
    print_board(board)

    # Get the current player's move
    move = get_move(current_player)

    # Make the move
    board[move[0]][move[1]] = current_player

    # Check if the game is over
    winner = check_winner(board)
    if winner is not None:
        break

    # Switch players
    current_player = player2 if current_player == player1 else player1


# Check for a winner
def check_winner(board):
    for i in range(3):
        # Check for a horizontal win
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return board[i][0]

        # Check for a vertical win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return board[0][i]

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    # If there is no winner, return None
    return None


# Print the board
def print_board(board):
    for row in board:
        print(' '.join(row))


# Get the current player's move
def get_move(current_player):
    while True:
        move = input('{}\'s turn: Enter a row and column (e.g. 1,1): '.format(current_player))

        # Validate the move
        try:
            row, col = move.split(',')
            row = int(row)
            col = int(col)
        except ValueError:
            print('Invalid move. Please try again.')
            continue

        if row not in range(3) or col not in range(3):
            print('Invalid move. Please try again.')
            continue

        # Check if the space is empty
        if board[row][col] != '-':
            print('That space is already taken. Please try again.')
            continue

        # If the move is valid, return it
        return row, col


# Start the game
if __name__ == '__main__':
    play_game()
