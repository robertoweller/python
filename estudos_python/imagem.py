from kivy.uix.image import Image
from kivy.app import App
from kivy.loader import Loader

class buscaNet(App):
	def hcarregar(self, carregar):
		if carregar.image.texture:
			self.imagem.texture = carregar.image.texture
			
	def build(self):
		iimagem = Loader.image('http://www.topmba.com.br/wp-content/uploads/2013/06/girl-backpack-thinking-sunset-field-fence-moment-field-reeds-hd-fullscreen.jpg')
		iimagem.bind(on_load = self.hcarregar)
		self.imagem = Image()
		return self.imagem


		
buscaNet().run()
