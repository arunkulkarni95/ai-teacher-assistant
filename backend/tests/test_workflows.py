import os
import sys

# Add the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from workflows.lesson_plan_workflow import process_lesson_plan
from IPython.display import Markdown
import logfire

logfire.configure()

async def test_lesson_plan_workflow():
    topic = "Fractions"
    content = "Today's lesson is about adding and subtracting fractions."

    # Process the lesson plan
    lesson_plan = await process_lesson_plan(topic, content, "es")

    # Convert to Markdown and display
    markdown_output = lesson_plan.to_markdown()
    print(markdown_output)  # For console output
    Markdown(markdown_output)  # For interactive Markdown display

if __name__ == "__main__":
    asyncio.run(test_lesson_plan_workflow())
