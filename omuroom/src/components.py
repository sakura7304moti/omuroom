import reflex as rx
from omuroom.src import color

c = color.color()
"""
ヘッダー
"""
def app_header():
    component = rx.vstack(
        rx.flex(
            rx.text(
                "オム子のお部屋",
                font_size="48px",
                width="50%"
            ),
            width="100%"
        ),
        rx.divider(width="100%"),
        width="100%",
    )
    return component

"""
トップ
"""
def top_panel():
    component = rx.image(
        src="/top3.png",
        background_color=c.base()
    )
    return component