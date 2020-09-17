class Sudoku:

    def __init__(self, max_display_solutions=2):
        """ Construction for grid initialization """
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.solutions = []
        self.run = True
        self.max_display_solutions = max_display_solutions

    def str_to_grid(self, str_pzl):
        """ Converting a string of 81 characters to a grid """
        if (type(str_pzl) == str) & (len(str_pzl) == 81) & str_pzl.isdigit():
            for i in range(0, 81):
                self.grid[int(i / 9)][int(i % 9)] = int(str_pzl[i])
        else:
            print("Invalid String!")

    def grid_to_str(self):
        """ Converting the grid to a 81 character string """
        pzl_str = ""
        for y in range(9):
            for x in range(9):
                pzl_str += str(self.grid[y][x])
        return pzl_str

    def solution_to_str(self):
        """ Returns the 1st solution as string """
        if len(self.solutions) > 0:
            pzl_str = ""
            for y in range(9):
                for x in range(9):
                    pzl_str += str(self.solutions[0][x][y])
        else:
            pzl_str = "No Solutions"
        return pzl_str

    def possible(self, y, x, n):
        """ Check if n is a possible value for y,x in the grid  """
        for i in range(0, 9):
            if self.grid[y][i] == n:
                return False
        for i in range(0, 9):
            if self.grid[i][x] == n:
                return False
        y0 = (y//3) * 3
        x0 = (x//3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y0+i][x0+j] == n:
                    return False
        return True

    def reset(self):
        """ Reset the grid and solutions"""
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.solutions = []
        self.run = True

    def solve(self):
        """ Basic recursive function for solving the puzzle """
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.grid[y][x] = n
                            self.solve()
                            if self.run:
                                self.grid[y][x] = 0
                    return
        if self.no_of_solutions() <= self.max_display_solutions:
            self.solutions.append([[self.grid[i][j]
                                    for i in range(9)] for j in range(9)])
        else:
            self.run = False

    def no_of_solutions(self):
        """ Return the number of solutions found. Check MAX_SOLUTIONS varible for max """
        return len(self.solutions)

    def print_grid(self):
        """ Print the grid in a user friendly way """
        print()
        print("Current Grid:")
        print()
        for i in range(9):
            print(self.grid[i])
        print()

    def print_solutions(self):
        """ Print possible solutions in a user friendly way """
        for i in range(len(self.solutions)):
            print()
            print("Solution: " + str(i+1))
            print()
            for j in range(9):
                print(self.solutions[i][j])
            print()

    def get_solutions(self):
        """ Return possible solutions """
        return self.solutions

    def get_grid(self):
        """ Return current grid """
        return self.grid

    def set_max_display_solutions(self, value):
        """ Set maximum solutions to be displayed """
        self.max_display_solutions = value

    def get_max_display_solutions(self):
        """ Get the maximum amount of solutions to be displayed """
        return self.max_display_solutions
    
    def is_valid(self):
        """ Checks if the sudoku is valid """
        a = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    rows = str(self.grid[i][j]) + " in row " + str(i) 
                    cols = str(self.grid[i][j]) + " in column " + str(j) 
                    sqrs = str(self.grid[i][j]) + " in square " + str(i//3) + " - " + str(j//3)
                    if (rows in a) | (rows in a) | (sqrs in a):
                        return False
                    else:
                        a.add(rows)
                        a.add(cols)
                        a.add(sqrs)
        return True
    
    def clues(self):
        """ Returns the number of non-zero digits """
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.grid[i][j] != 0:
                    count += 1
        return count
