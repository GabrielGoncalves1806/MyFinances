import flet as ft
from forms import add_transacao_form

class AddTransacaoView():
    def __init__(self, page:ft.Page):
        self.page = page
        
    
    def create_add_transacao_view(self):
        return ft.View(
            route="/add",
            controls=[
                add_transacao_form.TransactionForm.get_controls()
            ]
        )