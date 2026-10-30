# Product Requirements Document (PRD)
## Sistema de Avaliação de Desempenho Escolar / Universitário

### 1. Visão Geral
Este documento especifica os requisitos funcionais e as regras de negócio para o **Sistema de Avaliação de Desempenho Escolar / Universitário**, desenvolvido como parte do trabalho prático da disciplina de Qualidade e Teste de Software (QTS). O sistema tem como objetivo calcular a média ponderada de notas de um estudante, validar os limites permitidos e determinar o status acadêmico final de forma determinística.

---

### 2. Regras de Negócio (BR - Business Rules)

#### **BR01: Validação de Intervalo das Notas**
- Cada nota informada ($N_1, N_2, N_3$) deve estar estritamente no intervalo fechado entre **0.0 e 10.0**.
- Caso qualquer nota seja menor que `0.0` ou maior que `10.0`, o sistema deve lançar uma exceção do tipo `ValueError`.
- Caso a entrada fornecida não seja um número válido (ex: strings, booleanos ou nulos), o sistema deve lançar uma exceção do tipo `TypeError`.

#### **BR02: Pesos das Avaliações e Soma**
- O cálculo da média ponderada aceita uma tupla de pesos correspondentes às três avaliações (por padrão: $P_1 = 2.0$, $P_2 = 3.0$, $P_3 = 5.0$).
- A soma total dos pesos deve ser estritamente maior que zero. Se a soma for menor ou igual a zero, o sistema deve lançar um `ValueError`.

#### **BR03: Cálculo da Média Ponderada**
- A média ponderada é calculada pela fórmula matemática:
  $$\text{Média} = \frac{(N_1 \cdot P_1) + (N_2 \cdot P_2) + (N_3 \cdot P_3)}{P_1 + P_2 + P_3}$$
- O resultado final da média deve ser arredondado para **2 casas decimais**.

#### **BR04: Determinação do Status Acadêmico**
Com base na média calculada, o sistema classifica o estudante em uma das seguintes categorias:
1. **Aprovado Direto:** Aplicado quando $\text{Média} \ge 7.0$
2. **Recuperação:** Aplicado quando $4.0 \le \text{Média} < 7.0$
3. **Reprovado:** Aplicado quando $\text{Média} < 4.0$
- Valores de média inválidos (fora de $0.0$ a $10.0$ ou tipos incorretos) passados para a função de status devem disparar exceções defensivas (`ValueError` ou `TypeError`).

---

### 3. Requisitos Não Funcionais
- **Tecnologia:** Implementado em Python $\ge 3.12$ com tipagem estática rigorosa (`Type Hints`).
- **Gerenciamento de Dependências:** Utilização do gerenciador `uv`.
- **Qualidade de Testes:** Cobertura de código obrigatória de **100% (Branch Coverage)** validada via `pytest-cov`.