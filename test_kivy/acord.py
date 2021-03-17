from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem

class minha_lista(App):
	def build(self):
		lista = Accordion()
		
		item = AccordionItem(title = 'Amor', background_normal = 'cores.jpg', background_selected = 'um-video-super-legal-com-imagens-do-por-do-sol-muito-lindo.jpg')
		
		item.add_widget(Label(text = '''
Bom o que sinto as vezes, tenho medo de sentir, 
sera que eu sou a pessoa certa?, tenho  muitas insertezas, dizem que 
quando a gente gosta não que saber e que a pessoa pra si, mas eu 
agora não sei se só estou gostando será, eu mudei quero ter uma familia a pessoa 
que eu estou gostando ela tem seu receios. Não sei se isso é o certo, acredito que 
esse sentimento seja amor apaixonado tenho que esperar. Um dia tive uma crise de 
paixão logo outro dia me recuperei meio que não sentia mais que gosta, acredito 
que deva esperar.
		'''))
		
		
		item1 = AccordionItem(title = 'B')
		
		item2 = AccordionItem(title = 'C')
		
		item1.add_widget(Label(text = 'Pão'))
		item2.add_widget(Label(text = 'Oleo'))
		
		
		
		lista.add_widget(item2)
		lista.add_widget(item)
		lista.add_widget(item1)
		return lista
		


minha_lista().run()
