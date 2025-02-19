import flet as ft
from models import database_control

class TransacaoCard(ft.Card):
    def __init__(self, description, value, data, type,category_id):
        super().__init__()
        
        icone = ft.Icon(ft.Icons.ARROW_FORWARD, color="red") if type == "despesa" else ft.Icon(ft.Icons.ARROW_BACK, color="green")
        self.category_data = database_control.get_category(category_id)
    
        self.category_color = getattr(ft.Colors,self.category_data["cor"].split(".")[1],None)

        self.category = ft.Row(
                        [
                            ft.Container(height=20,width=20,border_radius=25,bgcolor=self.category_color),
                            ft.Text(self.category_data["nome"])
                        ]
                    )  
          
        self.content = ft.Container(
            content=ft.Column([
                ft.Row([ft.Text(description, size=18, weight="bold"),self.category],alignment="spaceBetween"),
                ft.Row([ft.Text(f"R$ {value:.2f}", size=16, color="grey")],alignment="spaceBetween"),
                
                # Linha com o icone de receita/despesa, data e 
                ft.Row(
                    [
                    icone,
                    ft.Text(data, size=14, color="grey")
                ], alignment="spaceBetween")
            ]),
            padding=15,
            
        )
        self.color = color=ft.Colors.GREY_900
        
        
                        