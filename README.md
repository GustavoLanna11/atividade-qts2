# Sistema de Avaliação de Desempenho Escolar / Universitário

Trabalho prático individual desenvolvido para a disciplina de Qualidade e Teste de Software (QTS), focado em engenharia de testes unitários, cobertura de código e governança de IA.

## 📌 Sobre o Domínio
O sistema calcula a média ponderada de notas de um estudante, valida os limites permitidos (notas de 0.0 a 10.0) e determina o status acadêmico final:
* **Aprovado Direto** ($\text{Média} \ge 7.0$)
* **Recuperação** ($4.0 \le \text{Média} < 7.0$)
* **Reprovado** ($\text{Média} < 4.0$)

Validações defensivas adicionais garantem o lançamento de exceções para entradas inválidas (ex: notas fora do intervalo válido).

---

## 🛠️ Requisitos Técnicos
* **Python** $\ge 3.12$
* **Gerenciador de Dependências:** `uv`

---

## 🚀 Instruções de Execução

### 1. Clonar o repositório e configurar o ambiente
Certifique-se de ter o `uv` instalado em sua máquina. No terminal, na raiz do projeto, execute:

```bash
# Sincronizar as dependências e criar o ambiente virtual
uv sync
```

### 2. Executar os Testes Unitários
Para rodar a suíte completa de testes unitários com o Pytest em modo verboso:

```bash
uv run pytest -v
```

### 3. Verificar a Cobertura de Código (100% Branch Coverage)
Para rodar os testes medindo a cobertura de linhas e ramificações (*branch coverage*) no módulo de negócio:

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

---

## 📂 Estrutura do Repositório
* `PRD.md`: Especificação dos requisitos e regras de negócio.
* `AI_USAGE.md`: Relatório de transparência sobre o uso de IA e auditoria.
* `.cursorrules`: Regras de contexto utilizadas no desenvolvimento assistido por IA.
* `src/`: Código-fonte principal do domínio (SUT).
* `tests/`: Suíte de testes unitários (`@pytest.mark.unit`, parametrização, BVA, EP e Error Guessing).
