from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import screen_helper

Window.size = (350, 600)


class ToolBarApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        screen = Builder.load_string(screen_helper)
        return screen

    @staticmethod
    def navigation_draw():
        print("Navigation")


ToolBarApp().run()
