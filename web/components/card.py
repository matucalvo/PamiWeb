import reflex as rx

def card(texto: str, url: str, descripcion: str, link: str) -> rx.Component:
    return rx.card(
         rx.link(
              rx.flex(  
                  rx.avatar(src=url),
                  rx.box(     
                       rx.heading(texto),
                       rx.text(   
                            descripcion,
                            ),
                          ),
                         spacing="2",
                         size="4",
        ),
    href=link),
    as_child=True,
)
