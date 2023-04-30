from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QTreeView, QTabWidget, QLabel, QWidget

from view import branch_tab, root_notebook

class View:
	def __init__(self, controller):
		self.controller = controller
		self.mainapp = controller.mainapp

		self.setup_widgets()
		self.setup_ui()
		# self.add_new_branch_tab()

	def setup_widgets(self):
		self.root_notebook = root_notebook.RootNoteBook(self)

	def setup_ui(self):
        # create a vertical layout
		layout = QHBoxLayout()

        # create a tree view and add it to the layout
		tree_view = QTreeView()
		layout.addWidget(tree_view)

        # create a tab widget and add it to the layout
		# self.tab_widget = QTabWidget()
		layout.addWidget(self.root_notebook)

		layout.setStretchFactor(tree_view, 2)
		layout.setStretchFactor(self.root_notebook, 8)

		# create a widget to hold the content of the new tab
		tab_content_widget = QWidget()

		# create a label to add to the new tab
		label = QLabel('This is tab 1')
		tab_content_layout = QVBoxLayout()
		tab_content_layout.addWidget(label)

		# set the layout of the tab content widget to the tab content layout
		tab_content_widget.setLayout(tab_content_layout)

		# add the tab content widget to the tab widget
		self.root_notebook.addTab(tab_content_widget, 'Tab 1')

		# create a central widget to hold the main layout
		central_widget = QWidget()

		# set the main layout to the vertical layout
		central_widget.setLayout(layout)

		# set the central widget of the main window to the central widget
		self.mainapp.setCentralWidget(central_widget)

	def add_new_branch_tab(self):
		# create a widget to hold the content of the new tab
		tab_content_widget = branch_tab.BranchTab()

		# create a label to add to the new tab
		label = QLabel('Important Content')
		tab_content_layout = QVBoxLayout()
		tab_content_layout.addWidget(label)

		# set the layout of the tab content widget to the tab content layout
		tab_content_widget.setLayout(tab_content_layout)

		# add the tab content widget to the tab widget
		self.tab_widget.addTab(tab_content_widget, 'New Tab')