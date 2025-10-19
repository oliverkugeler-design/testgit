import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def main():
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Hello World - PyQt6")

    # Add a label
    label = QLabel("Hello, World!")
    label.setStyleSheet("font-size: 24px; color: darkblue;")

    # Layout
    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    # Show window
    window.resize(300, 100)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
