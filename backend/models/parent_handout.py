from pydantic import BaseModel

class ParentHandout(BaseModel):
    title: str
    content: str
    action_items: str
    translated_text: str
