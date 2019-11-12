from tkinter import *

from PIL import Image, ImageTk
import main
import xo



class Gui:
    def __init__(self, root, game):
        self.game = game
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.canvas = Canvas(root, width = 640, height = 480, bg = "#10a7c0")
        self.welcome_text = "Welcome to XO Game! The current player is: "
        self.label = Label(root, text =self.welcome_text + "1", font = 13)
        self.label2 = Label(root, text = "player 0 is X and player 1 is O", font =13)
        self.label.grid(row = 0)
        self.label2.grid(row = 1)
        self.canvas.grid(row = 2)
        self.draw_board()

        self.canvas.bind('<Button-1>', self.canvas_click)
        self.exit_b = Button(root, text = "Exit here", command = self.exit)
        self.exit_b.grid(row = 3)
        self.play_again = False

        play_again_button = Button(text="Play again", command=self.set_play_again)
        play_again_button.grid(row=4)

    def exit(self):
        exit()

    def draw_board(self):
        self.canvas.config(width = 300,height = 300)
        self.root.update()
        img = Image.open("Background.jpeg")
        img2 = ImageTk.PhotoImage(img)
        self.canvas.image = img2
        self.canvas.create_image(0, 0, image = img2, anchor = NW)
        self.draw_grid()

    def draw_grid(self):
        self.canvas.create_line(0, 100, 300, 100, width = 7)
        self.canvas.create_line(0, 200, 300, 200, width = 7)
        self.canvas.create_line(100, 0, 100, 300, width = 7)
        self.canvas.create_line(200, 0, 200, 300, width = 7)

    def get_xy(self, location, i):
        if location == "ROW":
            return 0, i, 2, i
        elif location == "COL":
            return i, 0, i, 2
        else:
            return i, 0, abs(i-2), 2


    def create_line(self, location, i):
        x_start, y_start, x_end, y_end = self.get_xy(location, i)
        self.canvas.create_line(x_start*100+50 , y_start*100+50, x_end*100+50, y_end*100+50, width = 5)
        self.label.config(text = "Player " + str(int(not self.game.player))+ " Won!!!")

    def set_play_again(self):
        self.label.config(text = self.welcome_text+ str(1))
        self.game.board = [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
        self.canvas.delete("all")
        self.draw_board()
        self.game.mark = 0
        self.game.player = 1

    def canvas_tie(self):
        self.label.config(text = "Full board, Game over")



    def canvas_click(self, event):
        if self.game.mark == 0:
            x = int(event.x/100)
            y = int(event.y/100)
            self.draw_o(x, y) if self.game.player else self.draw_x(x, y)
            self.game.update_board(x, y)
            win = self.game.check_win()
            self.label.config(text = self.welcome_text + str(self.game.player))
            if win:
                location, i = win
                self.create_line(location, i)
            elif self.game.check_full():
                self.canvas_tie()




    def draw_o(self, x, y):
        my_x = x*100 + 50
        my_y = y*100 + 50
        self.canvas.create_oval(my_x - 30, my_y - 30, my_x + 30, my_y +30, width = 5, fill = "#10a7c0")

    def draw_x(self, x, y):
        x2 = x*100
        y2 = y*100
        self.canvas.create_line(x2 + 25, y2 + 25, x2 + 75, y2 + 75, width = 5)
        self.canvas.create_line(x2 + 25, y2 + 75, x2 + 75, y2 + 25, width = 5)




