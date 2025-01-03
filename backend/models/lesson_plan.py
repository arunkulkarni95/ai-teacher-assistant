from pydantic import BaseModel
from typing import List

class LessonPlan(BaseModel):
    topic: str
    objectives: List[str]
    content: str
    activities: List[str]

    def to_markdown(self) -> str:
        """
        Generate a Markdown representation of the lesson plan.
        """
        objectives_md = "\n".join([f"- {objective}" for objective in self.objectives])
        activities_md = "\n".join([f"- {activity}" for activity in self.activities])

        return (
            f"# Lesson Plan\n\n"
            f"**Topic:** {self.topic}\n\n"
            f"## Objectives\n{objectives_md}\n\n"
            f"## Content\n{self.content}\n\n"
            f"## Activities\n{activities_md}"
        )
