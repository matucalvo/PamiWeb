import reflex as rx
from web.components.card import *

def header() -> rx.Component:
    return rx.box(rx.grid(
        card("Mesa de ayuda sistemas", "sistemas.png", "Gestion de tickets", "asdasd"),
        card("SIT", "contra.png", "Autogestion de contraseñas", "https://sit.pami.org.ar/"),
        card("Correo institucional Zimbra", "correo.png", "Correo Zimbra", "https://correo.pami.org.ar/"),
        card("INTRANET PAMI", "intranet.png", "INTRANET de PAMI", "https://intranet.pami.ar/"),
        card("GDE", "carpeta.png", "Acceso a GDE", "https://cas.pami.gde.gob.ar/acceso/login/?generateToken=true&generateIDP=true&"),
        card("CUP", "candado.png", "Acceso a CUP", "https://cup.pami.org.ar/controllers/loginController.php"),
        card("EDUPAMI", "libros.png", "Acceso a EDUPAMI", "https://edupami.pami.org.ar/"),
        card("SII", "web.png", "Acceso a SII", "https://efectores.pami.org.ar/pami_efectores/"),
        card("Protocolo COVID-19", "virus.png", "Protocolo COVID-19", "https://www.pami.org.ar/saberesprevenir"),
        card("Boletin", "boletin.png", "Boletin del instituto", "https://www.pami.org.ar/boletin-oficial"),
        card("Correo institucional Outlook", "correo.png", "Correo Outlook", "https://email.pami.org.ar/owa/auth/logon.aspx?replaceCurrent=1&reason=2&url=https%3a%2f%2femail.pami.org.ar%2fowa%2f"),
        card("Novedades", "novedades.png", "Novedades PAMI" , "https://www.pami.org.ar/novedades"),
        columns="4",
        spacing="4",
        width="100%",
), spacing="2")
