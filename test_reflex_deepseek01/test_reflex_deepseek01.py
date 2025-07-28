import reflex as rx
from rxconfig import config
# from test_reflex_deepseek01.pages import houses  # Import houses page

from .ui.base import base_page
from . import blog, contact, pages, navigation

class State(rx.State):
    label =  "Welcome to Reflex! 2"

    clicked: bool = False

    def toggle_click(self):
        self.clicked = not self.clicked

    def handle_title_input_change(self, val):
        self.label = val

    # def did_click(self):
    #     print(self.label)




def index() -> rx.Component:
    my_child = rx.vstack(
            rx.heading(State.label, size="9", margin_bottom="1rem"),
            rx.link(
                rx.button("Go to About"),
                href="/about",  # Link to about page
            ),
            rx.link(), #always do instead of button
            rx.link(
                rx.button("Go to Houses"),
                href="/houses",  # Link to houses page
                # margin_top="2rem"
            ),
            height="100vh",
            spacing="5",
            justify="center",
            align="center",
            # text_align="center",
            # min_height="100vh",
        )
    return base_page(my_child)



app = rx.App()
app.add_page(index, route="/")
app.add_page(pages.houses_page, 
             route=navigation.routes.HOUSES_ROUTE)
app.add_page(pages.about_page, 
             route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(pages.pricing_page, 
             route=navigation.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, 
             route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(contact.contact_entries_list_page, 
             route=navigation.routes.CONTACT_ENTRIES_ROUTE,
             on_load=contact.ContactState.list_entries
             
)

  # Add houses page