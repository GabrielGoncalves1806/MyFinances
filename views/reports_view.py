import flet as ft

class ReportsView():
    def __init__(self,page:ft.Page):
        self.page = page
        
        self.page.views.append(self.render_reports_view())
        self.page.update()
    
    def render_reports_view(self):
        return ft.View(
            route="/reports",
            controls=[
                ft.Text("Relatórios")
            ]
        )