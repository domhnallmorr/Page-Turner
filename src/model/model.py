import copy
import random
import string

from model import config_file_manager

class Model:
	def __init__(self):
		self.setup_variables()

	def setup_variables(self):
		self.config_data = config_file_manager.load_config_file(self)
		self.root_tabs = {}
		self.branch_tabs = {}
	
		if "session_data" in self.config_data.keys():
			self.last_session = copy.deepcopy(self.config_data["session_data"])
		else:
			self.last_session = None

		self.config_data["session_data"] = {}

	def gen_id(self):
		count = 0
		while True:
			characters = string.ascii_letters + string.digits
			new_id = ''.join(random.choice(characters) for i in range(8))
		
			count += 1
			
			if new_id not in self.root_tabs.keys() and new_id not in self.branch_tabs.keys():
				break
			elif count > 10_000:
				raise Exception("id not generated after 10,000 attempts")
				
		return new_id
	
	def add_new_root_tab(self, default_text="New Tab"):
		root_id = self.gen_id()
		
		self.root_tabs[root_id] = {"text": default_text, "branch_tabs": []}
		self.config_data["session_data"][root_id] = {"text": default_text, "branch_tabs": {}}
		
		config_file_manager.write_config_file(self)

		return root_id
	
	def add_new_branch_tab(self, root_id, default_text="New Branch Tab", default_pdf=None):
		branch_id = self.gen_id()

		branch_tab = BranchTab(self, root_id, branch_id, default_text, pdf=default_pdf)
		self.branch_tabs[branch_id] = branch_tab

		self.root_tabs[root_id]["branch_tabs"].append(branch_tab)

		self.config_data["session_data"][root_id]["branch_tabs"][branch_id] = {"text": self.branch_tabs[branch_id].text, "pdf": default_pdf}
		
		config_file_manager.write_config_file(self)
	
		return branch_id

	def delete_root_tab(self, root_id):
		self.root_tabs.pop(root_id)
		self.config_data["session_data"].pop(root_id)

		config_file_manager.write_config_file(self)

	def delete_branch_tab(self, root_id, branch_id, tab_index):
		self.root_tabs[root_id]["branch_tabs"].pop(tab_index)
		self.config_data["session_data"][root_id]["branch_tabs"].pop(branch_id)

		config_file_manager.write_config_file(self)

	def rename_root_tab(self, root_id, text):
		self.root_tabs[root_id]["text"] = text
		self.config_data["session_data"][root_id]["text"] = text
		config_file_manager.write_config_file(self)

	def rename_branch_tab(self, root_id, branch_id, text):
		self.branch_tabs[branch_id].text = text
		self.config_data["session_data"][root_id]["branch_tabs"][branch_id]["text"] = text
		config_file_manager.write_config_file(self)

class BranchTab:
	def __init__(self, model, root_id, branch_id, text, pdf=None):
		self.model = model
		self.root_id = root_id
		self.branch_id = branch_id
		self.pdf = pdf
		self.text = text

	def update_pdf(self, file_name):
		self.pdf = file_name
		self.model.config_data["session_data"][self.root_id]["branch_tabs"][self.branch_id]["pdf"] = self.pdf
		config_file_manager.write_config_file(self.model)
