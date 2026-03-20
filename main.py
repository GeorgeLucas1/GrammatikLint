from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import init, salvar_analise, buscar_historico
from nlp import _analisar as analisar_nlp
from  rules  import _analisar as analisar_rules

app = FastAPI(title="GrammatikLint")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str

@app.on_event("startup")
def startup():
    init()

@app.post("/analyze")
def analisar(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="texto vazio")

    erros = analisar_nlp(req.text) + analisar_rules(req.text)
    total = len(erros)
    score = max(0.0, 100.0 - (total * 10))

    salvar_analise(req.text, erros, score)

    return {
        "errors": erros,
        "total_errors": total,
        "quality_score": score
    }

@app.get("/history")
def historico():
    return buscar_historico()

@app.get("/health")
def health():
    return {"status": "ok"}