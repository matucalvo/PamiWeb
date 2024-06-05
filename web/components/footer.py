import reflex as rx

def footer() -> rx.Component:
    return rx.center(
        rx.image(src="pami.png", height="auto", width="300px"),
        rx.text("Departamento de sistemas del hospital Bicentenario de Ituzaingo."),
        direction="column",
        width="50%"
    )