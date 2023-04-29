import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from controller import controller

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.version = "0.0.1"
		self.title = f"Page Turner {self.version}"
		self.left = 100
		self.top = 100
		self.width = 640
		self.height = 480
		
        
		self.controller = controller.Controller(self)
		self.initUI()
		self.showMaximized()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

