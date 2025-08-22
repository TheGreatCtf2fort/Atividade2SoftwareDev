# Atividade2SoftwareDev

from enum import nonmember


class Curso:
    __Identificador = nonmember

    def __init__(self, nome, professor, horas):
        self.nome = nome
        self.professor = professor
        self.horas = horas

    def myfunc(self):
        print("Nome do curso: " + self.nome +
              " Professor: " + self.professor +
              " Horas complementares: " + self.horas +
              " Local: " + self.local)

class Presencial(Curso):



class EaD(Curso):
    def __init__(self, nome, professor, horas):
        super()-__init__(nome, professor, horas)


c1 = Curso("POO", "Thomas", "220", "Sala 303")
c1.myfunc()
