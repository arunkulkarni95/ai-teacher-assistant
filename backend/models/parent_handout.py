from pydantic import BaseModel

class ParentHandout(BaseModel):
    title: str
    content: str
    action_items: str
    translated_text: str

    def to_markdown(self) -> str:
        """
        Generate a Markdown representation of the parent handout.
        """
        return (
            f"# Parent Handout\n\n"
            f"**Title:** {self.title}\n\n"
            f"**Content:**\n{self.content}\n\n"
            f"**Action Items:**\n{self.action_items}\n\n"
            f"**Translated Text:**\n{self.translated_text}"
        )
