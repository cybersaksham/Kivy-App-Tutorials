from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from helpers import list_helper, list_helper_advanced


class OneLineListApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper_advanced)
        return screen

    def on_start(self):
        for i in range(15):
            item = OneLineListItem(text=f"Item {i + 1}")
            self.root.ids.container.add_widget(item)


OneLineListApp().run()
