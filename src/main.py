import sys
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar

from controller import controller

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.version = "0.3.0"
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
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')

		# LOAD LAST SESSION
		loadsessionAction = QAction("&Load Last Session", self)
		loadsessionAction.triggered.connect(self.controller.load_last_session)
		fileMenu.addAction(loadsessionAction)
		
	
if __name__ == '__main__':
	app = QApplication(sys.argv)

	ex = App()
	sys.exit(app.exec())

