import flet as ft
from widgets import drawer_widget

class ReportsView():
    def __init__(self,page:ft.Page):
        self.page = page
        
        self.nav_drawer = drawer_widget.DrawerWidget(self.page)
        self.nav_drawer.selected_index = 1
        
        self.page.views.append(self.render_reports_view())
        self.page.update()
    
    def render_reports_view(self):
        return ft.View(
            route="/reports",
            controls=[
                ft.Text("Relatórios")
            ],
            appbar=ft.AppBar(
                title=ft.Text("Relatórios"),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.MENU,on_click= lambda e: self.page.open(self.nav_drawer))
            ),
            drawer=self.nav_drawer
            
        )