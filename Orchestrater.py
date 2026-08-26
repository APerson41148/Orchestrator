import platform
import subprocess
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QHBoxLayout,QLabel,QPushButton,QVBoxLayout,QWidget

current_os = platform.system().lower()


def on_click(app_name, url):
    if app_name == "Orchestrator":
        sys.exit(0)
    if current_os == "darwin":  # macOS
        subprocess.run(["open", "-a", app_name, url])
    elif current_os == "windows":  # Windows
        subprocess.run(["cmd", "/c", "start", "chrome", url], shell=True)
    elif current_os == "linux":  # Linux
        subprocess.run(["google-chrome", url])


# 1. Initialize Application
app = QApplication(sys.argv)

# 2. Create the main window
window = QWidget()
window.setWindowTitle("Orchestrator")

# 3. Create Widgets
label = QLabel("Hello, friend!")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")

gmail_button = QPushButton("Gmail")
aops_button = QPushButton("AoPS")
quit_button = QPushButton("Quit")

# Stylesheet for Web/Action buttons
button_style = """
    QPushButton {
        background-color: #0763f7;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        border: 2px solid #024abf;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #2273f5;
        cursor: pointer;
    }
    QPushButton:pressed {
        background-color: #bcd3f7;
    }
"""

quit_style = """
    QPushButton {
        background-color: #444;
        color: white;
        font-size: 14px;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    QPushButton:hover {
        background-color: #666;
    }
    QPushButton:pressed {
        background-color: #222;
    }
"""

gmail_button.setStyleSheet(button_style)
aops_button.setStyleSheet(button_style)
quit_button.setStyleSheet(quit_style)

# 4. Connect Signals
gmail_button.clicked.connect(
    lambda: on_click(
        "Google Chrome", "https://mail.google.com/mail/u/0/#inbox"
    )
)
aops_button.clicked.connect(
    lambda: on_click("Google Chrome", "https://artofproblemsolving.com/")
)
quit_button.clicked.connect(lambda: on_click("Orchestrator", None))

# 5. Layouts
# A. Horizontal layout for the two main action buttons (Side-by-side)
button_row = QHBoxLayout()
button_row.setSpacing(15)  # Space between Gmail and AoPS
button_row.addWidget(gmail_button)
button_row.addWidget(aops_button)

# B. Main vertical layout
layout = QVBoxLayout()
layout.setSpacing(15)
layout.addWidget(label)
layout.addLayout(button_row)  # Add the side-by-side button row
layout.addWidget(quit_button)  # Quit button underneath

window.setLayout(layout)

# 6. Show Window
window.show()

# 7. Start event loop
sys.exit(app.exec())