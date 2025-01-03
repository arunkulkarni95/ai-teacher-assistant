from pydantic import BaseModel
from typing import List

class LessonPlan(BaseModel):
    topic: str
    objectives: List[str]
    content: str
    activities: List[str]

    def to_markdown(self) -> str:
        """
        Convert the lesson plan to Markdown format.
        """
        objectives_md = "\n".join([f"- {o}" for o in self.objectives])
        activities_md = "\n".join([f"- {a}" for a in self.activities])
        return (
            f"# Lesson Plan: {self.topic}\n\n"
            f"## Objectives\n{objectives_md}\n\n"
            f"## Content\n{self.content}\n\n"
            f"## Activities\n{activities_md}"
        )

