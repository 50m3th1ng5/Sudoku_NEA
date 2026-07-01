import random


def create_full_board():
    """Generates a random, fully completed valid 9x9 Sudoku board."""
    board = [['.'] * 9 for _ in range(9)]
    digits = [str(i) for i in range(1, 10)]

    def fill(row=0, col=0):
        if row == 9:
            return True

        next_r = row + 1 if col == 8 else row
        next_c = 0 if col == 8 else col + 1

        # Use random.sample to avoid high-frequency array allocations in recursion loop
        for num in random.sample(digits, 9):
            if is_valid(board, row, col, num):
                board[row][col] = num

                if fill(next_r, next_c):
                    return True

                board[row][col] = '.'
        return False

    fill()
    return board


def is_valid(board, row, col, num_str):
    """Verifies if a number placement complies with Sudoku constraints."""
    for i in range(9):
        if board[row][i] == num_str or board[i][col] == num_str:
            return False

    # Row slicing handles 3x3 box scanning faster than a nested loop
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        if num_str in board[box_row + i][box_col:box_col + 3]:
            return False

    return True


def count_solutions_opt(board, row=0, col=0, limit=2):
    """
    Returns the number of unique solutions found up to the specified limit.
    Modifies the board in-place to optimize performance.
    """
    if row == 9:
        return 1

    next_r = row + 1 if col == 8 else row
    next_c = 0 if col == 8 else col + 1

    if board[row][col] != '.':
        return count_solutions_opt(board, next_r, next_c, limit)

    count = 0
    for num in "123456789":
        if is_valid(board, row, col, num):
            board[row][col] = num
            count += count_solutions_opt(board, next_r, next_c, limit)
            board[row][col] = '.'

            if count >= limit:
                return count
    return count


def puzzle_creation(clues_target):
    """Generates a playable Sudoku puzzle with a guaranteed unique solution."""
    board = create_full_board()
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    removed = 0
    max_removals = 81 - clues_target

    for row, col in cells:
        if removed >= max_removals:
            break

        backup = board[row][col]
        board[row][col] = '.'

        # Solvers naturally revert their board modifications, making copies unnecessary
        if count_solutions_opt(board) == 1:
            removed += 1
        else:
            board[row][col] = backup

    print(f"\nGenerated puzzle with {81 - removed} clues successfully!")
    return board


def print_board(board):
    """Prints the Sudoku board with a clean, formatted sub-grid grid layout."""
    print("\n-------------------------")
    for i in range(9):
        for j in range(9):
            if j == 0:
                print("|", end=" ")
            print(f"{board[i][j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end="")
        print()
