from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.gesture import Gesture, GestureDatabase

class janela(FloatLayout):
	def __init__(self, *args, **kwargs):
		super(GestureBoard, self).__init__()


class jogar(App):
	def build(self):
		return janela()

