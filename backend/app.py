from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from workflows.lesson_plan_workflows import process_plaintext_workflow, process_pdf_workflow
import pdfplumber
import asyncio
import logfire

logfire.configure()

app = FastAPI()

class PlaintextInput(BaseModel):
    topic: str
    content: str
    grade_level: int
    objectives: List[str]
    state: str

@app.post("/process-plaintext")
async def process_plaintext(input: PlaintextInput):
    """
    Endpoint to process plaintext lesson plans.
    """
    lesson_plans = await process_plaintext_workflow(
        input.topic, input.content, input.grade_level, input.objectives, input.state
    )
    return [lesson_plan.dict() for lesson_plan in lesson_plans]

@app.post("/process-pdf")
async def process_pdf(
    file: UploadFile = File(...), grade_level: int = 4, objectives: List[str] = [], state: str = "Maryland"
):
    """
    Endpoint to process PDF lesson plans.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF.")
    try:
        with pdfplumber.open(file.file) as pdf:
            pdf_text = " ".join(page.extract_text() for page in pdf.pages)
        lesson_plans = await process_pdf_workflow(pdf_text, grade_level, objectives, state)
        return [lesson_plan.dict() for lesson_plan in lesson_plans]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))