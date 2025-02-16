import flet as ft

class CategoryForm():
    def __init__(self,page:ft.Page):
        self.page = page
        
        self.name = ft.TextField(label="Nome da categoria")
        self.colors_list = [ft.Colors.RED,ft.Colors.GREEN,ft.Colors.BLUE,ft.Colors.YELLOW,ft.Colors.ORANGE,ft.Colors.PURPLE]
        self.colors_dropdown = ft.Dropdown(
            options=[]
        )
        
        self.save_button = ft.ElevatedButton(text="Salvar")
        
        for color in self.colors_list:
            self.colors_dropdown.options.append(
                ft.dropdown.Option(
                    text=color,
                    content=ft.Container(
                        height=25,
                        width=25,
                        border_radius=25,
                        bgcolor=color
                    )
                )
            )
    def save_values(self):
        pass
    def get_controls(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Categoria",size=18),
                        self.name,
                        self.colors_dropdown
                    ]
                ),
                padding=15
            )
        )