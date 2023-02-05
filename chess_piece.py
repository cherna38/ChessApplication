from enum import Enum, auto
from PySide6.QtGui import QPalette, QColor, QMouseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Signal

class Color(QPushButton):
    BTN_PUSHED = Signal(int)
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

    def mousePressEvent(self, e:QMouseEvent) -> None:
        self.BTN_PUSHED.emit(1)#(self.row, self.col))
        return super().mousePressEvent(e)

    def set_position(self, row, col):
        self.row = row
        self.col = col

class PieceType(Enum):
    PAWN = auto()
    ROOK = auto()
    BISHOP = auto()
    KNIGHT = auto()
    QUEEN = auto()
    KING = auto()


class ChessPiece():
    def __init__(self, team_color, type:PieceType) -> None:
        self.team = team_color
        self.type = type
        self.location = None
        self.piece_image = None

    def move(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def is_legal_move(self):
        pass


class Pawn(ChessPiece):
    def __init__(self) -> None:
        super().__init__()


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