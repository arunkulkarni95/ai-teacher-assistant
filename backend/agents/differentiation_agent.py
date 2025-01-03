from .base_agent import BaseAgent
from models.agent_dependencies import DifferentiationResult, LessonPlanDependencies

class DifferentiationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            result_type=DifferentiationResult,
            system_prompt="You are a skilled education specialist. Create engaging, skill-level-appropriate activities for learners."
        )

    async def generate_activity(self, topic: str, skill_level: str, grade_level: int, state: str) -> str:
        """
        Generate activities for specific skill levels, taking into account grade level and state.
        """
        prompt = (
            f"Create an activity for {skill_level} learners on the topic '{topic}'. "
            f"The activity should be suitable for grade {grade_level} students and comply with educational standards in {state}."
        )
        result = await self.run(prompt, deps=LessonPlanDependencies(todays_date="2024-12-30"))
        return result.data.activity_text  # Use structured result
