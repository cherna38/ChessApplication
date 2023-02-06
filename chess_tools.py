from PySide6.QtGui import QImage, QPixmap

PAWN_ROW = [1, 6]
ELITE_PIECES = [0, 7]


def load_svg(team_color: str, type: str) -> QPixmap:
    file_name = team_color+"_"+type+".svg"
    file_name = "resources/"+file_name
    img = QPixmap()
    img = img.fromImage(QImage(file_name))
    return img
