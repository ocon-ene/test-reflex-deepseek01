from typing import List
import reflex as rx
import asyncio

from .model import ContactEntryModel

from sqlmodel import select

class ContactState(rx.State):
    form_data: dict = {}
    did_submt: bool = False
    entries: List['ContactEntryModel'] = []

    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you, {first_name}!"
    
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print("Form data received:", self.form_data)
        data = form_data.copy()
        for k, v in form_data.items():
            if v =="" or v is None:
                continue
            data[k] = v
        print("Data to save before func save:", data)

        with rx.session() as session: #esta parte es la que da problemas, salva la bdd
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            print(f"Saved entry ID: {db_entry.id}")
            self.did_submt = True
            yield
        #     print("cosa pasa esto 1 ? ")
        
        # print("cosa pasa esto 2 ? ")
        await asyncio.sleep(1)
        # print("cosa pasa esto ? 3")

        self.did_submt = False 
        yield

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)                  
            ).all()
            print("Las entradas obtenidas:", entries)
            self.entries = entries



