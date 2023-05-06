import random
import string

class Model:
	def __init__(self):
		self.setup_variables()

	def setup_variables(self):
		self.root_tabs = {}
		self.branch_tabs = {}
	

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

		return root_id
	
	def add_new_branch_tab(self, root_id, default_text="New Branch Tab"):
		branch_id = self.gen_id()

		branch_tab = BranchTab(branch_id, default_text)
		self.branch_tabs[branch_id] = branch_tab

		self.root_tabs[root_id]["branch_tabs"].append(branch_tab)
		
		return branch_id

	def delete_root_tab(self, root_id):
		self.root_tabs.pop(root_id)

	def delete_branch_tab(self, root_id, branch_id):
		self.root_tabs[root_id]["branch_tabs"].pop(branch_id)

class BranchTab:
	def __init__(self, branch_id, text):
		self.branch_id = branch_id
		self.pdf = None
		self.text = text