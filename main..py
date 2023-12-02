import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from random import randint

class TetrisBlock(Widget):
    pass

class TetrisApp(App):
    def build(self):
        layout = GridLayout(cols=10, rows=20)
        
        # Створюємо ігрове поле
        for i in range(200):
            btn = TetrisBlock()
            layout.add_widget(btn)
            
        return layout

if __name__ == "__main__":
    TetrisApp().run()