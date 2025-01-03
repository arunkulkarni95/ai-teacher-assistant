from pydantic import BaseModel
from typing import List

class LessonPlan(BaseModel):
    topic: str
    grade_level: int
    state: str
    objectives: List[str]
    content: str
    activities: List[str]
    language: str  # "en" for English, "es" for Spanish
    skill_level: str  # "struggling", "average", "advanced"

    def to_markdown(self) -> str:
        """
        Convert the lesson plan into a Markdown representation.
        """
        objectives_md = "\n".join([f"- {objective}" for objective in self.objectives])
        activities_md = "\n".join([f"- {activity}" for activity in self.activities])

        return (
            f"# Lesson Plan\n\n"
            f"**Topic:** {self.topic}\n\n"
            f"**Grade Level:** {self.grade_level}\n\n"
            f"**State:** {self.state}\n\n"
            f"**Language:** {self.language}\n\n"
            f"**Skill Level:** {self.skill_level}\n\n"
            f"## Objectives\n{objectives_md}\n\n"
            f"## Content\n{self.content}\n\n"
            f"## Activities\n{activities_md}"
        )
