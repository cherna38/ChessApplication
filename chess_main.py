from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout

from chess_piece import *

import sys


class ChessTeam():
    def __init__(self) -> None:
        self.team = None

    def set_up_pieces(self):
        pass


class ChessGame(QMainWindow):
    def __init__(self) -> None:
        super(ChessGame, self).__init__()
        self.setWindowTitle("The Beautiful Game Of Chess")
        self.black_team = None
        self.white_team = None
        self._board = None
        self.create_board()
        self.create_pieces()

        self.first_square_selection: ChessSquare = None
        self.second_square_selection: ChessSquare = None

    def launch():
        pass

    def set_up_game_pieces(self, array):
        # array
        # for row in range(len(arr[0])):
        #     for col in range(len(arr[1])):
        pass

    def set_up_pawns(self, row, team):
        layout = self.get_board()

        for col in range(CHESS_BOARD_LENGTH):
            w_square = ChessSquare(row, col, Pawn(team))
            w_square.BTN_PUSHED.connect(self.on_square_clicked)
            layout.addWidget(
                w_square
            )

    def set_up_elite_pieces(self, row, team):
        layout = self.get_board()

        for col, piece_class in enumerate(CHESS_PIECE_ORDER):
            w_square = ChessSquare(row, col, piece_class(team))
            w_square.BTN_PUSHED.connect(self.on_square_clicked)
            layout.addWidget(
                w_square,
                row,
                col,
            )

    def set_up_empty_squares(self):
        layout = self.get_board()

        for row in range(2, 6):
            for col in range(CHESS_BOARD_WIDTH):
                w_square = ChessSquare(row, col)
                w_square.BTN_PUSHED.connect(self.on_square_clicked)
                layout.addWidget(
                    w_square,
                    row,
                    col,
                )

    def set_up_layout(self):
        layout = self.get_board()

        # TODO: set up functionality for random team
        # set up black pieces
        self.set_up_elite_pieces(ELITE_PIECES[0], ChessPiece.TEAM_BLACK)
        self.set_up_pawns(PAWN_ROW[0], ChessPiece.TEAM_BLACK)

        self.set_up_empty_squares()

        # set up white pieces
        self.set_up_pawns(PAWN_ROW[1], ChessPiece.TEAM_WHITE)
        self.set_up_elite_pieces(ELITE_PIECES[1], ChessPiece.TEAM_WHITE)

        # make squares different colors
        self.checker_the_board()

        layout.setSpacing(0)

    def checker_the_board(self):
        '''Set up the look of every square.
        '''
        board = self.get_board()
        for row in range(CHESS_BOARD_LENGTH):
            for col in range(CHESS_BOARD_WIDTH):
                square = self.get_square_at(row, col)
                cor_sum = row + col

                color = "background-color : "
                if cor_sum % 2 == 0 or cor_sum == 0:
                    color += "brown"
                else:
                    color += "white"

                square.setStyleSheet(color)

    def reset_selected_squares(self):
        self.first_square_selection = None
        self.second_square_selection = None

    def get_square_at(self, row, col) -> ChessSquare:
        lay = self.get_board()
        layout_item = lay.itemAtPosition(row, col)
        square = layout_item.widget()
        return square

    def on_square_clicked(self, row, col):
        chess_square = self.get_square_at(row, col)
        chess_piece = chess_square.get_chess_piece()

        # first selection must have a piece if not return and reset
        if self.first_square_selection == None:
            if chess_piece:
                self.first_square_selection = chess_square
            else:
                self.reset_selected_squares()
            return

        if self.first_square_selection == chess_square:
            self.reset_selected_squares()
            return

        if self.second_square_selection == None:
            self.second_square_selection = chess_square
            self.move_chess_piece(
                self.first_square_selection,
                self.second_square_selection,
            )
            # chess_piece.move()

    def move_chess_piece(self, from_square: ChessSquare, to_square: ChessSquare):
        lay = self.get_board()
        to_square.set_chess_piece(
            from_square.get_chess_piece()
        )

        from_square.set_chess_piece(None)

        self.reset_selected_squares()

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
