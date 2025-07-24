import reflex as rx
from rxconfig import config
from test_reflex_deepseek01.pages import houses  # Import houses page

from .ui.base import base_page

class State(rx.State):
    label =  "Welcome to Reflex! 2"

    clicked: bool = False

    def toggle_click(self):
        self.clicked = not self.clicked

    def handle_title_input_change(self, val):
        self.label = val

    def did_click(self):
        print(self.label)




def index() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9", margin_bottom="1rem"),

            rx.input(
                default_value=State.label,
                on_click=State.did_click,
                on_change = State.handle_title_input_change
            ),
            rx.button(
                "Write a message when clicked",
                on_click=State.toggle_click,
                size="4",
                margin_top="5rem"
            ),
            rx.cond(
                State.clicked,
                rx.text("Hello Reflex!", color="green"),
            ),

            rx.link(
                rx.button("Go to Houses"),
                href="/houses",  # Link to houses page
                # margin_top="2rem"
            ),
            height="100vh",
            spacing="5",
            justify="center",
            align="center",
            # min_height="100vh",
        )
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(houses.houses_page, route="/houses")  # Add houses page