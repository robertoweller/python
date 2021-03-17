from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem

class tela(App):
	def build(self):
		lista = Accordion()
		
		for x in range(7):
			item = AccordionItem(title = 'Item{0}'.format(x+1))
			item.add_widget(Label(text = 
			'''Além do horizonte deve ter
Algum lugar bonito pra viver em paz
Onde eu possa encontrar a natureza
Alegria e felicidade com certeza'''))
			lista.add_widget(item)
		
		return lista
		
tela().run()
