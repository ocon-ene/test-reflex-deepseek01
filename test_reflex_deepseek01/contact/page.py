import reflex as rx


from ..ui.base import base_page
from .. import navigation

from . import form, state, model


def contact_entry_list_item(contact: model.ContactEntryModel) -> rx.Component:
    return rx.box(
        rx.text(contact.first_name, contact.message, contact.email),
        padding="1rem",
    )

# def foreach_callback(text):
#     return rx.box(rx.text(text))

def contact_entries_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5"),
            rx.foreach(state.ContactState.entries,
                       contact_entry_list_item,),
            spacing="5",
            # justify="center",
            align="center",
            min_height="85vh",
        ),
    )

def contact_page() -> rx.Component:
    # my_form = contact.contact_form() #pudimos haber usado esto, pero segun el video es mejor usar el componente directamente
    my_child = rx.vstack(
            rx.heading("Contact", size="9", margin_bottom="1rem"),
            rx.cond(state.ContactState.did_submt, state.ContactState.thank_you, ""),
            # rx.box(
            #     my_form,
            #     width=["80vw", "80vw", "50vw"],  # Responsive width
            # ),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width="50vw",
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    form.contact_form(),
                    width="80vw",
                )
            ),
            height="100vh",
            spacing="5",
            justify="center",
            align="center",
        )
    return base_page(my_child)