import reflex as rx
from .nav import navbar

def base_page(child:rx.Component, *args) -> rx.Component:

    # print([type(x) for x in args])
    return rx.fragment(
        navbar(),
        # child,
        rx.box(    
            child,        
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            align = "center",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),

    )     

