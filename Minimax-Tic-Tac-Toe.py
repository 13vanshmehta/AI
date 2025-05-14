def print_board(board):
    """Print the Tic-Tac-Toe board"""
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")

def check_winner(board):
    """Check if there is a winner or a tie"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
    
    # Check for tie
    if ' ' not in board:
        return 'Tie'
    
    # Game is still ongoing
    return None

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm implementation
    Returns the best score for the current board state
    """
    # Check terminal states
    result = check_winner(board)
    if result == 'X':
        return 10 - depth
    elif result == 'O':
        return depth - 10
    elif result == 'Tie':
        return 0
    
    # Maximizing player (X)
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '  # Undo move
                best_score = max(score, best_score)
        return best_score
    
    # Minimizing player (O)
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '  # Undo move
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Find the best move for the AI (X) using minimax"""
    best_score = float('-inf')
    best_move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '  # Undo move
            
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

def main():
    # Initialize empty board
    board = [' ' for _ in range(9)]
    
    # Decide who goes first
    choice = int(input("Who goes first? (1: AI, 2: Player): "))
    player_turn = choice == 2
    
    # Game loop
    while True:
        print_board(board)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break
        
        if player_turn:
            # Player's turn
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'O'
            else:
                print("Invalid move. Try again.")
                continue
        else:
            # AI's turn
            move = find_best_move(board)
            board[move] = 'X'
            print(f"AI chose position {move}")
        
        # Switch turns
        player_turn = not player_turn

if __name__ == "__main__":
    main()