from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import sys

class tarefas(BoxLayout):
	def __init__(self, **arg): # **arg carrega tudo corretamente
		super().__init__(**arg)
		
		self.add_widget(Button(text = 'Anotar', font_size = 25, on_release = self.anotar)) 
		self.add_widget(Button(text = 'Cronometro', font_size = 25, on_release = self.crono)) 
				 
		
	def anotar(self, nota):
				
		nota.text = 'Ainda não esta pronto esse'
		
	def crono(self, cronometrar):
		
		carrega()
	
class carrega():
	def __init__(self, **a):
		
		import cronometro_com_botao	
		
class Programador(App):
	def build(self):
		return tarefas(orientation = 'horizontal')
	
Programador().run()
