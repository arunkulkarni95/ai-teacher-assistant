from fastapi import FastAPI, File, UploadFile, HTTPException
from workflows.lesson_plan_workflow import process_lesson_plan
import pdfplumber
import asyncio

app = FastAPI()

@app.post("/process-lesson-plan")
async def process_lesson_plan_endpoint(file: UploadFile = File(...), topic: str = "General", target_language: str = "es"):
    """
    Accept a lesson plan upload, translate and differentiate it.
    """
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    try:
        # Extract content from the uploaded file
        content = ""
        if file.content_type == "application/pdf":
            with pdfplumber.open(file.file) as pdf:
                content = " ".join(page.extract_text() for page in pdf.pages)
        elif file.content_type == "text/plain":
            content = (await file.read()).decode("utf-8")

        # Process the lesson plan
        lesson_plan = await process_lesson_plan(topic, content, target_language)
        return lesson_plan.model_dump()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing lesson plan: {str(e)}")
