# Relatório de Transparência de Uso de Inteligência Artificial (AI_USAGE.md)

Este documento descreve de forma transparente o papel das ferramentas de Inteligência Artificial no desenvolvimento deste trabalho prático para a disciplina de Qualidade e Teste de Software (QTS).

## 1. Ferramentas Utilizadas
- **Assistente de IA:** Google Gemini.
- **Ambiente de Desenvolvimento (IDE):** Visual Studio Code.
- **Gerenciador de Dependências:** `uv` (Python 3.12+).


## 2. Como a IA foi Empregada
A Inteligência Artificial (Google Gemini) foi utilizada como suporte técnico nas seguintes etapas:
- **Especificação de Requisitos (PRD):** Auxílio na estruturação inicial das regras de negócio determinísticas para o sistema de avaliação escolar (cálculo de média ponderada e limites de notas).
- **Implementação do Domínio (SUT):** Apoio na escrita do código em Python, aplicando boas práticas de tipagem estática (*Type Hints*) e tratamento defensivo de exceções (`ValueError` e `TypeError`).
- **Suíte de Testes Unitários:** Geração orientada de casos de teste parametrizados aplicando técnicas de caixa branca e preta, nomeadamente **Particionamento de Equivalência (EP)**, **Análise do Valor Limite (BVA)** e **Error Guessing**.

## 3. Auditoria e Validação Humana
Todo o código gerado pelo Gemini foi rigorosamente auditado e validado pelo autor do projeto:
1. **Revisão Crítica:** O código foi verificado linha por linha para garantir conformidade com os padrões da linguagem e com as regras de negócio exigidas no PRD.
2. **Execução de Testes:** A suíte de testes foi validada diretamente no terminal utilizando o framework `pytest`:
   ```bash
   uv run pytest -v