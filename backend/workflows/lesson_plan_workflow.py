from agents.translation_agent import TranslationAgent
from agents.differentiation_agent import DifferentiationAgent
from models.lesson_plan import LessonPlan
import asyncio

async def process_lesson_plan(topic: str, content: str, target_language: str = "es") -> LessonPlan:
    """
    Translate and differentiate a lesson plan.
    """
    translator = TranslationAgent()
    differentiation = DifferentiationAgent()

    # Perform translation and differentiation in parallel
    translated_content = asyncio.create_task(translator.translate(content, target_language))
    activities = await asyncio.gather(
        differentiation.generate_activity(topic, "struggling"),
        differentiation.generate_activity(topic, "average"),
        differentiation.generate_activity(topic, "advanced")
    )

    return LessonPlan(
        topic=topic,
        objectives=["Understand the basics of the topic", "Apply knowledge in activities"],
        content=await translated_content,
        activities=activities
    )