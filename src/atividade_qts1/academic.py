class AcademicEvaluator:
    @staticmethod
    def calcular_media_ponderada(n1: float, n2: float, n3: float, pesos: tuple[float, float, float] = (2.0, 3.0, 5.0)) -> float:
        for i, nota in enumerate([n1, n2, n3], start=1):
            if not isinstance(nota, (int, float)) or isinstance(nota, bool):
                raise TypeError(f"A nota {i} deve ser um número.")
            if not (0.0 <= nota <= 10.0):
                raise ValueError(f"A nota {i} deve estar entre 0.0 e 10.0.")

        p1, p2, p3 = pesos
        soma_pesos = p1 + p2 + p3
        
        if soma_pesos <= 0:
            raise ValueError("A soma dos pesos deve ser maior que zero.")

        media = (n1 * p1 + n2 * p2 + n3 * p3) / soma_pesos
        return round(media, 2)

    @staticmethod
    def determinar_status(media: float) -> str:
        if not isinstance(media, (int, float)) or isinstance(media, bool):
            raise TypeError("A média deve ser um número.")
        if not (0.0 <= media <= 10.0):
            raise ValueError("A média deve estar entre 0.0 e 10.0.")

        if media >= 7.0:
            return "Aprovado Direto"
        elif media >= 4.0:
            return "Recuperação"
        else:
            return "Reprovado"