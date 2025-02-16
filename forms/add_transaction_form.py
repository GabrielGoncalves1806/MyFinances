import flet as ft
from datetime import datetime
from models import database_control
from unidecode import unidecode

class TransactionForm():
    def __init__(self, page: ft.Page):
        self.page = page
        self.msg_snack = ft.SnackBar(ft.Text("Transação adicionada com sucesso!"))

        # Campos do formulário
        self.description = ft.TextField(label="Descrição", max_length=50)
        self.value = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
        self.type_transaction = ft.Dropdown(
            label="Tipo",
            options=[
                ft.dropdown.Option(text="Receita",content=ft.Row([ft.Icon(ft.Icons.ARROW_BACK, color=ft.Colors.GREEN,),ft.Text("Receita")])),
                ft.dropdown.Option(text="Despesa",content=ft.Row([ft.Icon(ft.Icons.ARROW_FORWARD, color=ft.Colors.RED,),ft.Text("Despesa")])),
            ]
        )
        self.date = datetime.now().strftime("%d/%m/%Y")

        self.botao_salvar = ft.ElevatedButton(
            text="Salvar",
            on_click=lambda e: self.save_values()
        )

    def save_values(self):
        dados = self.get_values()

        if not dados["description"] or not dados["value"] or not dados["type"]:
            self.msg_snack = ft.SnackBar(content=ft.Text("Preencha todos os campos!"))
        else:
            dados_salvos = database_control.add_transaction(
                dados["description"],
                float(dados["value"]),
                unidecode(dados["type"].lower()),
                self.date
            )
            
            if dados_salvos:
                self.msg_snack = ft.SnackBar(content=ft.Text("Transação adicionada com sucesso!"))
                self.description.value = ""
                self.value.value = ""
                self.type_transaction.value = None
            else:
                self.msg_snack = ft.SnackBar(content=ft.Text("Erro ao adicionar a transação!"))

        self.page.overlay.append(self.msg_snack)
        self.msg_snack.open = True
        self.page.update()

    def get_values(self):
        return {
            "description": self.description.value,
            "value": self.value.value,
            "type": self.type_transaction.value,
            "date": self.date
        }

    # Retorna os controles para a tela
    def get_controls(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Adicionar Receitas/Despesas",size=18),
                        self.description,
                        self.value,
                        self.type_transaction,
                        self.botao_salvar,
                    ],
                    spacing=10
                ),
                padding=15
            ) 
        )