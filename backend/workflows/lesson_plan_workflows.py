import asyncio
from agents.differentiation_agent import DifferentiationAgent
from agents.translation_agent import TranslationAgent

from typing import List

from agents.parsing_agent import ParsingAgent
from models.lesson_plan import LessonPlan

async def process_plaintext_workflow(topic: str, content: str, grade_level: int, objectives: List[str]) -> List[LessonPlan]:
    """
    Process plaintext input into English and Spanish lesson plans.
    """
    translator = TranslationAgent()
    differentiation = DifferentiationAgent()

    # Perform differentiation
    activities = await asyncio.gather(
        differentiation.generate_activity(topic, "struggling"),
        differentiation.generate_activity(topic, "average"),
        differentiation.generate_activity(topic, "advanced"),
    )

    # Generate English and Spanish versions
    english_lesson = LessonPlan(
        topic=topic,
        grade_level=grade_level,
        objectives=objectives,
        content=content,
        activities=activities,
        language="en",
    )
    spanish_content = await translator.translate(content, "es")
    spanish_activities = await asyncio.gather(
        *(translator.translate(activity, "es") for activity in activities)
    )
    spanish_lesson = LessonPlan(
        topic=topic,
        grade_level=grade_level,
        objectives=objectives,
        content=spanish_content,
        activities=spanish_activities,
        language="es",
    )
    return [english_lesson, spanish_lesson]


async def process_pdf_workflow(pdf_text: str, grade_level: int, objectives: List[str]) -> List[LessonPlan]:
    """
    Process a PDF input into English and Spanish lesson plans.
    """
    parser = ParsingAgent()
    parse_result = await parser.parse_pdf(pdf_text)
    return await process_plaintext_workflow(parse_result.topic, parse_result.summary, grade_level, objectives)

