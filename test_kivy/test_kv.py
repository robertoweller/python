from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from time import sleep
#from pyautogui import click

#Altera tamanho da janela para 390px de largura e 110px de altura
Window.size = (390, 110)

# Deixar teste com kv deixa para depois
x = Builder.load_string('''
BoxLayout:
	Button:
		font_size: 20
		text: 'Tempo do clique>>'
	TextInput:
		multiline: False
		font_size: 30
		text: '3.0'
''')

class aplicativo(App):
	def printa(self, sl, vv):
		self.tempo = float(vv)
		
	def printaa(self, escreve):
		
		self.tempo = float(self.tempo)
		
		print(self.ck.clock.schedule_interval)
#		click()
		
	def build(self):
		self.tempo = 3.0
		self.ck = Clock.schedule_interval(self.printaa, 3.0)
		
		#revisar como usar kv para não precisar esse codigo
		tx = TextInput(text = '3.0',multiline = False)
		tx.bind(text = self.printa)
		
		
		
		
		return tx
		
aplicativo().run()
	
