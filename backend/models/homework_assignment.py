from pydantic import BaseModel
from typing import List

class HomeworkAssignment(BaseModel):
    title: str
    description: str
    due_date: str
    questions: List[str]

    def to_markdown(self) -> str:
        """
        Generate a Markdown representation of the homework assignment.
        """
        questions_md = "\n".join([f"- {question}" for question in self.questions])

        return (
            f"# Homework Assignment\n\n"
            f"**Title:** {self.title}\n\n"
            f"**Description:** {self.description}\n\n"
            f"**Due Date:** {self.due_date}\n\n"
            f"## Questions\n{questions_md}"
        )
