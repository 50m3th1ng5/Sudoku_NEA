#Imports
import time
from puzzle_creation import puzzle_creation, print_board
from data import set_difficulty

#Click run in the gutter to run the program
if __name__ == '__main__':

    print("Program Load")
    
    difficulty = set_difficulty(str(input("Enter a difficulty level: ")).lower())

    start_time = time.time()
    puzzle = puzzle_creation(difficulty)#Generates the puzzle "Instantly" :)

    print(f"Time taken:{round(time.time() - start_time, 2)} seconds")
    print_board(puzzle)

    print("Program End")