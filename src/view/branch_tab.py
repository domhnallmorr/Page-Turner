import random
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QTreeView, QTabWidget, QLabel, QWidget

class BranchTab(QWidget):
	def __init__(self):
		super().__init__()

		self.setup_widgets()
		self.setup_layouts()

	def setup_widgets(self):
		self.label = QLabel(f"This is tab {random.randint(1, 100)}")

	def setup_layouts(self):
		tab_content_layout = QVBoxLayout()
		tab_content_layout.addWidget(self.label)

		self.setLayout(tab_content_layout)