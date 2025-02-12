import flet as ft

class TransacaoCard(ft.Card):
    def __init__(self, descricao, valor, data, tipo):
        super().__init__()
        
        icone = ft.Icon(ft.icons.ARROW_FORWARD, color="red") if tipo == "saida" else ft.Icon(ft.icons.ARROW_BACK, color="green")
        
        self.content = ft.Container(
            content=ft.Column([
                ft.Text(descricao, size=18, weight="bold"),
                ft.Text(f"R$ {valor:.2f}", size=16, color="grey"),
                ft.Row([
                    icone,
                    ft.Text(data, size=14, color="grey")
                ], alignment="spaceBetween")
            ]),
            padding=15,
        )

class ResumoCard(ft.Card):
    def __init__(self, saldo, meta_gasto, entradas, saidas):
        super().__init__()
        
        self.content = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Saldo", size=18, weight="bold"),
                    ft.Text("******", size=18, weight="bold"),
                    ft.Icon(ft.icons.VISIBILITY)
                ], alignment="spaceBetween"),
                ft.Text(f"Meta de Gastos: R$ {meta_gasto:.2f}", size=16, color="grey"),
                ft.ProgressBar(value=meta_gasto / saldo if saldo > 0 else 0),
                ft.Row([
                    ft.Text(f"Entradas: R$ {entradas:.2f}", size=16, color="green"),
                    ft.Text(f"Saídas: R$ {saidas:.2f}", size=16, color="red")
                ], alignment="spaceBetween")
            ]),
            padding=15,
        )

def main(page: ft.Page):
    page.title = "Gestão de Gastos"
    page.theme_mode = "light"
    
    lista_transacoes = ft.Column(scroll="auto", expand=True)
    lista_transacoes.controls.append(TransacaoCard("Vaquina futebol", 10.00, "12/02/2025", "saida"))
    lista_transacoes.controls.append(TransacaoCard("Adiantamento", 455.00, "15/02/2025", "entrada"))
    
    def adicionar_transacao(e):
        lista_transacoes.controls.append(TransacaoCard("Nova transação", 0.00, "00/00/0000", "entrada"))
        page.update()
    
    page.add(
        ft.Column(
            [
                ResumoCard(5000.00, 2000.00, 3000.00, 1000.00),
                lista_transacoes,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=adicionar_transacao)
            ],
            expand=True
        )
    )
    
ft.app(target=main)
