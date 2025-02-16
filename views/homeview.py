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

        
        self.meta_de_gasto = 500
        self.total_saidas = 0
        self.total_entradas = 0
        self.saldo = self.total_entradas - self.total_saidas
        
        self.atualizar_resumo()
        
        self.nav_drawer = drawer_widget.DrawerWidget()
        self.resumo = card_resume.ResumoCard(self.saldo,self.meta_de_gasto,self.total_entradas,self.total_saidas)
        self.historico = ft.Column(scroll=True,height=300)
        
        self.page.views.append(self.render_homeview())
        self.render_movimentacoes()
        
        self.page.update()
    
    def render_movimentacoes(self):
        self.historico.controls.clear()
        data = database_control.get_transaction()
        for item in data:
            self.historico.controls.append(card_transaction.TransacaoCard(description=item["description"],value=item["value"],type=item["type"],data=item["date"]))
        self.historico.controls.reverse()
        
    def atualizar_resumo(self):
        entradas = []
        saidas = []
        data = database_control.get_transaction()
        for item in data:
            if item["type"] == "receita":
                entradas.append(item["value"])
            else:
                saidas.append(item["value"])
        # Atualiza o ResumoCard com os novos values
        self.saldo = sum(entradas) - sum(saidas)
        self.total_entradas = sum(entradas)
        self.total_saidas = sum(saidas)
        #self.resumo.atualizar(saldo=sum(entradas)-sum(saidas),meta_gasto=self.meta_de_gasto,entradas=sum(entradas),saidas=sum(saidas))

        # Chama update para renderizar as alterações
        self.page.update()  # Apenas atualiza a página
    
    def render_homeview(self):
        return ft.View(
            route="/home",
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
                title=ft.Text("My Finance app"),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.MENU,on_click= lambda e: self.page.open(self.nav_drawer))
            ),
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: route_control.go_to(self.page,"/add")),
            drawer=self.nav_drawer
        )