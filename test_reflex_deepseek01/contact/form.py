import reflex as rx

from .state import ContactState


def contact_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                    required=True,
                    width="100%",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                    width="100%",
                ),
                rx.input(
                    placeholder="Email",
                    name="email",
                    type="email",
                    width="100%",
                ),
                rx.text_area(
                    name="message",
                    placeholder="Your message",
                    required=True,
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),