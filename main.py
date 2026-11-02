import flet as ft


async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    count = 0

    counter_text = ft.Text(
        value=str(count),
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(size=72),
    )

    def refresh_counter() -> None:
        counter_text.value = str(count)
        page.update()

    def increment(_: ft.ControlEvent) -> None:
        nonlocal count
        count += 1
        refresh_counter()

    def decrement(_: ft.ControlEvent) -> None:
        nonlocal count
        count -= 1
        refresh_counter()

    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    counter_text,
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.REMOVE, tooltip="Decrease", on_click=decrement),
                            ft.IconButton(icon=ft.Icons.ADD, tooltip="Increase", on_click=increment),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )


ft.run(main)
