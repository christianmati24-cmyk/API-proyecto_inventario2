import flet as ft
import requests

def vista_productos(page: ft.Page):
    productos = requests.get("http://127.0.0.1:8000/productos").json()

    lista = []

    for p in productos:
        lista.append(
            ft.Text(f"{p['nombre']} - ${p['precio']}")
        )

    return ft.Column(lista)