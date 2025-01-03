from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models.agent_dependencies import LessonPlanDependencies
from pydantic import BaseModel
from typing import Type

import dotenv

dotenv.load_dotenv()

class BaseAgent(Agent):
    def __init__(self, result_type: Type[BaseModel], system_prompt: str):
        model = OpenAIModel("gpt-4o-mini")  # Using openai:gpt-4o-mini model
        super().__init__(
            model=model,
            deps_type=LessonPlanDependencies,
            result_type=result_type,
            system_prompt=system_prompt,
        )
