import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

# Adiciona a pasta src ao path do Python
root_dir = Path(__file__).resolve().parent.parent
src_dir = root_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# Importa a aplicação a partir do subpacote atividade_qts1
from atividade_qts1.main import app

@pytest.fixture
def client():
    """Fixture do Pytest para instanciar o cliente de teste do FastAPI com setup/teardown."""
    print("\n[SETUP] A iniciar TestClient do FastAPI...")
    c = TestClient(app)
    yield c
    print("\n[TEARDOWN] A encerrar TestClient...")