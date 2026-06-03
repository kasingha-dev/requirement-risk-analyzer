from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import File
from services.file_processor import FileProcessor
from services.gap_analyzer import GapAnalyzer
from services.risk_analyzer import RiskAnalyzer
from services.question_generator import QuestionGenerator
from services.architecture_analyzer import ArchitectureAnalyzer
from services.report_generator import ReportGenerator
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from services.pdf_generator import PDFGenerator

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.requirement_extractor import RequirementExtractor

app = FastAPI()
latest_report = None

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/analyze")
async def analyze(
    request: Request,
    files: list[UploadFile] = File(...)
):

    documents = []

    for file in files:
        text = FileProcessor.extract_text(file)
        documents.append(text)

    merged_text = FileProcessor.merge_documents(documents)
    requirements = RequirementExtractor.extract_requirements(
        merged_text
    )

    missing_requirements = GapAnalyzer.analyze(
    requirements
    )

    risks = RiskAnalyzer.analyze(
        requirements
    )

    questions = QuestionGenerator.generate(
    requirements,
    missing_requirements,
    risks
    )

    architecture_concerns = (
    ArchitectureAnalyzer.analyze(
        requirements
    )
    )

    report = ReportGenerator.generate(
        requirements=requirements,
        missing_requirements=missing_requirements,
        risks=risks,
        questions=questions,
        architecture_concerns=architecture_concerns
    )

    global latest_report

    latest_report = report

    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "report": report
        }
    )


@app.get("/download-pdf")
async def download_pdf():

    global latest_report

    if latest_report is None:
        return {"error": "No report available"}

    pdf_bytes = PDFGenerator.generate(
        latest_report
    )

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=analysis_report.pdf"
        }
    )