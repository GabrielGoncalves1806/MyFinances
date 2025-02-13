import flet as ft
from forms import add_transacao_form
from controls import route_control

class AddTransacaoView():
    def __init__(self, page:ft.Page):
        self.page = page
        
        self.add_transacao_form = add_transacao_form.TransactionForm(self.page)
        
        self.page.views.append(self.render_add_transacao_view())
        self.page.update()
        
    def render_add_transacao_view(self):
        return ft.View(
            route="/add",
            controls=[
                ft.Column(
                    [
                        self.add_transacao_form.get_controls()
                    ]
                )   
            ],
            appbar=ft.AppBar(
                title=ft.Text("Adicionar movimentação"),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK,on_click=lambda e: route_control.go_to(page=self.page,route="/homeview"))
            )
        )