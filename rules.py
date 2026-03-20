import re

def _analisar(texto: str) -> list[dict]:
    erros = []
    stripped = texto.strip()

    # frase sem ponto final
    if stripped and stripped[-1] not in ".!?":
        erros.append({
            "offset_start": len(stripped) - 1,
            "offset_end": len(stripped),
            "error_type": "pontuacao",
            "message": "frase sem ponto final",
            "suggestion": "adicione . ! ou ?",
            "confidence": 1.0,
            "source": "rules"
        })

    # letra minúscula no início
    if stripped and stripped[0].islower():
        erros.append({
            "offset_start": 0,
            "offset_end": 1,
            "error_type": "capitalizacao",
            "message": "frase começa com letra minúscula",
            "suggestion": stripped[0].upper(),
            "confidence": 0.9,
            "source": "rules"
        })

    # espaços duplos
    for match in re.finditer(r" {2,}", texto):
        erros.append({
            "offset_start": match.start(),
            "offset_end": match.end(),
            "error_type": "espaco_duplo",
            "message": "espaço duplo encontrado",
            "suggestion": " ",
            "confidence": 1.0,
            "source": "rules"
        })

    # espaço antes de pontuação
    for match in re.finditer(r" +[,.!?;:]", texto):
        erros.append({
            "offset_start": match.start(),
            "offset_end": match.end(),
            "error_type": "espaco_pontuacao",
            "message": "espaço antes da pontuação",
            "suggestion": match.group().strip(),
            "confidence": 0.95,
            "source": "rules"
        })

    # reticências incorretas
    for match in re.finditer(r"\.{2}(?!\.)|\\.{4,}", texto):
        erros.append({
            "offset_start": match.start(),
            "offset_end": match.end(),
            "error_type": "reticencias",
            "message": "reticências devem ter exatamente 3 pontos",
            "suggestion": "...",
            "confidence": 0.9,
            "source": "rules"
        })

    # frase muito longa
    palavras = texto.split()
    if len(palavras) > 50:
        erros.append({
            "offset_start": 0,
            "offset_end": len(texto),
            "error_type": "frase_longa",
            "message": f"frase muito longa ({len(palavras)} palavras)",
            "suggestion": "divida em frases menores",
            "confidence": 0.7,
            "source": "rules"
        })

    return erros

