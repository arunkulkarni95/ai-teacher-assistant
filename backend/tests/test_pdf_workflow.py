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

async def test_pdf_workflow():
    """
    Test the PDF workflow with simulated PDF text, generating six lesson plans.
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
    state = "Maryland"

    # Process the lesson plan
    lesson_plans = await process_pdf_workflow(pdf_text, grade_level, objectives, state)

    # Validate that six lesson plans are generated
    assert len(lesson_plans) == 6, "Expected 6 lesson plans (3 English, 3 Spanish)."

    # Print each lesson plan as Markdown
    for lesson_plan in lesson_plans:
        markdown_output = lesson_plan.to_markdown()
        print(markdown_output)
        print("\n" + "=" * 40 + "\n")  # Separator for readability
        Markdown(markdown_output)


if __name__ == "__main__":
    asyncio.run(test_pdf_workflow())
