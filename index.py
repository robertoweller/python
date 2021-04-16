import os
from datetime import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class Relogio(App):
    def atualiza_horas(self, h):

        self.horas = datetime.now()
        # Corta o tempo
        self.agora = str(self.horas)[10:16]
        print(f"Horas atualizada > {self.agora}")
        self.lb.text = f"São \n  Francisco \n     do Sul \n     {self.agora}"

    def build(self):
        self.horas = datetime.now()
        # Corta o tempo
        self.agora = str(self.horas)[10:16]
        # Vou acessar ele atraves do função atualiza
        self.bx = BoxLayout()
        self.lb = Label(text=f"{self.agora}", font_size="50dp")
        # Vai ser acessado pela função atualiza
        self.bx.add_widget(self.lb)

        # Chama a função à cada vez
        ck = Clock.schedule_interval(self.atualiza_horas, 1)

        return self.bx


Relogio().run()


tempo = datetime.now()

tempo_a = str(tempo)[10:16]

print(f"{tempo_a}")


comandos = os.system('shutdown ')
