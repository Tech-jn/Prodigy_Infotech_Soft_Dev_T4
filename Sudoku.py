import tkinter as tk

from tkinter import messagebox



class SudokuSolverGUI:

    def __init__(self, master):

        self.master = master

        self.master.title("Sudoku Solver")

        self.master.configure(bg='brown')

        

        self.grid = [

            [3, 0, 6, 5, 0, 8, 4, 0, 0],

            [5, 2, 0, 0, 0, 0, 0, 0, 0],

            [0, 8, 7, 0, 0, 0, 0, 3, 1],

            [0, 0, 3, 0, 1, 0, 0, 8, 0],

            [9, 0, 0, 8, 6, 3, 0, 0, 5],

            [0, 5, 0, 0, 9, 0, 6, 0, 0],

            [1, 3, 0, 0, 0, 0, 2, 5, 0],

            [0, 0, 0, 0, 0, 0, 0, 7, 4],

            [0, 0, 5, 2, 0, 6, 3, 0, 0]

        ]



        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_widgets()

    

    def create_widgets(self):

        for i in range(9):

            for j in range(9):

                entry = tk.Entry(self.master, width=4, font=("Helvetica", 16), justify='center', bd=2, relief='solid')

                entry.grid(row=i, column=j, padx=5, pady=5)

                if self.grid[i][j] != 0:

                    entry.insert(0, self.grid[i][j])

                    entry.config(state='disabled', disabledbackground='#D3D3D3', disabledforeground='#000000')

                self.entries[i][j] = entry

        

        solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku, font=("Helvetica", 16), bg='#90EE90')

        solve_button.grid(row=9, column=0, columnspan=9, pady=20)

    

    def solve_sudoku(self):

        grid = [[int(self.entries[i][j].get()) if self.entries[i][j].get() else 0 for j in range(9)] for i in range(9)]

        

        if self.sudoku_solver(grid):

            for i in range(9):

                for j in range(9):

                    self.entries[i][j].delete(0, tk.END)

                    self.entries[i][j].insert(0, grid[i][j])

        else:

            messagebox.showerror("Error", "No solution exists")

    

    def sudoku_solver(self, grid):

        l = [0, 0]

        if not self.find_empty_location(grid, l):

            return True

        row, col = l

        for num in range(1, 10):

            if self.is_safe(grid, row, col, num):

                grid[row][col] = num

                if self.sudoku_solver(grid):

                    return True

                grid[row][col] = 0

        return False



    def find_empty_location(self, grid, l):

        for row in range(9):

            for col in range(9):

                if grid[row][col] == 0:

                    l[0], l[1] = row, col

                    return True

        return False



    def is_safe(self, grid, row, col, num):

        if num in grid[row]:

            return False

        if num in [grid[i][col] for i in range(9)]:

            return False

        start_row, start_col = row - row % 3, col - col % 3

        for i in range(3):

            for j in range(3):

                if grid[i + start_row][j + start_col] == num:

                    return False

        return True



if __name__ == "__main__":

    root = tk.Tk()

    app = SudokuSolverGUI(root)

    root.mainloop()
