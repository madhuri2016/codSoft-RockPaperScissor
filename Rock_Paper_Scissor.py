import tkinter as tk
import random
from tkinter import messagebox

class Rock_Paper_Scissor:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissor")
        self.root.geometry("450x350")

        self.player1 = ""
        self.player2 = ""
        self.player1Scr = 0
        self.player2Scr = 0
        self.choices = ["Rock", "Paper", "Scissor"]

        self.createWindow()

    def createWindow(self):
        self.root.configure(bg="skyblue")
        self.nameFrm = tk.Frame(self.root, bg="skyblue")
        self.nameFrm.pack(pady=20)

        gameLabel=tk.Label(self.nameFrm, text="ROCK-PAPER-SCISSORS", font=("Algerian", 14), bg="skyblue")
        gameLabel.grid(row=0, column=0, columnspan=2, pady=10)
        
        player1Label=tk.Label(self.nameFrm, text="Player 1 Name:", font=("Elephant", 10), bg="skyblue")
        player1Label.grid(row=1, column=0, pady=10)
        self.player1data = tk.Entry(self.nameFrm)
        self.player1data.grid(row=1, column=1)

        player2Label=tk.Label(self.nameFrm, text="Player 2 Name:", font=("Elephant", 10), bg="skyblue")
        player2Label.grid(row=2, column=0, pady=10)
        self.player2data = tk.Entry(self.nameFrm)
        self.player2data.grid(row=2, column=1)

        startGameBtn=tk.Button(self.nameFrm, text="Start Game", command=self.startGame)
        startGameBtn.grid(row=3, column=0, columnspan=2, pady=20)

    def startGame(self):
        self.player1 = self.player1data.get()
        self.player2 = self.player2data.get()

        if not self.player1 or not self.player2:
            messagebox.showwarning("Warning", "Please enter the names.")
            return

        self.nameFrm.pack_forget()
        self.setupGame()

    def setupGame(self):
        self.score_frame = tk.Frame(self.root, bg="grey")
        self.score_frame.pack(pady=10)

        self.player1_label = tk.Label(self.score_frame, text=f"{self.player1}: 0", bg="grey", font=("Arial", 12))
        self.player1_label.grid(row=0, column=0, padx=20)

        self.player2_label = tk.Label(self.score_frame, text=f"{self.player2}: 0", bg="grey", font=("Arial", 12))
        self.player2_label.grid(row=0, column=1, padx=20)

        self.gameFrm = tk.Frame(self.root, bg="grey")
        self.gameFrm.pack(pady=20)

        self.player1Btn = tk.Button(self.gameFrm, text="Play Player 1", command=self.playPlayer1Btn, bg="lightblue")
        self.player1Btn.grid(row=1, column=0, padx=20)

        self.player2Btn = tk.Button(self.gameFrm, text="Play Player 2", command=self.playPlayer2Btn, bg="lightblue")
        self.player2Btn.grid(row=1, column=1, padx=20)

        self.resultBoard = tk.Label(self.root, text="", bg="grey", font=("Arial", 14))
        self.resultBoard.pack(pady=20)

        self.continueFrm = tk.Frame(self.root, bg="grey")
        self.continueFrm.pack(pady=10)

    def playPlayer1Btn(self):
        self.player1Option = random.choice(self.choices)
        self.resultBoard.config(text=f"{self.player1} chose {self.player1Option}")
        self.check_both_played()

    def playPlayer2Btn(self):
        self.player2Option = random.choice(self.choices)
        self.resultBoard.config(text=f"{self.player2} chose {self.player2Option}")
        self.check_both_played()

    def check_both_played(self):
        if hasattr(self, 'player1Option') and hasattr(self, 'player2Option'):
            self.determine_winner()

    def determine_winner(self):
        player1Option = self.player1Option
        player2Option = self.player2Option

        if player1Option == player2Option:
            relsult = "It's a tie!"
        elif (player1Option == "Rock" and player2Option == "Scissor") or \
             (player1Option == "Paper" and player2Option == "Rock") or \
             (player1Option == "Scissor" and player2Option == "Paper"):
            relsult = f"{self.player1} won!"
            self.player1Scr += 1
        else:
            relsult = f"{self.player2} won!"
            self.player2Scr += 1

        messagebox.showinfo("Result", relsult)
        self.newScoreBoard()
        self.show_continue_options()

    def newScoreBoard(self):
        self.player1_label.config(text=f"{self.player1}: {self.player1Scr}")
        self.player2_label.config(text=f"{self.player2}: {self.player2Scr}")

    def show_continue_options(self):
        self.continueFrm.pack()
        tk.Button(self.continueFrm, text="Continue", command=self.continueGame, bg="lightgreen").grid(row=0, column=0, padx=10)
        tk.Button(self.continueFrm, text="End Game", command=self.end, bg="lightcoral").grid(row=0, column=1, padx=10)

    def continueGame(self):
        self.resultBoard.config(text="")
        self.continueFrm.pack_forget()
        delattr(self, 'player1Option')
        delattr(self, 'player2Option')

    def end(self):
        self.score_frame.pack_forget()
        self.gameFrm.pack_forget()
        self.resultBoard.pack_forget()
        self.continueFrm.pack_forget()
        self.player1Scr = 0
        self.player2Scr = 0
        self.createWindow()

if __name__ == "__main__":
    root = tk.Tk()
    app = Rock_Paper_Scissor(root)
    root.mainloop()
