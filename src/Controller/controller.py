from model import model
from view import view

class Controller:
	def __init__(self, mainapp):
		self.mainapp = mainapp
		self.model = model.Model()
		self.view = view.View(self)

		# Setup Default Root Tab
		self.add_new_root_tab()

	def add_new_root_tab(self, default_text="New Tab", default_branch_tab=True):
		root_id = self.model.add_new_root_tab(default_text=default_text)
		
		self.view.root_notebook.add_new_tab(root_id, default_text)

		# Add Default branch tab
		if default_branch_tab is True:
			self.add_new_branch_tab(root_id)

		return root_id
		
	def add_new_branch_tab(self, root_id, default_text="New Branch Tab", default_pdf=None):
		branch_id = self.model.add_new_branch_tab(root_id, default_text=default_text, default_pdf=default_pdf)

		self.view.root_notebook.root_tabs[root_id].add_new_branch_tab(branch_id, default_text, default_pdf)

	def rename_root_tab(self, root_id):
		default_text = self.model.root_tabs[root_id]["text"]
		text, ok = self.view.get_user_text("Rename Root Tab", default_text)

		if ok:
			self.model.rename_root_tab(root_id, text)
			self.view.root_notebook.rename_root_tab(root_id, text)

	def delete_root_tab(self, root_id, tab_index):
		self.model.delete_root_tab(root_id)
		self.view.root_notebook.delete_root_tab(root_id, tab_index)

	def delete_branch_tab(self, root_id, branch_id, tab_index):
		self.model.delete_branch_tab(root_id, branch_id, tab_index)
		self.view.root_notebook.root_tabs[root_id].delete_branch_tab(branch_id, tab_index)

	def rename_branch_tab(self, root_id, branch_id):
		default_text = self.model.branch_tabs[branch_id].text
		text, ok = self.view.get_user_text("Rename Branch Tab", default_text)

		if ok:
			self.model.rename_branch_tab(root_id, branch_id, text)
			self.view.root_notebook.root_tabs[root_id].rename_branch_tab(text)

	def load_last_session(self):
		# ASK USER TO CONFIRM

		# DELETE EXISTING TABS
		tabs = list(self.model.root_tabs.keys())
		for tab_index, root_id in enumerate(tabs):
			self.delete_root_tab(root_id, tab_index)


		# CREATE ROOT TAB
		for root_id in self.model.last_session.keys():
			default_text = self.model.last_session[root_id]["text"]
			new_root_id = self.add_new_root_tab(default_text=default_text, default_branch_tab=False)

			# CREATE THE BRANCH TABS
			for branch_id in self.model.last_session[root_id]["branch_tabs"].keys():
				default_text = self.model.last_session[root_id]["branch_tabs"][branch_id]["text"]
				default_pdf = self.model.last_session[root_id]["branch_tabs"][branch_id]["pdf"]

				self.add_new_branch_tab(new_root_id, default_text=default_text, default_pdf=default_pdf)

	def open_pdf(self, root_id, branch_id):
		file_name = self.view.root_notebook.root_tabs[root_id].branch_tabs[branch_id].select_pdf()

		if file_name:
			self.view.root_notebook.root_tabs[root_id].branch_tabs[branch_id].load_pdf(file_name)
			self.model.branch_tabs[branch_id].update_pdf(file_name)
