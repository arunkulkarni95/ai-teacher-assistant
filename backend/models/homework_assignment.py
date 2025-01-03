from pydantic import BaseModel
from typing import List

class HomeworkAssignment(BaseModel):
    title: str
    description: str
    due_date: str
    questions: List[str]

    def to_markdown(self) -> str:
        """
        Convert the homework assignment to Markdown format.
        """
        questions_md = "\n".join([f"- {q}" for q in self.questions])
        return (
            f"# {self.title}\n\n"
            f"**Description:** {self.description}\n\n"
            f"**Due Date:** {self.due_date}\n\n"
            f"### Questions\n{questions_md}"
        )
