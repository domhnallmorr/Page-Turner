import json
import os

def write_config_file(model, startup=False):
	save_dict = {}

	save_dict["session_data"] = model.config_data["session_data"]
	
	with open("page_turner_config.json", "w") as outfile:
		json.dump(save_dict, outfile, indent=4)

def load_config_file(model):

	if not os.path.isfile("page_turner_config.json"):
		generate_default_config_file()
		
	with open("page_turner_config.json") as f:
		data = json.load(f)
		
	return data

def generate_default_config_file():
	
	save_dict = {}
	
	with open('page_turner_config.json', 'w') as outfile:
		json.dump(save_dict, outfile, indent=4)

