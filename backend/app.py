from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import File
from services.file_processor import FileProcessor

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

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

    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "merged_text": merged_text
        }
    )