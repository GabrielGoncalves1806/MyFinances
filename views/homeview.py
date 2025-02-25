import flet as ft
from configs import PAGE_CONFIGS
from widgets import card_resume, card_transaction, drawer_widget
from models import database_control
from controls import route_control

class HomeView():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.window.width = PAGE_CONFIGS["width"]
        self.page.window.height = PAGE_CONFIGS["height"]
        self.page.theme_mode = PAGE_CONFIGS["theme"]   

        self.profile_data = database_control.get_profile_data()
        self.meta_de_gasto = self.profile_data["meta_gastos"]
        self.total_despesas = self.profile_data["total_gastos"]
        self.total_receita = self.profile_data["total_receita"]
        self.saldo = self.total_receita - self.total_despesas
        
        self.atualizar_resumo()
        
        # Widgets
        self.nav_drawer = drawer_widget.DrawerWidget(self.page)
        self.resumo = card_resume.ResumoCard(self.saldo,self.meta_de_gasto,self.total_receita,self.total_despesas)
        self.historico = ft.Column(scroll=True,expand=True)
        
        self.page.on_route_change = lambda e: self.page.update()
        
        self.page.views.append(self.render_homeview())
        self.render_movimentacoes()
        
        self.page.update()
        
    def render_movimentacoes(self):
        self.historico.controls.clear()
        data = database_control.get_transaction()
        for item in data:
            self.historico.controls.append(
                card_transaction.TransacaoCard(
                    description=item["description"],
                    value=item["value"],
                    type=item["type"],
                    data=item["date"],
                    category_id=item["category"]
                )
            )
        self.historico.controls.reverse()
        
    def atualizar_resumo(self):
        receita = []
        despesas = []
        data = database_control.get_transaction()
        for item in data:
            if item["type"] == "receita":
                receita.append(item["value"])
            else:
                despesas.append(item["value"])
        # Atualiza o ResumoCard com os novos values
        self.saldo = sum(receita) - sum(despesas)
        self.total_receita = sum(receita)
        self.total_despesas = sum(despesas)

        # Chama update para renderizar as alterações
        self.page.update()
    
    def render_homeview(self):
        return ft.View(
            route="/home",
            scroll=True,
            controls=[
                # Header
                ft.Column(
                    [
                        self.resumo,
                    ]
                ),
                # Body content
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Row([ft.Text("Histórico de transações",size=18)],alignment=ft.alignment.center),
                                self.historico
                            ],
                            spacing=10
                        ),padding=10
                    ), 
                ),
            ],
            appbar=ft.AppBar(
                title=ft.Text("MyFinance"),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.MENU,on_click= lambda e: self.page.open(self.nav_drawer))
            ),
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=lambda e: route_control.go_to(self.page,"/add")),
            drawer=self.nav_drawer,
            
        )