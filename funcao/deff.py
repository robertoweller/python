from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

class Bora(ScrollView):
	pass


class Inicio(App):
	def build(self):

		return Bora()


if __name__ == '__main__':
	Inicio().run()
