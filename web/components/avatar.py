import reflex as rx

def avatar(url: str) -> rx.Component:
    return rx.avatar(src=url, size='5')