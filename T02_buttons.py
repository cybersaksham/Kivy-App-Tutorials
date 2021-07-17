from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class BtnApp(MDApp):
    screen = MDScreen()

    def build(self):
        btn = MDFlatButton(text="Flat Button",
                           pos_hint={'center_x': 0.5, 'center_y': 0.8})
        btn2 = MDRectangleFlatButton(text="Rectangle Flat Button",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.7})
        btn3 = MDIconButton(icon="delete",
                            pos_hint={'center_x': 0.5, 'center_y': 0.6})
        btn4 = MDFloatingActionButton(icon="language-python",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.screen.add_widget(btn)
        self.screen.add_widget(btn2)
        self.screen.add_widget(btn3)
        self.screen.add_widget(btn4)
        return self.screen


BtnApp().run()
