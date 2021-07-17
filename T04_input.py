from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from helpers import username_helper


class InputApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        # username = MDTextField(text="Enter Username",
        #                        size_hint_x=None, width=300,
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.username = Builder.load_string(username_helper)
        btn = MDRectangleFlatButton(text="Show",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                    on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def show_data(self, _):
        check_str = f"You entered {self.username.text}"
        if self.username.text == "":
            check_str = "Please enter Username"
        close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Checker",
                               text=check_str,
                               buttons=[close_btn])
        self.dialog.open()

    def close_dialog(self, _):
        self.dialog.dismiss()


InputApp().run()
