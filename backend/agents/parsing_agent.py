from .base_agent import BaseAgent
from pydantic import BaseModel
from models.agent_dependencies import LessonPlanDependencies

class ParsingResult(BaseModel):
    topic: str
    summary: str

class ParsingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            result_type=ParsingResult,
            system_prompt="You are a document parsing assistant. Extract the topic and summarize the content of lesson plans."
        )

    async def parse_pdf(self, pdf_text: str) -> ParsingResult:
        """
        Parse the topic and summary from PDF text.
        """
        prompt = f"Extract the topic and summarize the content from the following PDF text:\n\n{pdf_text}"
        result = await self.run(prompt, deps=LessonPlanDependencies(todays_date="2024-12-30"))
        return result.data  # Return the structured ParsingResult
