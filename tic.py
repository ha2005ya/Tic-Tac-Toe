import random
import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ("X", "O")  # X = human, O = AI
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.results = []

    def print_board(self):
        for i, row in enumerate(self.board):
            row_display = " | ".join(cell if cell != " " else "  " for cell in row)
            print(" " + row_display)
            if i < 2:
                print("-" * 15)

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def player_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if self.board[row][col] == " ":
                    self.board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 0 and 2.")

    def ai_move(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    if self.check_winner() == "O":
                        return
                    self.board[i][j] = " "

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    if self.check_winner() == "X":
                        self.board[i][j] = "O"
                        return
                    self.board[i][j] = " "

        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = "O"

    def play(self):
        self.reset_board()
        while True:
            print("\nWelcome to Tic-Tac-Toe!")
            self.print_board()

            while True:
                print("\nYour turn:")
                self.player_move()
                self.print_board()
                winner = self.check_winner()
                if winner or self.is_draw():
                    break

                print("\nAI's turn...")
                self.ai_move()
                self.print_board()
                winner = self.check_winner()
                if winner or self.is_draw():
                    break

            if winner:
                print(f"\n{winner} wins!")
                self.scores[winner] += 1
            else:
                print("\nIt's a draw!")
                self.scores["Draws"] += 1

            self.results.append([self.scores["X"], self.scores["O"], self.scores["Draws"]])
            print("\nScores:", self.scores)

            again = input("\nDo you want to play again? (yes or no): ").lower()
            if again != "yes":
                break
            self.reset_board()

        results_array = np.array(self.results)
        print("\nAll results:\n", results_array)


game = TicTacToe()
game.play()
