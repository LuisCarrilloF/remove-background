import flet as ft

def main(page: ft.Page):
    page.title = "LCarrillo.dev - Remove Background"
    page.bgcolor = "#1a1a2e"
    page.window.height = 850
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK
    
    page.update()

ft.app(target=main)