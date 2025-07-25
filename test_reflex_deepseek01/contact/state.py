from typing import List
import reflex as rx
import asyncio

from .model import ContactEntryModel

from sqlmodel import select

class ContactState(rx.State):
    form_data: dict = {}
    did_submt: bool = False
    entries: List['ContactEntryModel'] = []

    async def _save_to_db(self, form_data: dict) :
        """Helper method to save to database."""
        with rx.session() as session:
            db_entry = ContactEntryModel(**form_data)
            session.add(db_entry)
            session.commit()

    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you, {first_name}!"
    
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data= form_data.copy()
        for k, v in form_data.items():
            if v =="" or v is None:
                continue
            data[k] = v
        self._save_to_db(form_data)
 
        self.did_submt = True
        yield
        await asyncio.sleep(1)
        
        self.did_submt = False 
        yield

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)                  
            ).all()
            print("sdfsdf")
            print(entries)
            self.entries = entries



