from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from widgets.stats_widget import StatsWidget


class PerformancePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel(
            "SYSTEM PERFORMANCE"
        )

        title.setStyleSheet("""
            color:#b026ff;
            font-size:32px;
            font-weight:bold;
        """)

        stats = StatsWidget()

        layout.addWidget(title)
        layout.addWidget(stats)