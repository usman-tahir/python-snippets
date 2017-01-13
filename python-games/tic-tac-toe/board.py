
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.currentBoard = Board.createBoard(self, self.rows, self.columns)

    def createBoard(self, rows, columns):
        emptyRows = [' '] * rows
        generatedBoard = []
        for column in range(columns):
            generatedBoard.append(emptyRows)
        # print(generatedBoard)
        return generatedBoard

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_board(self):
        return self.Board

    def set_rows(self, rows):
        self.rows = rows

    def set_columns(self, columns):
        self.columns = columns

    def set_board(self, board):
        self.board = board

    def __str__(self):
        column_separator = " | "
        row_separator = "\n" + (self.rows * "-----") + "\n"
        output = ""
        for row in range(len(self.currentBoard)):
            for move in self.currentBoard[row]:
                output += move + column_separator
            if row < len(self.currentBoard) - 1:
                output += row_separator
        return output

b = Board(2, 2)
print(str(b))
