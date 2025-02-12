import flet as ft

class TransacaoCard(ft.Card):
    def __init__(self, descricao, valor, data, tipo):
        super().__init__()
        icone = ft.Icon(ft.Icons.ARROW_FORWARD, color="red") if tipo == "saida" else ft.Icon(ft.icons.ARROW_BACK, color="green")
        
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