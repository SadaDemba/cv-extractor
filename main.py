from fastapi import FastAPI
from app.routes import router as cv_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CV Extraction API", version="1.0.0")

# Inclure les routes pour les fonctionnalités
app.include_router(cv_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API d'extraction de CV !"}
