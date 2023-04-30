from model import model
from view import view

class Controller:
	def __init__(self, mainapp):
		self.mainapp = mainapp
		self.model = model.Model()
		self.view = view.View(self)

		# Setup Default Root Tab
		self.add_new_root_tab()

	def add_new_root_tab(self, default_text="New Tab"):
		root_id = self.model.add_new_root_tab()

		self.view.root_notebook.add_new_tab(root_id, default_text)
