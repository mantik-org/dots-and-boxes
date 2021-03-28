

class GameAgent:

    def __init__(self, id, grid, timelimit):

        rows, cols = grid

        self.ids = { id }
        self.rows = rows
        self.cols = cols
        self.board = []

        for _ in range(rows + 1):
            col = []
            for _ in range(cols + 1):
                col.append({ 'v' : 0, 'h': 0 })
            self.board.append(col)


    def add(self, id):
        self.ids.add(id)
        