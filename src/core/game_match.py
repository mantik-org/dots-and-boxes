

class GameMatch:

    def __init__(self, identifier, grid, timelimit):

        rows, cols = grid

        self.ids = { identifier }
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
        