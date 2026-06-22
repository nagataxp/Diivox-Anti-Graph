from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QGridLayout
)

from widgets.scan_ring import ScanRing
from widgets.stats_widget import StatsWidget
from widgets.activity_feed import ActivityFeed


class DashboardCard(QFrame):

    def __init__(self, title, value):
        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background:#0b0b0b;
                border:1px solid #b026ff;
                border-radius:18px;
            }

            QLabel{
                color:white;
            }
        """)

        layout = QVBoxLayout(self)

        titleLabel = QLabel(title)
        titleLabel.setStyleSheet("""
            font-size:14px;
            color:#999999;
        """)

        valueLabel = QLabel(value)
        valueLabel.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            color:#00ff88;
        """)

        layout.addWidget(titleLabel)
        layout.addWidget(valueLabel)


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget{
                background:#050505;
            }
        """)

        mainLayout = QHBoxLayout(self)

        # ===== CENTER =====

        centerLayout = QVBoxLayout()

        title = QLabel("CYBER SENTINEL")
        title.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
            color:#b026ff;
        """)

        subtitle = QLabel("ADVANCED SECURITY DASHBOARD")
        subtitle.setStyleSheet("""
            color:#888888;
            font-size:14px;
        """)

        self.scanRing = ScanRing()
        self.scanRing.setMinimumSize(550, 550)

        centerLayout.addWidget(title)
        centerLayout.addWidget(subtitle)
        centerLayout.addSpacing(10)
        centerLayout.addWidget(self.scanRing)

        # ===== RIGHT PANEL =====

        rightLayout = QVBoxLayout()

        statusCard = DashboardCard(
            "System Status",
            "SECURE"
        )

        threatsCard = DashboardCard(
            "Threats Blocked",
            "127"
        )

        scansCard = DashboardCard(
            "Scans Today",
            "43"
        )

        stats = StatsWidget()

        feed = ActivityFeed()

        rightLayout.addWidget(statusCard)
        rightLayout.addWidget(threatsCard)
        rightLayout.addWidget(scansCard)
        rightLayout.addWidget(stats)
        rightLayout.addWidget(feed)

        # ===== TOP STATS =====

        topStats = QGridLayout()

        card1 = DashboardCard(
            "Firewall",
            "ACTIVE"
        )

        card2 = DashboardCard(
            "Network",
            "SAFE"
        )

        card3 = DashboardCard(
            "Database",
            "UPDATED"
        )

        topStats.addWidget(card1, 0, 0)
        topStats.addWidget(card2, 0, 1)
        topStats.addWidget(card3, 0, 2)

        contentLayout = QVBoxLayout()
        contentLayout.addLayout(topStats)
        contentLayout.addLayout(centerLayout)

        mainLayout.addLayout(contentLayout, 4)
        mainLayout.addLayout(rightLayout, 1)