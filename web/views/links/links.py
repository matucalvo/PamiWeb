import reflex as rx
from web.components.link_button import *

def links() -> rx.Component:
    return rx.hstack(
        link_button("Inicio", "https://instagram.com"),
        link_button("Internos HBI", "https://instagram.com"),
        link_button("Fichas", "asdasd")
    )