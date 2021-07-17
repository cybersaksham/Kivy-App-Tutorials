from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton


class BtnApp(MDApp):
    screen = MDScreen()

    def build(self):
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.theme_style = "Dark"
        btn1 = MDRectangleFlatButton(text="Rectangle Flat Button",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn2 = MDFloatingActionButton(icon="language-python",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.screen.add_widget(btn1)
        self.screen.add_widget(btn2)
        return self.screen


BtnApp().run()
