from PyQt6.QtWidgets import QTabWidget, QMenu
from PyQt6.QtGui import QIcon, QAction


from view import root_tab

class RootNoteBook(QTabWidget):
	def __init__(self, view):
		super().__init__()
		self.view = view
		self.root_tabs = {}
		

	def add_new_tab(self, root_id, default_text):
		self.root_tabs[root_id] = root_tab.RootTab(root_id, self.view)
		self.addTab(self.root_tabs[root_id], default_text)

	def contextMenuEvent(self, e):
		context = QMenu(self)
		new_root_tab_action = context.addAction("New Root Tab")
		new_root_tab_action.triggered.connect(self.new_tab_action)

		context.exec(e.globalPos())

	def new_tab_action(self):
		self.view.controller.add_new_root_tab()