import flet as ft

def main(page:ft.Page):
    saldo = 0
    
    def add(e):
        
        page.update()
        
    page.add(
        ft.Text(saldo),
        ft.Button("add", on_click=add)
    )

ft.app(main)