import pytest
from src.atividade_qts1.academic import AcademicEvaluator


# ================= Testes parametrizados =====================
@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3, pesos, esperado",
    [
        (10.0, 10.0, 10.0, (1.0, 1.0, 1.0), 10.0),
        (0.0, 0.0, 0.0, (1.0, 1.0, 1.0), 0.0),
        (5.0, 5.0, 5.0, (1.0, 1.0, 1.0), 5.0),
        (7.0, 8.0, 9.0, (2.0, 3.0, 5.0), 8.3),
    ]
)

# ================= Padrão AAA =======================
def test_calcular_media_ponderada_sucesso(n1, n2, n3, pesos, esperado):
    # Arrange & Act
    resultado = AcademicEvaluator.calcular_media_ponderada(n1, n2, n3, pesos)
    
    # Assert
    assert resultado == esperado

@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3, expected_status",
    [
        (7.0, 7.0, 7.0, "Aprovado Direto"),
        (10.0, 10.0, 10.0, "Aprovado Direto"),
        (4.0, 4.0, 4.0, "Recuperação"),
        (6.9, 6.9, 6.9, "Recuperação"),
        (3.9, 3.9, 3.9, "Reprovado"),
        (0.0, 0.0, 0.0, "Reprovado"),
    ]
)

# ================= Análise de Limites ======================
def test_determinar_status_limites_e_ep(n1, n2, n3, expected_status):
    # Arrange
    media = AcademicEvaluator.calcular_media_ponderada(n1, n2, n3)
    
    # Act
    status = AcademicEvaluator.determinar_status(media)
    
    # Assert
    assert status == expected_status

@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3",
    [
        (-0.1, 5.0, 5.0),
        (10.1, 5.0, 5.0),
        (5.0, -1.0, 5.0),
        (5.0, 11.0, 5.0),
        (5.0, 5.0, -0.01),
        (5.0, 5.0, 10.01),
    ]
)

# ===================== Error Guessing ==========================
def test_error_guessing_notas_fora_dos_limites(n1, n2, n3):
    with pytest.raises(ValueError):
        AcademicEvaluator.calcular_media_ponderada(n1, n2, n3)

@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3",
    [
        ("10", 5.0, 5.0),
        (5.0, None, 5.0),
        (5.0, 5.0, [5.0]),
    ]
)
def test_error_guessing_tipos_invalidos_notas(n1, n2, n3):
    with pytest.raises(TypeError):
        AcademicEvaluator.calcular_media_ponderada(n1, n2, n3)

@pytest.mark.unit
def test_error_guessing_pesos_invalidos():
    with pytest.raises(ValueError):
        AcademicEvaluator.calcular_media_ponderada(5.0, 5.0, 5.0, pesos=(-1.0, -1.0, -1.0))

@pytest.mark.unit
@pytest.mark.parametrize(
    "media_invalida",
    [-0.1, 10.1, "7.0", None]
)
def test_error_guessing_status_invalido(media_invalida):
    if isinstance(media_invalida, str) or media_invalida is None:
        with pytest.raises(TypeError):
            AcademicEvaluator.determinar_status(media_invalida)
    else:
        with pytest.raises(ValueError):
            AcademicEvaluator.determinar_status(media_invalida)