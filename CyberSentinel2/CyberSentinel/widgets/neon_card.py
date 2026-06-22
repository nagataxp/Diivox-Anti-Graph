from PyQt6.QtWidgets import QFrame
from PyQt6.QtGraphicsEffects import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor


class NeonCard(QFrame):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background:#0c0c0c;
                border:1px solid #b026ff;
                border-radius:18px;
            }
        """)

        glow = QGraphicsDropShadowEffect()

        glow.setBlurRadius(40)
        glow.setColor(QColor("#b026ff"))
        glow.setOffset(0)

        self.setGraphicsEffect(glow)