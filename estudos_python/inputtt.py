from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
 
class programa(App):
	def build(self):
		self.box = BoxLayout(orientation='horizontal', spacing=20)
		self.txt = TextInput(hint_text='Clique aqui')
		self.btn = Button(text = 'Clique', on_press = self.texto)
		self.box.add_widget(self.txt)
 
		self.box.add_widget(self.btn)
		return self.box
	def texto(self, escreve):
		print(self.txt.text)
		

		
programa().run()
