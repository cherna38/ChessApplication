from enum import Enum, auto

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