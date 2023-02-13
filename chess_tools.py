from PySide6.QtGui import QImage, QPixmap

PAWN_ROW = [1, 6]
ELITE_PIECES = [0, 7]
CHESS_BOARD_LENGTH = 8
CHESS_BOARD_WIDTH = 8

TEAM_BLACK = "black"
TEAM_WHITE = "white"

TOP_OF_BOARD = 0  # "top"
BOTTOM_OF_BOARD = CHESS_BOARD_LENGTH-1  # "bottom"


def load_svg(team_color: str, type: str) -> QPixmap:
    file_name = team_color+"_"+type+".svg"
    file_name = "resources/"+file_name
    img = QPixmap()
    img = img.fromImage(QImage(file_name))
    return img
