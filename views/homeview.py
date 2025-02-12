import flet as ft
from configs import PAGE_CONFIGS
from widgets import card_transacao, card_resumo

class HomeView():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.window.width = PAGE_CONFIGS["width"]
        self.page.window.height = PAGE_CONFIGS["height"]
        self.page.theme_mode = PAGE_CONFIGS["theme"]    

        
        self.meta_de_gasto = 100
        self.total_saidas = 75
        self.total_entradas = 10
        self.saldo = self.total_entradas - self.total_saidas
        
        self.resumo = card_resumo.ResumoCard(self.saldo,self.meta_de_gasto,self.total_entradas,self.total_saidas)
        self.txt = ft.Text(value=100)
        
        self.page.views.append(self.render_homeview())
        self.page.update()
        
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
                        self.txt,
                        ft.Button(text="add", on_click=self.alterar_meta)
                    ]
                )
            ]
        )