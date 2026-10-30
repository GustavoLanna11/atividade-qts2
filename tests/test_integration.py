import pytest
from tests.factories import AlunoFactory

@pytest.mark.integration
def test_avaliar_aluno_sucesso(client):
    """Testa a rota de avaliação de alunos usando a massa de dados gerada pelo Faker."""
    dados_aluno = AlunoFactory.criar()
    
    response = client.post("/api/avaliar", json=dados_aluno)
    
    assert response.status_code == 200
    data = response.json()
    assert data["aluno"] == dados_aluno["nome"]
    assert "media" in data
    assert "status" in data

@pytest.mark.integration
def test_avaliar_aluno_com_mock(client, mocker):
    """Testa a integração utilizando mocker.patch para isolar o comportamento de cálculo."""
    # Corrigido para apontar para o caminho exato do módulo importado
    mocker.patch(
        "atividade_qts1.main.calcular_media_e_status",
        return_value={"media": 8.5, "status": "Aprovado Direto"}
    )
    
    dados_aluno = AlunoFactory.criar()
    response = client.post("/api/avaliar", json=dados_aluno)
    
    assert response.status_code == 200
    data = response.json()
    assert data["media"] == 8.5
    assert data["status"] == "Aprovado Direto"

@pytest.mark.integration
def test_avaliar_aluno_dados_invalidos(client):
    """Testa o comportamento da API ao receber notas inválidas (fora do intervalo 0-10)."""
    dados_invalidos = {
        "nome": "Aluno Teste",
        "nota1": 15.0,  # Inválido (máximo é 10.0)
        "nota2": 5.0,
        "nota3": 6.0
    }
    
    response = client.post("/api/avaliar", json=dados_invalidos)
    
    # O Pydantic deve rejeitar com erro 422 (Unprocessable Entity)
    assert response.status_code == 422