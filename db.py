import sqlite3
import json

conn = sqlite3.connect("grammatik.db", check_same_thread=False)

def init():
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS documents (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            content    TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS analyses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            errors_json TEXT NOT NULL,
            score       REAL NOT NULL,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (document_id) REFERENCES documents(id)
        );
    """)
    conn.commit()
def salvar_analise(conteudo: str, erros: list, score: float):
    cur = conn.execute("INSERT INTO documents (content) VALUES (?)", (conteudo,))
    conn.commit()
    doc_id = cur.lastrowid
    conn.execute(
        "INSERT INTO analyses (document_id, errors_json, score) VALUES (?, ?, ?)",
        (doc_id, json.dumps(erros, ensure_ascii=False), score)
    )
    conn.commit()
    return doc_id

def buscar_historico():
    rows = conn.execute("""
        SELECT d.id, d.content, a.errors_json, a.score, a.created_at
        FROM documents d
        JOIN analyses a ON a.document_id = d.id
        ORDER BY a.created_at DESC
        LIMIT 20
    """).fetchall()
    return [
        {
            "id": r[0],
            "content": r[1],
            "errors": json.loads(r[2]),
            "score": r[3],
            "created_at": r[4]
        }
        for r in rows
    ]
