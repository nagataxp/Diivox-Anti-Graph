from PyQt6.QtWidgets import (
    QListWidget,
    QListWidgetItem
)

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor


class ActivityFeed(QListWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QListWidget{
                background:#0b0b0b;
                border:1px solid #b026ff;
                border-radius:18px;
                color:white;
                padding:10px;
                font-size:13px;
            }

            QListWidget::item{
                padding:8px;
                border-bottom:1px solid #1a1a1a;
            }
        """)

        self.setMinimumHeight(260)

        self.logs = [
            ("SUCCESS", "Firewall initialized"),
            ("SUCCESS", "Security engine loaded"),
            ("SUCCESS", "Network secured"),
            ("INFO", "Database synchronized"),
            ("INFO", "System scan started"),
            ("SUCCESS", "No threats detected"),
            ("INFO", "Memory analysis completed"),
            ("SUCCESS", "Protection enabled"),
            ("WARNING", "Suspicious connection blocked"),
            ("INFO", "Background scan running")
        ]

        self.index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.addLog)
        self.timer.start(2500)

        for _ in range(4):
            self.addLog()

    def addLog(self):

        level, message = self.logs[self.index]

        if level == "SUCCESS":
            prefix = "🟢"
            color = QColor("#00ff88")

        elif level == "WARNING":
            prefix = "🟠"
            color = QColor("#ffb347")

        else:
            prefix = "🔵"
            color = QColor("#66ccff")

        item = QListWidgetItem(
            f"{prefix}  {message}"
        )

        item.setForeground(color)

        self.insertItem(0, item)

        if self.count() > 25:
            self.takeItem(25)

        self.index += 1

        if self.index >= len(self.logs):
            self.index = 0