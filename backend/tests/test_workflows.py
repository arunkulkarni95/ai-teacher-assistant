import sys
import os

# Add the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from workflows.lesson_plan_workflow import process_lesson_plan
import asyncio
import logfire

logfire.configure()

def test_lesson_plan_workflow():
    topic = "Fractions"
    content = "Today's lesson is about adding and subtracting fractions."

    lesson_plan = asyncio.run(process_lesson_plan(topic, content, "es"))
    print(lesson_plan.model_dump_json(indent=4))

if __name__ == "__main__":
    test_lesson_plan_workflow()
