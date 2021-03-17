import contar
from kivy.app import App
from kivy.uix.label import Label

class inicio(App):
	def build(self):
	
		return Label(text = str(contar.conta(50, 80, 90)), font_size = 50)
		

inicio().run()

	


