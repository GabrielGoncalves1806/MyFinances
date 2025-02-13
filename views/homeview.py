import flet as ft
from configs import PAGE_CONFIGS
from widgets import card_transacao, card_resumo, popup_add_transacao
from models import database_control
from datetime import datetime
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
        
        self.resumo = card_resumo.ResumoCard(self.saldo,self.meta_de_gasto,self.total_entradas,self.total_saidas)
        self.historico = ft.Column(scroll=True,height=300)
        
        self.page.views.append(self.render_homeview())
        self.render_movimentacoes()
        
        self.page.update()
    
    def render_movimentacoes(self):
        self.historico.controls.clear()
        data = database_control.get_transacoes()
        for item in data:
            self.historico.controls.append(card_transacao.TransacaoCard(descricao=item["descricao"],valor=item["valor"],tipo=item["tipo"],data=item["data"]))
        
    def atualizar_resumo(self):
        entradas = []
        saidas = []
        data = database_control.get_transacoes()
        for item in data:
            if item["tipo"] == "entrada":
                entradas.append(item["valor"])
            else:
                saidas.append(item["valor"])
        # Atualiza o ResumoCard com os novos valores
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
                automatically_imply_leading=False
            ),
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: route_control.go_to(self.page,"/add"))
        )