import asyncio
import os
import sys

# Add the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from workflows.lesson_plan_workflows import process_plaintext_workflow, process_pdf_workflow
from IPython.display import Markdown
import logfire

# Configure Logfire
logfire.configure()

async def test_plaintext_workflow():
    """
    Test the plaintext workflow with sample inputs.
    """
    topic = "Fractions"
    content = "Today's lesson is about adding and subtracting fractions."
    grade_level = 5
    objectives = [
        "Understand fractions.",
        "Practice addition and subtraction of fractions."
    ]

    # Process the lesson plan
    lesson_plans = await process_plaintext_workflow(topic, content, grade_level, objectives)

    # Generate Markdown outputs
    for lesson_plan in lesson_plans:
        markdown_output = lesson_plan.to_markdown()
        print(markdown_output)  # For console output
        Markdown(markdown_output)  # For interactive Markdown display


async def test_pdf_workflow():
    """
    Test the PDF workflow with sample PDF content.
    """
    # Simulated extracted text from a PDF
    pdf_text = """
    Lesson Topic: Fractions
    Content: This lesson covers how to add and subtract fractions. Students will also solve word problems involving fractions.
    """
    grade_level = 5
    objectives = [
        "Understand fractions.",
        "Practice addition and subtraction of fractions.",
        "Solve fraction word problems."
    ]

    # Process the lesson plan
    lesson_plans = await process_pdf_workflow(pdf_text, grade_level, objectives)

    # Generate Markdown outputs
    for lesson_plan in lesson_plans:
        markdown_output = lesson_plan.to_markdown()
        print(markdown_output)  # For console output
        Markdown(markdown_output)  # For interactive Markdown display


if __name__ == "__main__":
    asyncio.run(test_plaintext_workflow())
    asyncio.run(test_pdf_workflow())
