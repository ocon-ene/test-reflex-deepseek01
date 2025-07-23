import reflex as rx

def houses_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("This is a house", size="7"),
            rx.link(
                rx.button("Go Back"),
                href="/",  # Link back to homepage
                margin_top="2rem"
            ),
            spacing="4",
            align="center"
        ),
        height="100vh"
    )