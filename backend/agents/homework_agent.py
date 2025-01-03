from agents.base_agent import BaseAgent
from models.homework_assignment import HomeworkAssignment

class HomeworkAgent(BaseAgent):
    def __init__(self):
        super().__init__(result_type=HomeworkAssignment)

    def generate_homework(self, topic: str, grade_level: int) -> HomeworkAssignment:
        """
        Generate a structured homework assignment.
        """
        prompt = (
            f"Create a homework assignment for grade {grade_level} students on the topic '{topic}'. "
            f"Include a title, description, due date, and at least 3 questions."
        )
        return self.run(prompt)
