from enum import Enum, auto
from PySide6.QtGui import QPalette, QColor, QMouseEvent, QImage
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Signal
from chess_tools import *


class PieceType(Enum):
    PAWN = auto()
    ROOK = auto()
    BISHOP = auto()
    KNIGHT = auto()
    QUEEN = auto()
    KING = auto()


class ChessPiece():
    TEAM_BLACK = "black"
    TEAM_WHITE = "white"

    def __init__(self, team_color) -> None:  # type: PieceType
        self.team = team_color
        self.type = type
        self.location = None
        self.piece_image = None
        self.piece_image = self.get_piece_image()

    def move(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_team(self):
        raise NotImplementedError

    def get_piece_image(self):
        if not self.piece_image:
            self.piece_image = load_svg(
                self.get_team(), self.get_name()
            )

        return self.piece_image

    def is_legal_move(self):
        pass


class Pawn(ChessPiece):
    def __init__(self, team_color) -> None:
        self._name = "pawn"
        super().__init__(team_color)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name

    def get_team(self):
        return self.team


class Rook(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


class Bishop(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


class Knight(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


class Queen(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


class King(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


class ChessSquare(QPushButton):
    BTN_PUSHED = Signal(int, int)

    def __init__(self, row: int, col: int, chess_piece: ChessPiece = None):
        super(ChessSquare, self).__init__()
        self.setAutoFillBackground(True)

        color = "red"
        self.square_img = None
        if chess_piece:
            color = chess_piece.get_team()
            self.square_img = chess_piece.get_piece_image()

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        self.row = row
        self.col = col

        self.chess_piece: ChessPiece = chess_piece

        self.set_square_image()

    def get_square_image(self) -> QImage:
        if self.chess_piece:
            return self.chess_piece.get_piece_image()

        return None

    def set_square_image(self):
        img = self.get_square_image()
        if img:
            self.setIcon(img)

    def set_chess_piece(self, chess_piece: ChessPiece):
        self.chess_piece = chess_piece
        self.set_square_image()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.BTN_PUSHED.emit(self.row, self.col)
        return super().mousePressEvent(e)

    def set_position(self, row, col):
        self.row = row
        self.col = col
