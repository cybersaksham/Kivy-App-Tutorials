from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class AdvancedListApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        for i in range(5):
            icon = IconLeftWidget(icon="delete")
            item = ThreeLineIconListItem(text=f"Item {i + 1}",
                                         secondary_text=f"This is item no {i + 1}",
                                         tertiary_text=f"This is another item no {i + 1}")
            item.add_widget(icon)
            list_view.add_widget(item)
        for i in range(5):
            icon = ImageLeftWidget(source="cute.png")
            item = ThreeLineAvatarListItem(text=f"Item {i + 1}",
                                           secondary_text=f"This is item no {i + 1}",
                                           tertiary_text=f"This is another item no {i + 1}")
            item.add_widget(icon)
            list_view.add_widget(item)

        scroll_view.add_widget(list_view)
        screen.add_widget(scroll_view)
        return screen


AdvancedListApp().run()
