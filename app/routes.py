from fastapi import APIRouter, File, UploadFile, HTTPException
from .services import extract_cv

router = APIRouter()

# Définir une taille maximale (en octets)
MAX_FILE_SIZE = 3 * 1024 * 1024  # 5 Mo

@router.post("/extract/")
async def extract_data_from_cv(file: UploadFile = File(...)):
    """
    Endpoint pour extraire les informations d'un CV.
    """

    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Seuls les fichiers PDF ou DOCX sont acceptés.")
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Le fichier ne doit pas dépasser 10 Mo")

    data = await extract_cv(file)
    return {"extracted_data": data}
