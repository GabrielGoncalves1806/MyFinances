import flet as ft
from models import database_control

class CategoryForm():
    def __init__(self,page:ft.Page):
        self.page = page
        self.msg_snack = ft.SnackBar(ft.Text("Categoria adicionada com sucesso!"))
        
        self.name = ft.TextField(label="Nome da categoria")
        self.colors_list = [ft.Colors.RED,ft.Colors.GREEN,ft.Colors.BLUE,ft.Colors.YELLOW,ft.Colors.ORANGE,ft.Colors.PURPLE]
        self.colors_dropdown = ft.Dropdown(label="Cor")
        
        self.save_button = ft.ElevatedButton(text="Salvar", on_click=lambda e: self.save_values())
        
        for color in self.colors_list:
            self.colors_dropdown.options.append(
                ft.dropdown.Option(
                    text=color,
                    content=ft.Row(
                        [
                            ft.Container(height=25,width=25,border_radius=25,bgcolor=color),
                            ft.Text(value=color.split(".")[0].upper())
                        ]
                    )
                )
            )
    def save_values(self):
        data = self.get_values()
        if not data["name"] or not data["color"]:
            self.msg_snack.content = ft.Text("Preencha todos os campos!")
        else:
            data_saved = database_control.add_category(self.name.value,self.colors_dropdown.value)
            
        if data_saved:
            self.name.value = ""
            self.colors_dropdown.value = None
        else:
            self.msg_snack.content = ft.Text("Erro ao adicionar categoria!")
        
        self.page.overlay.append(self.msg_snack)
        self.msg_snack.open = True
        self.page.update()
        
    def get_values(self):
        return {
            "name": self.name.value,
            "color": self.colors_dropdown.value,
        }
        
    def get_controls(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Categoria",size=18),
                        self.name,
                        self.colors_dropdown,
                        self.save_button
                    ]
                ),
                padding=15
            )
        )