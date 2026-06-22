from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont
)
from PyQt6.QtCore import Qt, QTimer


class ScanRing(QWidget):

    def __init__(self):
        super().__init__()

        self.angle1 = 0
        self.angle2 = 0
        self.glow = 0
        self.direction = 1
        self.percent = 99

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):

        self.angle1 += 1
        self.angle2 -= 2

        self.glow += self.direction

        if self.glow > 50:
            self.direction = -1

        if self.glow < 0:
            self.direction = 1

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        centerX = self.width() / 2
        centerY = self.height() / 2

        painter.translate(centerX, centerY)

        # ===== OUTER GLOW =====

        glowPen = QPen(
            QColor(
                176,
                38,
                255,
                60 + self.glow
            )
        )

        glowPen.setWidth(24)

        painter.setPen(glowPen)

        painter.drawEllipse(
            -170,
            -170,
            340,
            340
        )

        # ===== OUTER RING =====

        painter.save()

        painter.rotate(self.angle1)

        outerPen = QPen(
            QColor("#b026ff")
        )

        outerPen.setWidth(10)
        outerPen.setCapStyle(
            Qt.PenCapStyle.RoundCap
        )

        painter.setPen(outerPen)

        painter.drawArc(
            -160,
            -160,
            320,
            320,
            0,
            300 * 16
        )

        painter.restore()

        # ===== MIDDLE RING =====

        painter.save()

        painter.rotate(self.angle2)

        greenPen = QPen(
            QColor("#00ff88")
        )

        greenPen.setWidth(12)

        painter.setPen(greenPen)

        painter.drawArc(
            -130,
            -130,
            260,
            260,
            0,
            220 * 16
        )

        painter.restore()

        # ===== INNER CORE =====

        painter.setPen(Qt.PenStyle.NoPen)

        painter.setBrush(
            QColor(10, 10, 10)
        )

        painter.drawEllipse(
            -105,
            -105,
            210,
            210
        )

        # ===== INNER BORDER =====

        innerPen = QPen(
            QColor("#222222")
        )

        innerPen.setWidth(2)

        painter.setPen(innerPen)

        painter.drawEllipse(
            -105,
            -105,
            210,
            210
        )

        # ===== CENTER TEXT =====

        painter.setPen(
            QColor("#ffffff")
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                20,
                QFont.Weight.Bold
            )
        )

        painter.drawText(
            -80,
            -10,
            160,
            40,
            Qt.AlignmentFlag.AlignCenter,
            "SECURE"
        )

        painter.setPen(
            QColor("#00ff88")
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                28,
                QFont.Weight.Bold
            )
        )

        painter.drawText(
            -80,
            20,
            160,
            60,
            Qt.AlignmentFlag.AlignCenter,
            f"{self.percent}%"
        )