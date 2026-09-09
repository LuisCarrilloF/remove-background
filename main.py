import flet as ft
import os

def main(page: ft.Page):

    async def select_files(e):
        files = await file_picker.pick_files(
            allow_multiple=True,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["png", "jpg", "jpeg", "bmp"],
        )

        if files:
            file_count = len(files)
            directory = os.path.dirname(files[0].path)
            select_files_info.value = f"{file_count} archivo(s) seleccionado(s) en {directory}"
            select_files_info.color = "#4caf50"
        else:
            select_files_info.value = "No hay archivos seleccionados"
            select_files_info.color = "#a80000"

        page.update()

    page.title = "LCarrillo.dev - Remove Background"
    page.bgcolor = "#1a1a2e"
    page.window.height = 850
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK

    select_files_info = ft.Text(
        "Ningún archivo ha sido seleccionado",
        color="#a0a0a0",
        size=15
    )

    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    btn_select_files = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.CLOUD_UPLOAD, color="#fcfefc"),
                ft.Text("Seleccionar archivos", color="#fcfefc", size=15, weight=ft.FontWeight.BOLD)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        color="#fcfefc",
        bgcolor="#ad4141",
        on_click=select_files,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            elevation=12
        )
    )

    page.add(select_files_info, btn_select_files)


ft.app(target=main)