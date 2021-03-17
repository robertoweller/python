'''
Image mipmap
============
Difference between a mipmapped image and no mipmap image.
The lower image is normal, and the top image is mipmapped.
'''

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.label import Label
from os.path import join

class LabelMipmapTest(App):
    def build(self):
        s = ScatterPlane(scale=.5)
        l1 = Label(text ='55', font_size = 60, pos=(400, 100))
        l2 = Label(text='66', font_size = 60, pos=(400, 356))
        s.add_widget(l1)
        s.add_widget(l2)
        return s

if __name__ == '__main__':
    LabelMipmapTest().run()
