import flet as ft
from datetime import datetime
from models import database_control
from unidecode import unidecode

class TransactionForm():
    def __init__(self, page: ft.Page):
        self.page = page
        self.msg_snack = ft.SnackBar(ft.Text("Transação adicionada com sucesso!"))

        # Campos do formulário
        self.descricao = ft.TextField(label="Descrição", max_length=50)
        self.valor = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
        self.tipo_transacao = ft.Dropdown(
            label="Tipo",
            options=[
                ft.dropdown.Option("Entrada"),
                ft.dropdown.Option("Saída"),
            ]
        )
        self.data = datetime.now().strftime("%d/%m/%Y")

        self.botao_salvar = ft.ElevatedButton(
            text="Salvar",
            on_click=lambda e: self.save_values()
        )

    def save_values(self):
        dados = self.get_values()

        if not dados["descricao"] or not dados["valor"] or not dados["tipo"]:
            self.msg_snack = ft.SnackBar(content=ft.Text("Preencha todos os campos!"))
        else:
            dados_salvos = database_control.add_transacao(
                dados["descricao"],
                float(dados["valor"]),
                unidecode(dados["tipo"].lower()),
                self.data
            )
            
            if dados_salvos:
                self.msg_snack = ft.SnackBar(content=ft.Text("Transação adicionada com sucesso!"))
                self.descricao.value = ""
                self.valor.value = ""
                self.tipo_transacao.value = None
            else:
                self.msg_snack = ft.SnackBar(content=ft.Text("Erro ao adicionar a transação!"))

        self.page.overlay.append(self.msg_snack)
        self.msg_snack.open = True
        self.page.update()

    def get_values(self):
        return {
            "descricao": self.descricao.value,
            "valor": self.valor.value,
            "tipo": self.tipo_transacao.value,
            "data": self.data
        }

    # Retorna os controles para a tela
    def get_controls(self):
        return ft.Column(
            [
                self.descricao,
                self.valor,
                self.tipo_transacao,
                self.botao_salvar,
            ],
            spacing=10
        )

        