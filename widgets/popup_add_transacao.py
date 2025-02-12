import flet as ft

class TransacaoPopup(ft.AlertDialog):
    def __init__(self, on_save):
        super().__init__()
        self.on_save = on_save  # Função chamada ao salvar a transação
        
        # Campos do formulário
        self.descricao = ft.TextField(label="Descrição", expand=True)
        self.valor = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER, expand=True)
        self.tipo = ft.Dropdown(
            label="Tipo",
            options=[
                ft.dropdown.Option("Entrada"),
                ft.dropdown.Option("Saída"),
            ],
            expand=True
        )

        # Criar o popup
        self.content = ft.Column(
            [
                self.descricao,
                self.valor,
                self.tipo,
                ft.Row(
                    [
                        ft.TextButton("Cancelar", on_click=self.fechar),
                        ft.FilledButton("Salvar", on_click=self.salvar),
                    ],
                    alignment="end"
                )
            ],
            tight=True
        )

    def abrir(self, e):
        self.open = True
        self.update()

    def fechar(self, e):
        self.open = False
        self.update()

    def salvar(self, e):
        if not self.descricao.value or not self.valor.value or not self.tipo.value:
            return  # Não permite salvar se algum campo estiver vazio

        # Chama a função de callback passando os dados preenchidos
        self.on_save({
            "descricao": self.descricao.value,
            "valor": float(self.valor.value),
            "tipo": self.tipo.value
        })

        # Fecha o popup
        self.fechar(e)
