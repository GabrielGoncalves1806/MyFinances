import flet as ft

class ResumoCard(ft.Card):
    def __init__(self, saldo, meta_gasto, receita, saidas):
        super().__init__()

        self.saldo_text = ft.Text(f"Saldo: R$ {saldo:.2f}", size=18, weight="bold")
        self.meta_text = ft.Text(f"Meta de Gastos: R$ {meta_gasto:.2f}", size=16, color="grey")
        self.progress_bar = ft.ProgressBar(
            value=saidas / meta_gasto if meta_gasto > 0 else 0, 
            height=5, 
            border_radius=25, 
            color=ft.Colors.GREEN if saidas / meta_gasto < 0.75 else ft.Colors.RED)
        self.receita_text = ft.Text(f"Receita: R$ {receita:.2f}", size=16, color="green")
        self.saidas_text = ft.Text(f"Saídas: R$ {saidas:.2f}", size=16, color="red")

        # Criar os componentes do Card
        self.content = ft.Container(
            content=ft.Column([
                ft.Row([self.saldo_text], alignment="spaceBetween"),
                self.meta_text,
                self.progress_bar,
                ft.Row([self.receita_text, self.saidas_text], alignment="spaceBetween")
            ]),
            padding=15,
        )

