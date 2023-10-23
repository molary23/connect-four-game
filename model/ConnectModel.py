class ConnectModel:

    @property
    def board(self):
        return self.__board

    @property
    def current_player(self):
        return self.__current_player

    def __init__(self, m, n):
        if m < 4 or n < 5:
            raise ValueError("The board must be at least 4 x 5")
        self.__board = []
        for i in range(0, m):
            self.__board.append([])
            for j in range(0, n):
                self.__board[i].append(0)
        self.__current_player = "🟡"

    def load_game(self, board, current_player):
        if len(board) < 4:
            raise ValueError("Board must be at least 4 x 5")
        if len(board[0]) < 5:
            raise ValueError("Board must be at least 4 x 5")
        if current_player != 1 and current_player != 2:
            raise ValueError("Current player invalid - must be 1 or 2")
        self.__board = board
        self.__current_player = current_player

    def make_move(self, y):
        if y < 0 or y > len(self.board[0]):
            raise ValueError("Invalid column")
        if self.board[0][y] != 0:
            raise ValueError("Column full")
        row = len(self.board) - 1
        while self.board[row][y] != 0:
            row -= 1
        self.__board[row][y] = self.current_player
        return True

    def check_win(self):
        y_axis = len(self.board[0])
        x_axis = len(self.board)
        for row in range(x_axis):
            for col in range(y_axis):
                if (col + 3 < y_axis and self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2]
                        == self.board[row][col + 3] == self.current_player):
                    return True
                if (row + 3 < x_axis and self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col]
                        == self.board[row + 3][col] == self.current_player):
                    return True
                if (row + 3 < x_axis and col + 3 < y_axis and self.board[row][col] == self.board[row + 1][col + 1]
                        == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] == self.current_player):
                    return True
                if (row + 3 < x_axis and col - 3 >= 0 and self.board[row][col] == self.board[row + 1][col - 1]
                        == self.board[row + 2][col - 2] == self.board[row + 3][col - 3] == self.current_player):
                    return True
        return False

    def check_draw(self):
        for j in range(0, len(self.board[0])):
            if self.board[0][j] == 0:
                return False
        return True

    def next_player(self):
        if self.current_player == "🟡":  # 1
            self.__current_player = "⚫️"  # 2
        else:
            self.__current_player = "🟡"
