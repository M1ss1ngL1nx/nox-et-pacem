def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    for _ in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if make_move(board, row, col, current_player):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter row and column as integers.")

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    main()
