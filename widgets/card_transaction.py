import flet as ft

class TransacaoCard(ft.Card):
    def __init__(self, description, value, data, type):
        super().__init__()
        icone = ft.Icon(ft.Icons.ARROW_FORWARD, color="red") if type == "despesa" else ft.Icon(ft.Icons.ARROW_BACK, color="green")
        
        self.content = ft.Container(
            content=ft.Column([
                ft.Text(description, size=18, weight="bold"),
                ft.Text(f"R$ {value:.2f}", size=16, color="grey"),
                ft.Row([
                    icone,
                    ft.Text(data, size=14, color="grey")
                ], alignment="spaceBetween")
            ]),
            padding=15,
            
        )
        self.color = color=ft.Colors.GREY_900