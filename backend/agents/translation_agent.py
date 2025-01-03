from .base_agent import BaseAgent
from models.agent_dependencies import LessonPlanDependencies, TranslationResult

class TranslationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            result_type=TranslationResult,
            system_prompt="You are a helpful translator specialized in educational materials. Provide accurate, clear, and context-aware translations."
        )

    async def translate(self, text: str, target_language: str = "es") -> str:
        """
        Translate text into the target language.
        """
        prompt = f"Translate the following text to {target_language}:\n{text}"
        result = await self.run(prompt, deps=LessonPlanDependencies(todays_date="2024-12-30"))
        return result.data.translated_text  # Use structured result
