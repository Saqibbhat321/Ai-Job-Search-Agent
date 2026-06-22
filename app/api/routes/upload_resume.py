import os
import tempfile

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException

from app.resume.parser import ResumeParser
from app.resume.resume_matcher import ResumeMatcher


router = APIRouter()

matcher = ResumeMatcher()


@router.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    filename = file.filename.lower()

    suffix = os.path.splitext(
        filename
    )[1]

    if suffix not in [
        ".pdf",
        ".docx",
        ".txt"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are supported"
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        content = await file.read()

        temp_file.write(content)

        temp_path = temp_file.name

    try:

        if suffix == ".pdf":

            resume_text = ResumeParser.parse_pdf(
                temp_path
            )

        elif suffix == ".docx":

            resume_text = ResumeParser.parse_docx(
                temp_path
            )

        else:

            with open(
                temp_path,
                "r",
                encoding="utf-8"
            ) as file:

                resume_text = file.read()

        results = matcher.match_resume(
            resume_text
        )

        return {
            "filename": filename,
            "recommendations": results
        }

    finally:

        if os.path.exists(
            temp_path
        ):

            os.remove(
                temp_path
            )