from pydantic import BaseModel, Field
from dataclasses import dataclass

@dataclass
class LessonPlanDependencies:
    """
    Dependencies shared by agents, such as the current date or other contextual information.
    """
    todays_date: str

class TranslationResult(BaseModel):
    """
    Result type for the TranslationAgent.
    """
    translated_text: str = Field(description="The translated lesson content.")

class DifferentiationResult(BaseModel):
    """
    Result type for the DifferentiationAgent.
    """
    activity_text: str = Field(description="A differentiated activity for the specified skill level.")
