import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication(sys.argv)
    
    # Create a window
    window = QWidget()
    window.setWindowTitle("Hello PyQt !")
    window.setGeometry(100, 100, 300, 100)  # x, y, width, height
    
    # Add a label to the window
    label = QLabel("Hello, World! 123r", parent=window)
    label.move(100, 40)
    
    # Show window
    window.show()
    
    # Enter the Qt event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
