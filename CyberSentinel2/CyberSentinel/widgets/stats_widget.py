from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QProgressBar
)

from PyQt6.QtCore import QTimer

from core.system_monitor import SystemMonitor


class StatCard(QFrame):

    def __init__(self, title):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background:#0b0b0b;
                border:1px solid #b026ff;
                border-radius:18px;
            }

            QLabel{
                color:white;
                background:transparent;
            }

            QProgressBar{
                border:none;
                background:#161616;
                border-radius:8px;
                text-align:center;
                color:white;
                min-height:16px;
            }

            QProgressBar::chunk{
                background:#00ff88;
                border-radius:8px;
            }
        """)

        layout = QVBoxLayout(self)

        self.titleLabel = QLabel(title)
        self.titleLabel.setStyleSheet("""
            font-size:13px;
            color:#888888;
        """)

        self.valueLabel = QLabel("0%")
        self.valueLabel.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:#00ff88;
        """)

        self.progress = QProgressBar()

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.valueLabel)
        layout.addWidget(self.progress)

    def setValue(self, value):

        value = int(value)

        self.valueLabel.setText(f"{value}%")
        self.progress.setValue(value)


class StatsWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.cpuCard = StatCard("CPU")
        self.ramCard = StatCard("RAM")
        self.diskCard = StatCard("DISK")

        layout.addWidget(self.cpuCard)
        layout.addWidget(self.ramCard)
        layout.addWidget(self.diskCard)

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.updateStats
        )

        self.timer.start(1000)

        self.updateStats()

    def updateStats(self):

        self.cpuCard.setValue(
            SystemMonitor.cpu()
        )

        self.ramCard.setValue(
            SystemMonitor.ram()
        )

        self.diskCard.setValue(
            SystemMonitor.disk()
        )