import flet as ft


def main(page: ft.Page):
    page.title = "Neru"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Text("Neru", size=32)

    page.add(ft.Column([logo]))


if __name__ == "__main__":
    ft.app(main)
