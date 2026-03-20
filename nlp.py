import spacy
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# carregar modelo
nlp = spacy.load("pt_core_news_sm")

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str


@app.post("/analyze")
def analisar(req: AnalyzeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="texto vazio")

    erros = _analisar(req.text)
    return {
        "errors": erros,
        "total_errors": len(erros)
    }


def _analisar(texto: str) -> list[dict]:
    doc = nlp(texto)
    erros = []

    # =========================
    # NLP RULES
    # =========================
    for token in doc:

        # helper
        def is_det_noun(t):
            return t.dep_ == "det" and t.head.pos_ == "NOUN"

        # -------------------------
        # concordância nominal (número)
        # -------------------------
        if is_det_noun(token):
            art_plural = token.morph.get("Number") == ["Plur"]
            sub_singular = token.head.morph.get("Number") == ["Sing"]

            if art_plural and sub_singular:
                erros.append({
                    "offset_start": token.idx,
                    "offset_end": token.head.idx + len(token.head.text),
                    "error_type": "concordancia_nominal",
                    "message": f'"{token.text} {token.head.text}" — número não concorda',
                    "suggestion": f'"{token.text} {token.head.text}s" ou "o {token.head.text}"',
                    "confidence": 0.9,
                    "source": "nlp"
                })

        # -------------------------
        # concordância de gênero
        # -------------------------
        if is_det_noun(token):
            art_gender = token.morph.get("Gender")
            noun_gender = token.head.morph.get("Gender")

            if art_gender and noun_gender and art_gender != noun_gender:
                erros.append({
                    "offset_start": token.idx,
                    "offset_end": token.head.idx + len(token.head.text),
                    "error_type": "concordancia_genero",
                    "message": f'"{token.text} {token.head.text}" — gênero não concorda',
                    "suggestion": "ajuste artigo ou substantivo",
                    "confidence": 0.85,
                    "source": "nlp"
                })

        # -------------------------
        # concordância verbal
        # -------------------------
        if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
            suj_plural = token.morph.get("Number") == ["Plur"]
            verb_singular = token.head.morph.get("Number") == ["Sing"]

            if suj_plural and verb_singular:
                erros.append({
                    "offset_start": token.head.idx,
                    "offset_end": token.head.idx + len(token.head.text),
                    "error_type": "concordancia_verbal",
                    "message": f'"{token.head.text}" não concorda com sujeito plural "{token.text}"',
                    "suggestion": "ajuste o verbo para plural",
                    "confidence": 0.85,
                    "source": "nlp"
                })

        # -------------------------
        # "a gente vamos"
        # -------------------------
        if token.text.lower() == "gente" and token.head.pos_ == "VERB":
            if token.head.morph.get("Number") == ["Plur"]:
                erros.append({
                    "offset_start": token.head.idx,
                    "offset_end": token.head.idx + len(token.head.text),
                    "error_type": "concordancia_verbal",
                    "message": '"a gente" exige verbo no singular',
                    "suggestion": "use verbo no singular (ex: vai)",
                    "confidence": 0.9,
                    "source": "nlp"
                })

        if token.pos_ == "VERB":
            if "Inf" in token.morph.get("VerbForm"):
                if token.dep_ == "ROOT":
                    erros.append({
                        "offset_start": token.idx,
                        "offset_end": token.idx + len(token.text),
                        "error_type": "verbo_infinitivo",
                        "message": "verbo no infinitivo pode estar incorreto",
                        "suggestion": "conjugue o verbo",
                        "confidence": 0.6,
                        "source": "nlp"
                    })


    # repetição de palavra
    for i in range(len(doc) - 1):
        if doc[i].text.lower() == doc[i+1].text.lower():
            erros.append({
                "offset_start": doc[i].idx,
                "offset_end": doc[i+1].idx + len(doc[i+1].text),
                "error_type": "repeticao",
                "message": f'palavra repetida "{doc[i].text}"',
                "suggestion": f'remover uma ocorrência de "{doc[i].text}"',
                "confidence": 0.95,
                "source": "nlp"
            })

    # "mim fazer"
    for i in range(len(doc) - 1):
        if doc[i].text.lower() == "mim" and doc[i+1].pos_ == "VERB":
            erros.append({
                "offset_start": doc[i].idx,
                "offset_end": doc[i+1].idx + len(doc[i+1].text),
                "error_type": "pronome",
                "message": 'uso incorreto de "mim" antes de verbo',
                "suggestion": 'use "eu"',
                "confidence": 0.95,
                "source": "heuristica"
            })

    # "mais" vs "mas"
    for i in range(len(doc)):
        if doc[i].text.lower() == "mais":
            if i > 0 and doc[i-1].pos_ == "VERB":
                erros.append({
                    "offset_start": doc[i].idx,
                    "offset_end": doc[i].idx + len(doc[i].text),
                    "error_type": "uso_incorreto",
                    "message": '"mais" pode estar incorreto, talvez "mas"',
                    "suggestion": "verifique se o correto é 'mas'",
                    "confidence": 0.6,
                    "source": "heuristica"
                })

    return erros
