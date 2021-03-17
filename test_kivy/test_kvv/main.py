from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class casa(FloatLayout):
	pass
	
class Test(App):
	def build(self):
	
		return casa()
	
Test().run()
