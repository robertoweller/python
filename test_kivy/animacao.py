from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation

class Animar(App):
	def build(self):
		# Defino quantos pixels vai se mexer para eixo X e eixo Y
		ani = Animation(x=-220, y = 200, duration=2.) + Animation(x = -220, y = -200, duration=2.)
		
		ani.repeat = True
		# Label vem com posição posição inicial no meio
		lb = Label(
			text = '[u][color=ff9933]Teste[/color][/u]', 
			font_size = 30, 
			markup = True
			)
				
		ini = ani.start(lb)
		ani.repeat = False
		return lb
	
		
		
Animar().run()
