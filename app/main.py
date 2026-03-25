import flet as ft
from app.views.mostrar_productos import vista_productos

def main(page: ft.Page):
    page.title = "Mostrar datos FastAPI"
    page.add(vista_productos(page))

ft.app(target=main)