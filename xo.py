
EMPTY = -1

class Game:
    def __init__(self):
        self.board = [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
        self.player = 1
        self.mark = 0

    def row(self):
        for y in range(3):
            row = self.board[y]
            if row[0] == row[1] == row[2] and row[0] != -1:
                return y

    def column(self):
        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] and self.board[0][x] != -1:
                return x


    def diagonal(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != -1:
            return 0
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != -1:
            return 2

    def check_win(self):
        win1 = self.row()
        win2 = self.column()
        win3 = self.diagonal()
        if win1 is not None:
            self.mark = 1
            return "ROW", win1
        elif win2 is not None:
            self.mark = 1
            return "COL", win2
        elif win3 is not None:
            self.mark = 1
            return "DIAG", win3



    def update_board(self, x, y):
        self.board[y][x] = self.player
        self.player = 1 if self.player == 0 else 0

    def check_full(self):
        for i in self.board:
            for x in i:
                if x == -1:
                    return False
        return True











