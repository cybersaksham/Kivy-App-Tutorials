username_helper = """
MDTextField:
    hint_text: "Username"
    helper_text: "Enter a random text"
    helper_text_mode: "on_focus"
    icon_right: "face"
    icon_right_color: app.theme_cls.primary_color
    size_hint_x: None
    width: 300
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Item 1"
            OneLineListItem:
                text: "Item 2"
"""

list_helper_advanced = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "ToolBar"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 10
        MDLabel:
            text: "Hello"
            halign: "center"
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                on_action_button: app.navigation_draw()
                icon: "delete"
"""

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

screen_manager_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: "menu"
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: "Upload"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: "profile"
    MDLabel:
        text: "Profile Screen"
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: "upload"
    MDLabel:
        text: "Uploading..."
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
"""
