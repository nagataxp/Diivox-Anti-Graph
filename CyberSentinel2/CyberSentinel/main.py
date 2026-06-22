import sys

from PyQt6.QtWidgets import QApplication

from qfluentwidgets import (
    FluentWindow,
    FluentIcon,
    NavigationItemPosition
)

from ui.dashboard_page import DashboardPage
from ui.scanner_page import ScannerPage
from ui.activity_page import ActivityPage
from ui.performance_page import PerformancePage
from ui.settings_page import SettingsPage


class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()

        self.resize(1700, 950)

        self.setWindowTitle(
            "Cyber Sentinel Security Suite"
        )

        self.initNavigation()

    def initNavigation(self):

        self.dashboardPage = DashboardPage()
        self.scannerPage = ScannerPage()
        self.activityPage = ActivityPage()
        self.performancePage = PerformancePage()
        self.settingsPage = SettingsPage()

        self.addSubInterface(
            self.dashboardPage,
            FluentIcon.HOME,
            "Dashboard"
        )

        self.addSubInterface(
            self.scannerPage,
            FluentIcon.SEARCH,
            "Scanner"
        )

        self.addSubInterface(
            self.activityPage,
            FluentIcon.HISTORY,
            "Activity"
        )

        self.addSubInterface(
            self.performancePage,
            FluentIcon.SPEED_HIGH,
            "Performance"
        )

        self.navigationInterface.addSeparator()

        self.addSubInterface(
            self.settingsPage,
            FluentIcon.SETTING,
            "Settings",
            NavigationItemPosition.BOTTOM
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    try:
        with open(
            "styles/cyber_theme.qss",
            "r",
            encoding="utf-8"
        ) as f:
            app.setStyleSheet(f.read())
    except:
        pass

    window = MainWindow()
    window.show()

    sys.exit(app.exec())