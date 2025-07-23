import reflex as rx
# from rxconfig import config
import reflex as rx
from test_reflex_deepseek01.pages import houses  # Import houses page

class State(rx.State):
    clicked: bool = False
    
    def toggle_click(self):
        self.clicked = not self.clicked

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.button(
                "Click Me",
                on_click=State.toggle_click,
                size="4",
                margin_bottom="1rem"
            ),
            rx.cond(
                State.clicked,
                rx.text("Hello Reflex!", color="green"),
            ),
            rx.link(
                rx.button("Go to Houses"),
                href="/houses",  # Link to houses page
                margin_top="2rem"
            ),
            height="100vh"
        )
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(houses.houses_page, route="/houses")  # Add houses page