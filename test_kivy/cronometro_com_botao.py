from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (390, 110)

class Teste(App):
	def build(self):
		bx = FloatLayout()
		bt_play = Button(
			font_size = 20,
			text= '>', 
			size_hint = (.5, .25),
			pos = (5, 20),
			on_release = self.clica
			)
		bt_volta = Button(
			font_size = 20,
			text= '[color=ff9933]<[/color]', 
			size_hint = (.5, .25),
			pos = (200, 20),
			on_release = self.volta,
			markup = True
			)
		self.lb = Label(
			text = 'Cronometro',
			size_hint = (.5, .15),
			pos = (100, 70),
			font_size = 30
			)	
		self.x = 0
		self.y = ''
		self.segundos = 0
		self.ss = '0'
		self.minutos = 0
		self.mm = '0'
		self.horas = 0
		self.hh = '0'	
		
		# Cara que chama a função e deixa em luping
		ck = Clock.schedule_interval(self.tempo, 1)
		
		bx.add_widget(bt_volta)
		bx.add_widget(bt_play)
		bx.add_widget(self.lb)
		
		return bx
	
	def volta(self, volta):
		
		self.segundos = 0
		self.minutos = 0
		self.horas = 0
		self.lb.text = '0{0}:0{1}:0{2}'.format(self.horas, self.minutos, self.segundos)
		
	def clica(self, play):
		
		self.x += 1
		if self.x == 1:
			self.y = '|-|'
		if self.x == 2:
			self.x = 0
			self.y = '>'
		play.text = str(self.y)
	# Quando o relogio tiver rodando essa é a função que está sendo chamada!		
	def tempo(self, tempo):
		if self.x == 1:
			if self.segundos > 9:
				self.ss = ''
			if self.segundos > 59:
				self.minutos += 1
				self.segundos = 0
			if self.segundos <= 9:
				self.ss = '0'
			if self.minutos > 9:
				self.mm = ''
			if self.minutos > 59:
				self.horas += 1
				self.minutos = 0
			if self.minutos <= 9:
				self.mm = '0'
			if self.horas > 9:
				self.hh = ''
			if self.horas > 59:
				self.horas = 0
			if self. horas <= 9:
				self.hh = '0'
			
			self.lb.text = f'{self.hh}{self.horas}:{self.mm}{self.minutos}:{self.ss}{self.segundos}'
			if self.lb.text == '00:10:00':
				print('Deu, a carne!')
			self.segundos += 1
	
		
		
Teste().run()
