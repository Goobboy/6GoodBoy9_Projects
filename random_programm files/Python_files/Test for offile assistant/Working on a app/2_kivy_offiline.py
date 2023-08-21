from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivymd.app import MDApp

Window.size = (400, 600)
minimum_size = (300,500)
Window.minimum_width, Window.minimum_height = minimum_size


class Myroot(BoxLayout):

    def __init__(self):
        super().__init__()


class the_Gridlayout(GridLayout):
    pass


class OfflineAssistantApp(MDApp):
    pass


OfflineAssistantApp().run()