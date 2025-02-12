import flet as ft
from configs import PAGE_CONFIGS
from widgets import card_transacao, card_resumo, popup_add_transacao
from models import database_control
from datetime import datetime

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
        
        self.popup = popup_add_transacao.TransacaoPopup(self.adicionar_transacao)
        self.page.overlay.append(self.popup)
        self.resumo = card_resumo.ResumoCard(self.saldo,self.meta_de_gasto,self.total_entradas,self.total_saidas)
        self.historico = ft.Column(scroll=True,height=300)
        
        self.txt = ft.Text(value=100)

        self.page.views.append(self.render_homeview())
        self.page.update()
        
    def adicionar_transacao(self,dados):
        data = datetime.now()
        data = data.strftime("%d/%m/%Y")
        database_control.adicionar_transacao(dados["descricao",dados["valor",dados["tipo"].lower(),data]])
        
    def alterar_meta(self, e):
        # Atualiza a meta de gasto
        self.meta_de_gasto += 10
        print(self.meta_de_gasto)

        # Atualiza o ResumoCard com os novos valores
        self.resumo.atualizar(self.saldo, self.meta_de_gasto, self.total_entradas, self.total_saidas)

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
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.popup.abrir)
        )