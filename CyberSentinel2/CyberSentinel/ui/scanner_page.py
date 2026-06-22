from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QProgressBar
)

from PyQt6.QtCore import Qt, QTimer

from widgets.scan_ring import ScanRing


class InfoCard(QFrame):

    def __init__(self, title):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background:#0b0b0b;
                border:1px solid #b026ff;
                border-radius:18px;
            }
        """)

        layout = QVBoxLayout(self)

        self.titleLabel = QLabel(title)
        self.titleLabel.setStyleSheet("""
            color:#888;
            font-size:13px;
        """)

        self.valueLabel = QLabel("0")
        self.valueLabel.setStyleSheet("""
            color:#00ff88;
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.valueLabel)


class ScannerPage(QWidget):

    def __init__(self):
        super().__init__()

        self.filesScanned = 0
        self.threatsFound = 0

        mainLayout = QVBoxLayout(self)

        title = QLabel("ADVANCED SECURITY SCANNER")

        title.setStyleSheet("""
            color:#b026ff;
            font-size:32px;
            font-weight:bold;
        """)

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.ring = ScanRing()
        self.ring.setMinimumSize(550, 550)

        self.statusLabel = QLabel(
            "READY TO SCAN"
        )

        self.statusLabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.statusLabel.setStyleSheet("""
            color:#00ff88;
            font-size:20px;
            font-weight:bold;
        """)

        cardsLayout = QHBoxLayout()

        self.filesCard = InfoCard(
            "FILES SCANNED"
        )

        self.threatCard = InfoCard(
            "THREATS FOUND"
        )

        self.speedCard = InfoCard(
            "SCAN SPEED"
        )

        cardsLayout.addWidget(
            self.filesCard
        )

        cardsLayout.addWidget(
            self.threatCard
        )

        cardsLayout.addWidget(
            self.speedCard
        )

        self.progress = QProgressBar()

        self.progress.setStyleSheet("""
            QProgressBar{
                background:#111;
                border:1px solid #b026ff;
                border-radius:10px;
                color:white;
                text-align:center;
                height:30px;
            }

            QProgressBar::chunk{
                background:#00ff88;
                border-radius:10px;
            }
        """)

        self.scanButton = QPushButton(
            "START SECURITY SCAN"
        )

        self.scanButton.setStyleSheet("""
            QPushButton{
                background:#b026ff;
                color:white;
                border:none;
                border-radius:18px;
                padding:16px;
                font-size:18px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#d14cff;
            }
        """)

        self.scanButton.clicked.connect(
            self.startScan
        )

        mainLayout.addWidget(title)
        mainLayout.addWidget(self.ring)
        mainLayout.addWidget(self.statusLabel)
        mainLayout.addLayout(cardsLayout)
        mainLayout.addWidget(self.progress)
        mainLayout.addWidget(self.scanButton)

        self.timer = QTimer()
        self.timer.timeout.connect(
            self.updateScan
        )

    def startScan(self):

        self.filesScanned = 0
        self.threatsFound = 0

        self.progress.setValue(0)

        self.statusLabel.setText(
            "SCANNING..."
        )

        self.scanButton.setEnabled(False)

        self.timer.start(40)

    def updateScan(self):

        value = self.progress.value()

        if value >= 100:

            self.timer.stop()

            self.statusLabel.setText(
                "SYSTEM SECURE"
            )

            self.scanButton.setEnabled(True)

            return

        value += 1

        self.progress.setValue(value)

        self.filesScanned += 57

        self.filesCard.valueLabel.setText(
            str(self.filesScanned)
        )

        self.threatCard.valueLabel.setText(
            str(self.threatsFound)
        )

        self.speedCard.valueLabel.setText(
            f"{250 + value} MB/s"
        )