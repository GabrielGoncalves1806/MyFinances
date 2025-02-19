import flet as ft
from datetime import datetime
from models import database_control
from unidecode import unidecode

class TransactionForm():
    def __init__(self, page: ft.Page):
        self.page = page
        self.msg_snack = ft.SnackBar(ft.Text("Transação adicionada com sucesso!"))
        self.database_categories = database_control.get_category()
        
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
        self.category = ft.Dropdown(
            label="Categoria",
            options=[ft.dropdown.Option(text="Sem categoria")]
            )
        
        for categories in self.database_categories:
            color_name = getattr(ft.Colors,categories["cor"].split(".")[-1],None)
            
            self.category.options.append(
                ft.dropdown.Option(
                    text=categories["nome"],
                    content=ft.Row(
                        [
                            ft.Container(height=25,width=25,border_radius=25,bgcolor=color_name),
                            ft.Text(categories["nome"])
                        ]
                    )
                )
            )
        
        self.date = datetime.now().strftime("%d/%m/%Y")

        self.botao_salvar = ft.ElevatedButton(
            text="Salvar",
            on_click=lambda e: self.save_values()
        )
    
    def update_categories(self):
        self.database_categories = database_control.get_category()
        self.page.update()

    def save_values(self):
        dados = self.get_values()

        if not dados["description"] or not dados["value"] or not dados["type"]:
            self.msg_snack.content = ft.Text("Preencha todos os campos!")
        else:
            dados_salvos = database_control.add_transaction(
                description=dados["description"],
                value=float(dados["value"]),
                type=unidecode(dados["type"].lower()),
                date=self.date,
                category_id=database_control.get_category(name=self.category.value)
            )
            
            if dados_salvos:
                self.msg_snack = ft.SnackBar(content=ft.Text("Transação adicionada com sucesso!"))
                self.description.value = ""
                self.value.value = ""
                self.category.value = None
                self.type_transaction.value = None
            else:
                self.msg_snack.content = ft.Text("Erro ao adicionar a transação!")

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
                        self.category,
                        self.botao_salvar,
                    ],
                    spacing=10
                ),
                padding=15
            ) 
        )