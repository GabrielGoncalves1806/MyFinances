import flet as ft

class DrawerWidget(ft.NavigationDrawer):
    def __init__(self):
        super().__init__()
        
        self.controls = [
                ft.Container(
                    content=ft.Column(
                       [
                            ft.Image(
                                src="assets/profile.png",
                                width=75,
                                height=75,
                                border_radius=50
                            ),
                            ft.Text("Gabriel Oliveira",size=18)
                       ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=10,
                    alignment=ft.alignment.center
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    label="Relatórios",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.NavigationDrawerDestination(
                    label="Parametros",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.NavigationDrawerDestination(
                    label="Configurações",
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.SETTINGS_ROUNDED),
                ),
            ]      
        
        
        # self.controls=[
        #     ft.Container(height=12),
        #     ft.NavigationDrawerDestination(
        #         label="Item 1",
        #         icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
        #         selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
        #     ),
        #     ft.Divider(thickness=2),
        #     ft.NavigationDrawerDestination(
        #         icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
        #         label="Item 2",
        #         selected_icon=ft.Icons.MAIL,
        #     ),
        #     ft.NavigationDrawerDestination(
        #         icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
        #         label="Item 3",
        #         selected_icon=ft.Icons.PHONE,
        #     ),
        # ],
    