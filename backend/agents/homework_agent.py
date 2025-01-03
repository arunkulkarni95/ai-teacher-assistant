from pydantic_ai import Agent
from pydantic_ai.models.mistral import MistralModel
from models.homework_assignment import HomeworkAssignment

class HomeworkAgent(Agent):
    def __init__(self):
        model = MistralModel('mistral-small-latest')
        super().__init__(model, result_type=HomeworkAssignment)

    def generate_homework(self, topic: str, grade_level: int) -> HomeworkAssignment:
        """
        Generate a structured homework assignment.
        """
        prompt = (
            f"Create a homework assignment for grade {grade_level} students on the topic '{topic}'. "
            f"Include a title, description, due date, and at least 3 questions."
        )
        return self.run(prompt)
