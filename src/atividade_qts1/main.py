from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Sistema de Avaliação Escolar - QTS",
    description="API e Interface Web para gestão de notas e verificação de status académico",
    version="2.0.0"
)

class AlunoSchema(BaseModel):
    nome: str = Field(..., min_length=2)
    nota1: float = Field(..., ge=0.0, le=10.0)
    nota2: float = Field(..., ge=0.0, le=10.0)
    nota3: float = Field(..., ge=0.0, le=10.0)

def calcular_media_e_status(n1: float, n2: float, n3: float) -> dict:
    media = round((n1 + n2 + n3) / 3, 2)
    if media >= 7.0:
        status_final = "Aprovado Direto"
    elif media >= 4.0:
        status_final = "Recuperação"
    else:
        status_final = "Reprovado"
    return {"media": media, "status": status_final}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Painel do Aluno - Consulta de Notas</title>
        <style>
            body { font-family: system-ui, sans-serif; background-color: #f3f4f6; padding: 30px; color: #1f2937; }
            .card { background: white; padding: 24px; border-radius: 8px; max-width: 480px; margin: auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .campo-grupo { margin-bottom: 16px; }
            label { display: block; margin-bottom: 6px; font-weight: bold; }
            input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
            button { background-color: #2563eb; color: white; border: none; padding: 12px; width: 100%; border-radius: 4px; font-weight: bold; cursor: pointer; }
            button:focus, input:focus { outline: 2px solid #2563eb; }
        </style>
    </head>
    <body>
        <main class="card">
            <h1>Sistema de Avaliação Escolar</h1>
            <p>Insira os dados do aluno para calcular a média final e o status do semestre.</p>
            <form id="form-aluno">
                <div class="campo-grupo">
                    <label for="nome">Nome Completo do Aluno</label>
                    <input type="text" id="nome" name="nome" placeholder="Ex: João Silva" required>
                </div>
                <div class="campo-grupo">
                    <label for="nota1">Nota do 1º Bimestre</label>
                    <input type="number" id="nota1" name="nota1" min="0" max="10" step="0.1" required>
                </div>
                <div class="campo-grupo">
                    <label for="nota2">Nota do 2º Bimestre</label>
                    <input type="number" id="nota2" name="nota2" min="0" max="10" step="0.1" required>
                </div>
                <div class="campo-grupo">
                    <label for="nota3">Nota do 3º Bimestre</label>
                    <input type="number" id="nota3" name="nota3" min="0" max="10" step="0.1" required>
                </div>
                <button type="submit" id="btn-calcular">Calcular Média Final</button>
            </form>
        </main>
    </body>
    </html>
    """

@app.post("/api/avaliar", status_code=status.HTTP_200_OK)
def avaliar_aluno(aluno: AlunoSchema):
    resultado = calcular_media_e_status(aluno.nota1, aluno.nota2, aluno.nota3)
    return {
        "aluno": aluno.nome,
        "notas": [aluno.nota1, aluno.nota2, aluno.nota3],
        "media": resultado["media"],
        "status": resultado["status"]
    }