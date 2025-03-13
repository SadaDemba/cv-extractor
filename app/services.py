import os
from fastapi import UploadFile, File
from .utils import extract_text_from_pdf, parse_cv_with_openai


async def extract_cv(file: UploadFile = File(...)):
    # Sauvegarder temporairement le fichier
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    try:
        # Extraction du texte avec pdfminer
        cv_text = extract_text_from_pdf(file.filename)

        # Parsing avec OpenAI
        user_model = parse_cv_with_openai(cv_text)

        return user_model
    finally:
        # Nettoyer le fichier temporaire
        os.remove(file.filename)
