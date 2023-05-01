from PyQt6.QtWidgets import QTabWidget, QMenu, QTabBar
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt

from view import root_tab

class RootNoteBook(QTabWidget):
	def __init__(self, view):
		super().__init__()
		self.view = view
		self.root_tabs = {}
		
		self.setTabBar(QTabBar())
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.contextMenuEvent)

	def add_new_tab(self, root_id, default_text):
		self.root_tabs[root_id] = root_tab.RootTab(root_id, self.view)
		self.addTab(self.root_tabs[root_id], default_text)

	def contextMenuEvent(self, pos):
		self.tab_index = self.tabBar().tabAt(pos)
		self.root_id_selected = list(self.root_tabs.keys())[self.tab_index]

		context = QMenu(self)
		new_root_tab_action = context.addAction("New Root Tab")
		new_root_tab_action.triggered.connect(self.new_tab_action)

		edit_branch_tab_action = context.addAction("Rename Root Tab")
		edit_branch_tab_action.triggered.connect(self.rename_tab_action)

		context.exec(self.mapToGlobal(pos))

	def new_tab_action(self):
		self.view.controller.add_new_root_tab()

	def rename_tab_action(self):
		self.view.controller.rename_root_tab(self.root_id_selected)

	def rename_root_tab(self, root_id, text):
		self.setTabText(self.tab_index, text)

