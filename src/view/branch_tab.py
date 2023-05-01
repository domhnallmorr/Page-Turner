import random
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QTreeView, QTabWidget, QLabel, QWidget, QPushButton, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView 

class BranchTab(QWidget):
	def __init__(self):
		super().__init__()

		self.setup_widgets()
		self.setup_layouts()
		

	def setup_widgets(self):
		self.button = QPushButton("Open PDF", self)
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
		# options = QFileDialog.options()
		# options |= QFileDialog.DontUseNativeDialog
		file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")

		if file_name:
			self.load_pdf(file_name)

	def load_pdf(self, file_name):
		self.webView.setUrl(QUrl.fromLocalFile(file_name))