from view import view

class Controller:
	def __init__(self, mainapp):
		self.mainapp = mainapp
		self.view = view.View(self)
