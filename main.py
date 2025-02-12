import flet as ft
from views import homeview

def main(page:ft.Page):
    homeview.HomeView(page)
    
ft.app(main)