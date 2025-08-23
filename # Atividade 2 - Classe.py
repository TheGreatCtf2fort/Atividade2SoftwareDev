# Atividade 2 - Classe

class Curso:
    def __init__(self, nome, professor, horas, local):
        self.nome = nome
        self.professor = professor
        self.horas = horas
        self.local = local

    def myfunc(self):
        print(f"Curso Presencial: {self.nome} Professor: {self.professor} "
              f"Horas: {self.horas} Local: {self.local}")

# Subclasse Presencial
class Presencial(Curso):
    pass

# Subclasse EaD com override
class EaD(Curso):
    def __init__(self, nome, professor, horas):
        super().__init__(nome, professor, horas, "Online")

    # Sobrescrevendo método da classe base
    def myfunc(self):
        print(f"Curso EaD: {self.nome} Professor: {self.professor} "
              f"Horas: {self.horas} Plataforma: {self.local}")

c1 = Presencial("POO", "Thomas", "220", "Sala 303")
c2 = EaD("Banco de Dados", "Carla", "180")

c1.myfunc()
c2.myfunc()
