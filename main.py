from tkinter import *

from xo_gui import *
from xo import *
play_again = False
def run_game():
        root = Tk()
        game = Game()
        gui = Gui(root, game)
        if play_again:
            run_game()
        mainloop()

if __name__ == '__main__':
    run_game()
