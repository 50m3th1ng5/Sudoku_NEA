import random

def create_full_board():
    board = [['.'] * 9 for _ in range(9)]

    def fill(row=0, colum=0):
        if row == 9:
            return True
        next_r = row + 1 if colum == 8 else row
        next_c = 0 if colum == 8 else colum + 1

        nums = list(map(str, range(1, 10)))
        random.shuffle(nums)  # Shuffle ensures a random unique board every time

        for num in nums:
            if is_valid(board, row, colum, num):
                board[row][colum] = num
                if fill(next_r, next_c):
                    return True
                board[row][colum] = '.'
        return False

    fill()
    return board


def is_valid(board, row, col, num_str):
    # Check row and column
    for i in range(9):
        if board[row][i] == num_str or board[i][col] == num_str:
            return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num_str:
                return False
    return True


def count_solutions_opt(board, row=0, colum=0, limit=2):
    if row == 9:
        return 1  # Reached the end, valid full solution found

    next_r = row + 1 if colum == 8 else row
    next_c = 0 if colum == 8 else colum + 1

    if board[row][colum] != '.':
        return count_solutions_opt(board, next_r, next_c, limit)

    count = 0
    for num in map(str, range(1, 10)):
        if is_valid(board, row, colum, num):
            board[row][colum] = num
            count += count_solutions_opt(board, next_r, next_c, limit)
            board[row][colum] = '.'  # Backtrack

            if count >= limit:
                return count
    return count


def puzzle_creation(clues_target):
    #Start with a completed board
    board = create_full_board()

    #Create a list of all 81 cell coordinates and shuffle them
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    removed = 0
    max_removals = 81 - clues_target

    #Iterate through the board
    for row, col in cells:
        if removed >= max_removals:
            break

        backup = board[row][col]
        board[row][col] = '.'  # Attempt to empty the cell

        # Verify if the board has exactly one unique solution
        if count_solutions_opt([r[:] for r in board]) == 1:
            removed += 1
        else:
            board[row][col] = backup  #Use backup if board doesn't have a unique solution

    print(f"\nGenerated puzzle with {81 - removed} clues successfully!")
    return board


'''Only Temporary was stolen from stack overflow for testing reasons'''
def print_board(board):

    print("\n-------------------------")

    for i in range(9):
        for j in range(9):
            if board[i][j] is not None:
                if j == 0:
                    print("|", end=" ")
                print(f"{board[i][j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end=" ")
        print()