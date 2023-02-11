from enum import Enum, auto
import operator
from PySide6.QtGui import QPalette, QColor, QMouseEvent, QImage
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal, QSize
from chess_tools import *


class PieceType(Enum):
    PAWN = auto()
    ROOK = auto()
    BISHOP = auto()
    KNIGHT = auto()
    QUEEN = auto()
    KING = auto()


class ChessSquare(QPushButton):
    BTN_PUSHED = Signal(int, int)

    def __init__(self, row: int, col: int, chess_piece: "ChessPiece" = None):
        super(ChessSquare, self).__init__()
        self.setAutoFillBackground(True)

        color = "brown"
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

        self.setFixedSize(50, 50)

        self.setIconSize(QSize(40, 40))

    def get_square_image(self) -> QImage:
        if self.chess_piece:
            return self.chess_piece.get_piece_image()

        return None

    def set_square_image(self):
        img = self.get_square_image()
        if img:
            self.setIcon(img)
        else:
            self.setIcon(QPixmap())

    def set_chess_piece(self, chess_piece: "ChessPiece"):
        self.chess_piece = chess_piece
        self.set_square_image()

    def get_chess_piece(self) -> "ChessPiece":
        if self.chess_piece:
            return self.chess_piece

        return None

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.BTN_PUSHED.emit(self.row, self.col)
        return super().mousePressEvent(e)

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self) -> int | int:
        return self.row, self.col


class ChessTeam():
    def __init__(self, team_color, starting_position) -> None:
        self.team = team_color
        self.position = starting_position

    def get_team(self):
        return self.team

    def get_starting_side(self):
        return self.position


class ChessPiece():
    def __init__(self, team: ChessTeam) -> None:
        self.team = team
        # self.type = type
        self.location = None
        self.piece_image = None
        self.piece_image = self.get_piece_image()

    def get_team(self):
        return self.team.get_team()

    def move(self, from_square: ChessSquare, to_square: ChessSquare) -> bool:
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def get_name(self):
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
    def __init__(self, chess_team) -> None:
        self._name = "pawn"
        super().__init__(chess_team)

        if self.team.get_starting_side() is TOP_OF_BOARD:
            self.operation = operator.lt
        else:
            self.operation = operator.gt

    def move(self, from_square, to_square):
        # row, col = from_square.get_position()
        # to_row, to_col = to_square.get_position()
        # self.get_team()
        from_pos, col = from_square.get_position()
        to_pos, col = to_square.get_position()

        if self.operation(from_pos, to_pos) and abs(from_pos-to_pos) == 1:
            return True

        return False

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class Rook(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "rook"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class Bishop(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "bishop"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class Knight(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "knight"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class Queen(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "queen"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class King(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "king"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name


class NoPiece(ChessPiece):
    def __init__(self, chess_team) -> None:
        self._name = "none"
        super().__init__(chess_team)

    def move(self):
        return super().move()

    def eat(self):
        return super().eat()

    def get_name(self):
        return self._name

    def get_team(self):
        return self.team


CHESS_PIECE_ORDER = [
    Rook,
    Knight,
    Bishop,
    Queen,
    King,
    Bishop,
    Knight,
    Rook,
]
