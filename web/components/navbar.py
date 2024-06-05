import reflex as rx
from web.views.links.links import *

def navBar() -> rx.Component:
    return rx.center(
        links(),
        padding_x = "16px",
        padding_y = "20px"
    )

