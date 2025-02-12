import flet as ft
from configs import PAGE_CONFIGS
class HomeView():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.window.width = PAGE_CONFIGS["width"]
        self.page.window.height = PAGE_CONFIGS["height"]
        self.page.theme_mode = PAGE_CONFIGS["theme"]    

        self.page.views.append(self.render_homeview())
        self.page.update()
        
    def render_homeview(self):
        return ft.View(
            route="/home",
            controls=[
                # Header
                ft.Column(controls=[
                    ft.Text("Opa"),
                    
                ])
            ]
        )