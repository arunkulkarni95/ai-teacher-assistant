from pydantic_ai import Agent
from pydantic_ai.models.mistral import MistralModel

class TranslationAgent(Agent):
    def __init__(self):
        model = MistralModel('mistral-small-latest')  # Replace with your chosen Mistral model
        super().__init__(model)

    def translate(self, text: str, target_language: str = "es") -> str:
        """
        Translate text into the target language.
        """
        prompt = f"Translate the following text to {target_language}:\n{text}"
        return self.run(prompt)
