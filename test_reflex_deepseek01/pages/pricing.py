import reflex as rx
from ..ui.base import base_page


def pricing_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Pricing", size="9", margin_bottom="1rem"),
            rx.text("This is the money pricing baibi of the Reflex app."),
            height="100vh",
            spacing="5",
            justify="center",
            align="center",
        )
    return base_page(my_child)
