import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_available_moves(board):
    # Get a list of available moves
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def evaluate_board(board):
    # Evaluate the board for Minimax algorithm
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player):
    # Minimax algorithm with alpha-beta pruning
    result = evaluate_board(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'O'
            eval = minimax(new_board, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'X'
            eval = minimax(new_board, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    # Find the best move for the AI using Minimax algorithm
    best_eval = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = 'O'
        eval = minimax(new_board, 0, False)

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue

        print_board(board)

        # Check if the human player wins or the board is full
        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI player's move
        print("AI's move:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'O'

        print_board(board)

        # Check if the AI player wins or the board is full
        if is_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
