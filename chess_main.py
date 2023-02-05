from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout


from chess_piece import *

import sys

class ChessGame(QMainWindow):
    def __init__(self) -> None:
        super(ChessGame, self).__init__()
        self.setWindowTitle("The Beautiful Game Of Chess")
        self.black_team = None
        self.white_team = None
        self._board = None
        self.create_board()
        self.create_pieces()


    def launch():
        pass

    def set_up_layout(self):
        layout = self.get_board()

        rows, cols = (8, 8)
        arr = [[0]*cols]*rows

        for row in range(len(arr[0])):
            for col in range(len(arr[1])):
                w = Color("green")
                w.clicked.connect(self.on_btn_clicked)
                Color.BTN_PUSHED.connect(self.on_btn_clicked)
                layout.addWidget( w, row, col)

    def on_btn_clicked(self, cordinates):
        pass


    def create_board(self):
        self._board = QGridLayout()
        widget = QWidget()
        self.set_up_layout()
        widget.setLayout(self.get_board())
        self.setCentralWidget(widget)

    def get_board(self):
        return self._board

    def create_pieces(self):
        pass

    def piece_has_moved(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGame()
    window.show()

    app.exec()
