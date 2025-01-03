from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv

load_dotenv()

class DifferentiationAgent(Agent):
    def __init__(self):
        model = OpenAIModel('gpt-4o-mini')
        super().__init__(model)

    def generate_activity(self, topic: str, skill_level: str) -> str:
        """
        Generate activities for specific skill levels.
        """
        prompt = f"Create an activity for {skill_level} learners on the topic '{topic}'."
        return self.run(prompt)
