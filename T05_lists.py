"""
Flow to make lists:
    OneLineListItem => MDList => ScrollView => Screen
"""

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivy.uix.scrollview import ScrollView


class OneLineListApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        for i in range(5):
            list_view.add_widget(OneLineListItem(text=f"Item {i + 1}"))
        for i in range(5):
            list_view.add_widget(TwoLineListItem(text=f"Item {i + 1}",
                                                 secondary_text=f"This is item no {i + 1}"))
        for i in range(5):
            list_view.add_widget(ThreeLineListItem(text=f"Item {i + 1}",
                                                   secondary_text=f"This is item no {i + 1}",
                                                   tertiary_text=f"This is another item no {i + 1}"))
        scroll_view.add_widget(list_view)
        screen.add_widget(scroll_view)
        return screen


OneLineListApp().run()
