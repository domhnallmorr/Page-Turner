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

		# Add Default branch tab
		self.add_new_branch_tab(root_id)

	def add_new_branch_tab(self, root_id):
		branch_id = self.model.add_new_branch_tab(root_id)

		self.view.root_notebook.root_tabs[root_id].add_new_branch_tab(branch_id)

	def rename_root_tab(self, root_id):
		default_text = self.model.root_tabs[root_id]["text"]
		text, ok = self.view.get_user_text("Rename Root Tab", default_text)

		if ok:
			self.model.root_tabs[root_id]["text"] = text
			self.view.root_notebook.rename_root_tab(root_id, text)

	def delete_root_tab(self, root_id, tab_index):
		self.model.delete_root_tab(root_id)
		self.view.root_notebook.delete_root_tab(tab_index)

	def delete_branch_tab(self, root_id, branch_id, tab_index):
		self.model.delete_branch_tab(root_id, tab_index)
		self.view.root_notebook.root_tabs[root_id].delete_branch_tab(tab_index)

	def rename_branch_tab(self, root_id, branch_id):
		default_text = self.model.branch_tabs[branch_id].text
		text, ok = self.view.get_user_text("Rename Branch Tab", default_text)

		if ok:
			self.model.branch_tabs[branch_id].text = text
			self.view.root_notebook.root_tabs[root_id].rename_branch_tab(text)
