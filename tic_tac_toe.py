import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.player = 'X'
        self.board = [' '] * 9
        self.win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.labels = []
        self.buttons = []

        for i in range(9):
            button_x = 100 + (i % 3) * 100
            button_y = 100 + (i // 3) * 100

            b = tk.Button(self.root, text=' ', bg='white', font=('Helvetica', 20),
                          command=lambda i=i: self.clicked(i))
            b.place(x=button_x, y=button_y, width=90, height=90)

            self.labels.append(tk.Label(self.root, text=' ', font=('Helvetica', 14), fg='black'))
            self.labels[-1].place(x=button_x + 10, y=button_y + 80)

            self.buttons.append(b)

        self.root.mainloop()

    def clicked(self, i):
        if self.board[i] == ' ':
            self.board[i] = self.player
            self.labels[i].config(text=self.player)

            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.player} wins!")
                self.root.destroy()

            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.destroy()

            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_win(self):
        for combo in self.win_combo:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

TicTacToe()