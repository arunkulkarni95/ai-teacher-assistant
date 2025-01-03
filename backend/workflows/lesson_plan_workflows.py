from agents.differentiation_agent import DifferentiationAgent
from agents.translation_agent import TranslationAgent

from typing import List

from agents.parsing_agent import ParsingAgent
from models.lesson_plan import LessonPlan

async def process_plaintext_workflow(
    topic: str, content: str, grade_level: int, objectives: List[str], state: str
) -> List[LessonPlan]:
    translator = TranslationAgent()
    differentiation = DifferentiationAgent()

    # Generate activities for three skill levels
    activities = {
        "struggling": await differentiation.generate_activity(topic, "struggling", grade_level, state),
        "average": await differentiation.generate_activity(topic, "average", grade_level, state),
        "advanced": await differentiation.generate_activity(topic, "advanced", grade_level, state),
    }

    lesson_plans = []

    # Create English lesson plans
    for skill_level in activities:
        lesson_plans.append(
            LessonPlan(
                topic=topic,
                grade_level=grade_level,
                state=state,
                objectives=objectives,
                content=content,
                activities=[activities[skill_level]],
                language="en",
                skill_level=skill_level,
            )
        )

    # Translate content and activities to Spanish
    translated_content = await translator.translate(content, "es")
    translated_activities = {
        skill: await translator.translate(activity, "es") for skill, activity in activities.items()
    }

    # Create Spanish lesson plans
    for skill_level in translated_activities:
        lesson_plans.append(
            LessonPlan(
                topic=topic,
                grade_level=grade_level,
                state=state,
                objectives=objectives,
                content=translated_content,
                activities=[translated_activities[skill_level]],
                language="es",
                skill_level=skill_level,
            )
        )

    return lesson_plans

async def process_pdf_workflow(
    pdf_text: str, grade_level: int, objectives: List[str], state: str
) -> List[LessonPlan]:
    """
    Process a PDF input into six lesson plans.
    """
    parser = ParsingAgent()
    parse_result = await parser.parse_pdf(pdf_text)
    return await process_plaintext_workflow(
        parse_result.topic, parse_result.summary, grade_level, objectives, state
    )

