import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def ai_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board) == "O":
                    return
                board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board) == "X":
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    if board[1][1] == " ":
        board[1][1] = "O"
        return

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        if board[corner[0]][corner[1]] == " ":
            board[corner[0]][corner[1]] = "O"
            return

    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for side in sides:
        if board[side[0]][side[1]] == " ":
            board[side[0]][side[1]] = "O"
            return

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken, choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 1 and 3.")

        print_board(board)

        if check_winner(board) == "X":
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move(board)
        print_board(board)

        if check_winner(board) == "O":
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
