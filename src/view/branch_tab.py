import random
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QTreeView, QTabWidget, QLabel, QWidget, QPushButton, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView 

class BranchTab(QWidget):
	def __init__(self, root_id, view, branch_id, default_pdf):
		super().__init__()
		self.root_id = root_id
		self.view = view
		self.branch_id = branch_id
		self.default_pdf = default_pdf

		self.setup_widgets()
		self.setup_layouts()
		

	def setup_widgets(self):
		if self.default_pdf is None:
			self.button = QPushButton("Open PDF", self)
		else:
			self.button = QPushButton(f"Open {self.default_pdf}", self)
		self.button.clicked.connect(self.open_pdf)
		# self.label = QLabel(f"This is tab {random.randint(1, 100)}")
		self.webView = QWebEngineView()
		self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
		self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
		# self.setCentralWidget(self.webView)

	def setup_layouts(self):
		tab_content_layout = QVBoxLayout()
		tab_content_layout.addWidget(self.button)
		tab_content_layout.addWidget(self.webView)

		self.setLayout(tab_content_layout)

	def open_pdf(self):
		if self.default_pdf is None:
			self.view.controller.open_pdf(self.root_id, self.branch_id)
		else:
			self.load_pdf(self.default_pdf)

	def select_pdf(self):
		file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")

		return file_name
		# if file_name:
		# 	self.load_pdf(file_name)

	def load_pdf(self, file_name):
		self.webView.setUrl(QUrl.fromLocalFile(file_name))