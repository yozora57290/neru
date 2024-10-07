import flet as ft


def main(page: ft.Page):
    page.title = "Neru"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Text("Neru", size=32)
    record_button = ft.ElevatedButton("睡眠を記録")
    manage_button = ft.ElevatedButton("睡眠を管理")
    settings_button = ft.ElevatedButton("設定")

    page.add(
        ft.Column(
            [logo, record_button, manage_button, settings_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )
    )


if __name__ == "__main__":
    ft.app(main)
