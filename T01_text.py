from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class TextApp(MDApp):
    def build(self):
        # label = MDLabel(text="Primary", halign='center', theme_text_color="Primary")
        # label = MDLabel(text="Secondary", halign='center', theme_text_color="Secondary")
        # label = MDLabel(text="Error", halign='center', theme_text_color="Error")
        label = MDLabel(text="Error", halign='center', theme_text_color="Custom",
                        text_color=(1, 0, 1, 1), font_style="H1")
        icon_label = MDIcon(icon='delete', halign='center',
                            theme_text_color="Custom", text_color=(1, 0, 0, 1))
        return icon_label


TextApp().run()
