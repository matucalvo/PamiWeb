import reflex as rx
from web.components.navbar import *
from web.components.footer import *
from web.views.links.header.header import *

#class State(rx.State):
 #   pass 


def index() -> rx.Component:
    return rx.center(
        navBar(),
        rx.divider(),
        rx.vstack(
            header(),
            max_width="1000px",
            margin_y="115px",
        ),
        rx.divider(),
        footer(),
        background="linear-gradient(#BDBDBD, PeachPuff, #BDBDBD)",
        direction="column",
        spacing="3",
        
    )
    

app = rx.App(
    theme=rx.theme(
    appearance="dark",
    has_background=True,
    radius="large",
    accent_color="teal",
    )
)
app.add_page(index)
app._compile()
