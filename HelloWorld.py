import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def main():
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Hello PyQt !")
    window.setGeometry(100, 100, 300, 100)  # x, y, width, height
    
    # Add a label to the window
    label = QLabel("Hello, World!", parent=window)
    label.move(100, 40)
    
    # Show window
    window.resize(300, 100)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
