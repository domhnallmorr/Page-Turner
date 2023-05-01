from PyQt6.QtWidgets import QLabel, QTabWidget, QWidget, QVBoxLayout, QMenu, QTabBar
from PyQt6.QtCore import Qt
from view import branch_tab

class RootTab(QWidget):
	def __init__(self, root_id, view):
		super().__init__()
		self.root_id = root_id
		self.view = view

		self.branch_tabs = {}
		self.setup_widgets()
		self.setup_layouts()


	def setup_widgets(self):
		self.label = QLabel("dfsdf")

		self.notebook = QTabWidget()
		self.notebook.setTabBar(QTabBar())
		self.notebook.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.notebook.customContextMenuRequested.connect(self.contextMenuEvent)

	def setup_layouts(self):
		self.tab_content_layout = QVBoxLayout()
		self.tab_content_layout.addWidget(self.notebook)

		self.setLayout(self.tab_content_layout)

		# tab_content_widget = QWidget()

        # # create a label to add to the new tab
		# label = QLabel('This is tab 1')
		# tab_content_layout = QVBoxLayout()
		# tab_content_layout.addWidget(label)

		# tab_content_widget.setLayout(tab_content_layout)

        # # add the tab content widget to the tab widget
		# self.notebook.addTab(tab_content_widget, 'Branch Tab')

	def contextMenuEvent(self, pos):
		self.tab_index = self.notebook.tabBar().tabAt(pos)
		self.branch_id_selected = list(self.branch_tabs.keys())[self.tab_index]

		context = QMenu(self)
		new_branch_tab_action = context.addAction("New Branch Tab")
		new_branch_tab_action.triggered.connect(self.new_tab_action)

		edit_branch_tab_action = context.addAction("Rename Branch Tab")
		edit_branch_tab_action.triggered.connect(self.rename_tab_action)
		

		context.exec(self.notebook.mapToGlobal(pos))

	def new_tab_action(self):
		self.view.controller.add_new_branch_tab(self.root_id)

	def add_new_branch_tab(self, branch_id):
		self.branch_tabs[branch_id] = branch_tab.BranchTab()
		self.notebook.addTab(self.branch_tabs[branch_id], 'Branch Tab')

	def rename_tab_action(self):
		self.view.controller.rename_branch_tab(self.root_id, self.branch_id_selected)

	def rename_branch_tab(self, text):
		self.notebook.setTabText(self.tab_index, text)