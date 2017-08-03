import gspread

class Cell(gspread.Worksheet):
    def _cell_addr(self, row, col):
        return (row, col)

    def cell(self, row, col):
        feed = self.client.get_cells_cell_id_feed(self,
                                                  self._cell_addr(row, col))
        return Cell(self, feed)
