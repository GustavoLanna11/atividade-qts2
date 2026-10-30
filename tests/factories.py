from faker import Faker

fake = Faker("pt_BR")

class AlunoFactory:
    @staticmethod
    def criar():
        return {
            "nome": fake.name(),
            "nota1": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1),
            "nota2": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1),
            "nota3": round(fake.pyfloat(min_value=0.0, max_value=10.0, right_digits=1), 1)
        }