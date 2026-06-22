from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QCheckBox
)


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel(
            "SETTINGS"
        )

        title.setStyleSheet("""
            color:#b026ff;
            font-size:32px;
            font-weight:bold;
        """)

        darkMode = QCheckBox(
            "Enable Dark Mode"
        )

        startup = QCheckBox(
            "Launch On Startup"
        )

        rpc = QCheckBox(
            "Enable Discord RPC"
        )

        layout.addWidget(title)
        layout.addWidget(darkMode)
        layout.addWidget(startup)
        layout.addWidget(rpc)