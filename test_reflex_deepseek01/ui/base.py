import reflex as rx
from .nav import navbar

def base_page(child:rx.Component, *args) -> rx.Component:

    print([type(x) for x in args])
    return rx.container(
        navbar(),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),

    )     

