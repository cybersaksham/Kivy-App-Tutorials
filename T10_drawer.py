from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import screen_helper

Window.size = (350, 600)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "ToolBar"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: "cute.png"
                MDLabel:
                    text: "User"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "user@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon: "face"
                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon: "upload"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
"""


class DrawerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        screen = Builder.load_string(navigation_helper)
        return screen

    @staticmethod
    def navigation_draw():
        print("Navigation")


DrawerApp().run()
