import flet as ft

class ResumoCard(ft.Card):
    def __init__(self, saldo, meta_gasto, entradas, saidas):
        super().__init__()

        self.saldo_text = ft.Text(f"Saldo: R$ {saldo:.2f}", size=18, weight="bold")
        self.meta_text = ft.Text(f"Meta de Gastos: R$ {meta_gasto:.2f}", size=16, color="grey")
        self.progress_bar = ft.ProgressBar(value=saidas / meta_gasto if meta_gasto > 0 else 0, height=5, 
                                            border_radius=25, 
                                            color=ft.Colors.GREEN if saidas / meta_gasto < 0.75 else ft.Colors.RED)
        self.entradas_text = ft.Text(f"Entradas: R$ {entradas:.2f}", size=16, color="green")
        self.saidas_text = ft.Text(f"Saídas: R$ {saidas:.2f}", size=16, color="red")

        # Criar os componentes do Card
        self.content = ft.Container(
            content=ft.Column([
                ft.Row([self.saldo_text, ft.Icon(ft.Icons.VISIBILITY)], alignment="spaceBetween"),
                self.meta_text,
                self.progress_bar,
                ft.Row([self.entradas_text, self.saidas_text], alignment="spaceBetween")
            ]),
            padding=15,
        )

    def atualizar(self, saldo, meta_gasto, entradas, saidas):
        # Atualizar os textos e a barra de progresso diretamente
        self.saldo_text.value = f"Saldo: R$ {saldo:.2f}"
        self.meta_text.value = f"Meta de Gastos: R$ {meta_gasto:.2f}"
        self.progress_bar.value = saidas / meta_gasto if meta_gasto > 0 else 0
        self.entradas_text.value = f"Entradas: R$ {entradas:.2f}"
        self.saidas_text.value = f"Saídas: R$ {saidas:.2f}"

        # Atualizar a cor da barra de progresso
        self.progress_bar.color = ft.Colors.GREEN if saidas / meta_gasto < 0.75 else ft.Colors.RED

        # Chamar update para atualizar a interface
        self.update()  # Atualiza o card apenas
