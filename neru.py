import flet as ft


def page_record(page: ft.Page):
    page.controls.clear()

    title = ft.Text("睡眠を記録", size=32)

    def on_sleep_time_change(e):
        sleep_time_button.text = f"就寝時間: {e.control.value.strftime('%H:%M')}"
        sleep_time_button.update()

    sleep_time_button = ft.ElevatedButton(
        "就寝時間を入力",
        on_click=lambda _: page.open(
            ft.TimePicker(
                cancel_text="キャンセル",
                confirm_text="確認",
                help_text="就寝時間を入力",
                on_change=on_sleep_time_change,
            )
        ),
    )

    def on_wake_time_change(e):
        wake_time_button.text = f"起床時間: {e.control.value.strftime('%H:%M')}"
        wake_time_button.update()

    wake_time_button = ft.ElevatedButton(
        "起床時間を入力",
        on_click=lambda _: page.open(
            ft.TimePicker(
                cancel_text="キャンセル", confirm_text="確認", help_text="起床時間を入力", on_change=on_wake_time_change
            )
        ),
    )

    def on_record_button_click(e):
        record_button.text = "記録しました"
        record_button.update()

    record_button = ft.ElevatedButton("記録する", on_click=on_record_button_click)

    page.add(
        ft.Column(
            [title, sleep_time_button, wake_time_button, record_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )
    )


def main(page: ft.Page):
    page.title = "Neru"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    logo = ft.Text("Neru", size=32)
    record_button = ft.ElevatedButton("睡眠を記録", on_click=lambda _: page_record(page))
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
