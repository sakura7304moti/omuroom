"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from omuroom.src import components
from omuroom.src import color

import reflex as rx

c = color.color()

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


@rx.page(route = "/", title = "omuroom top")
def index() -> rx.Component:
    return rx.vstack(
        components.app_header(),
        components.top_panel(),
        width="100%"
    )

style = {
    "font_family" : "Noto Sans JP",
    "font_size" : "16px",
    "padding" : "16px",
    "background_color" : "RGB(251,245,237)",
    "height" : "100vh"
    
}


app = rx.App(style = style)
app.add_page(index)
