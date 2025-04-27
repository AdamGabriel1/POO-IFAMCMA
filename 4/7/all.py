class Sala:
    def __init__(self, bloco: int, sala: int, capacidade: int):
        self.bloco = bloco
        self.sala = sala
        self.capacidade = capacidade

    def getDescricao(self):
        return f"Bloco {self.bloco}, Sala {self.sala} ({self.capacidade} lugares)"

class Turma:
    def __init__(self, nome: str, professor: str, numAlunos: int, horarios: list = None):
        self.nome = nome
        self.professor = professor
        self.numAlunos = numAlunos
        self.horarios = horarios if horarios is not None else []

    def addHorario(self, horario: int):
        if 1 <= horario <= 25 and horario not in self.horarios:
            self.horarios.append(horario)

    def getHorariosString(self) -> str:
        horariosDias = {
            1: ("Segunda", "07:15"), 2: ("Terça", "07:15"), 3: ("Quarta", "07:15"),
            4: ("Quinta", "07:15"), 5: ("Sexta", "07:15"), 6: ("Segunda", "08:05"),
            7: ("Terça", "08:05"), 8: ("Quarta", "08:05"), 9: ("Quinta", "08:05"),
            10: ("Sexta", "08:05"), 11: ("Segunda", "09:10"), 12: ("Terça", "09:10"),
            13: ("Quarta", "09:10"), 14: ("Quinta", "09:10"), 15: ("Sexta", "09:10"),
            16: ("Segunda", "10:00"), 17: ("Terça", "10:00"), 18: ("Quarta", "10:00"),
            19: ("Quinta", "10:00"), 20: ("Sexta", "10:00"), 21: ("Segunda", "10:50"),
            22: ("Terça", "10:50"), 23: ("Quarta", "10:50"), 24: ("Quinta", "10:50"),
            25: ("Sexta", "10:50")
        }
        horariosStr = [f"{horariosDias[horario][0]} {horariosDias[horario][1]}h" for horario in self.horarios if horario in horariosDias]
        return ", ".join(horariosStr)

    def getDescricao(self) -> str:
        return (f"Turma: {self.nome}\nProfessor: {self.professor}\n"
                f"Número de alunos: {self.numAlunos}\nHorários: {self.getHorariosString()}")

class TurmaEmSala:
    def __init__(self, turma: Turma, sala: Sala):
        self.turma = turma
        self.sala = sala

class Ensalamento:
    def __init__(self):
        self.salas = []
        self.turmas = []
        self.ensalamento = []

    def addSala(self, sala):
        self.salas.append(sala)

    def addTurma(self, turma):
        self.turmas.append(turma)

    def salaDisponivel(self, sala: Sala, horarios: list) -> bool:
        for a in self.ensalamento:
            if a.sala == sala and any(horario in a.turma.horarios for horario in horarios):
                return False
        return True

    def alocar(self, turma: Turma, sala: Sala) -> bool:
        if turma.numAlunos <= sala.capacidade and self.salaDisponivel(sala, turma.horarios):
            self.ensalamento.append(TurmaEmSala(turma, sala))
            return True
        return False

    def alocarTodas(self):
        for turma in self.turmas:
            alocada = False
            for sala in self.salas:
                if self.alocar(turma, sala):
                    alocada = True
                    break
            if not alocada:
                print(f"Turma {turma.nome} não foi alocada.")

    def getTotalTurmasAlocadas(self):
        return len(self.ensalamento)

    def getTotalEspacoLivre(self):
        total = 0
        for a in self.ensalamento:
            total += a.sala.capacidade - a.turma.numAlunos
        return total

    def relatorioResumoEnsalamento(self):
        totalSalas = len(self.salas)
        totalTurmas = len(self.turmas)
        turmasAlocadas = self.getTotalTurmasAlocadas()
        espacosLivres = self.getTotalEspacoLivre()
        
        return (f"Total de Salas: {totalSalas}\n"
                f"Total de Turmas: {totalTurmas}\n"
                f"Turmas alocadas: {turmasAlocadas}\n"
                f"Espaços livres: {espacosLivres}\n")

    def relatorioTurmasPorSala(self):
        relatorio = self.relatorioResumoEnsalamento()
        
        salasTurmas = {}
        for a in self.ensalamento:
            salaChave = (a.sala.bloco, a.sala.sala)
            if salaChave not in salasTurmas:
                salasTurmas[salaChave] = []
            salasTurmas[salaChave].append(a.turma)

        for (bloco, sala), turmas in salasTurmas.items():
            relatorio += (f"---Bloco: {bloco}, Sala: {sala} ({self.salas[0].capacidade} lugares)---\n")
            for turma in turmas:
                relatorio += f"\n{turma.getDescricao()}\n"
        
        return relatorio

class EnsalamentoMain:
    def mainSala(self):
        sala1 = Sala(1, 49, 50)
        sala1.getDescricao()
        
    def mainTurma(self):
        turma1 = Turma("Fund de Redes de Computadores", "Luiz Carlos", 50, [1,6])

        turma2 = Turma("Programacao Web", "Fredy Veras", 50, [13,3,8])

        turma3 = Turma("Topicos Especiais em Informatica", "Fredy Veras", 50, [19])

        turma4 = Turma("Projeto Integrador", "Luiz Carlos", 50, [2,7])

        turma5 = Turma("Programacao Orientada Objetos", "Yuri Assayag", 50, [17,22,4,9])

        turma6 = Turma("Programacao para Dispositivos Moveis", "Yuri Assayag", 50, [15,20,25])
        
        turmas=[turma1,turma2,turma3,turma4,turma5, turma6]
        
        for turma in turmas:
            print(f"{turma.getDescricao()}\n")
        
    def mainAll(self):
        sala1 = Sala(1, 49, 50)
        
        turma1 = Turma("Fund de Redes de Computadores", "Luiz Carlos", 50)
        turma1.addHorario(1)  # Segunda 07:15
        turma1.addHorario(6)  # Segunda 08:05

        turma2 = Turma("Programacao Web", "Fredy Veras", 50)
        turma2.addHorario(13)  # Quarta 09:10
        turma2.addHorario(3)   # Quarta 07:15
        turma2.addHorario(8)   # Quarta 08:05

        turma3 = Turma("Topicos Especiais em Informatica", "Fredy Veras", 50)
        turma3.addHorario(19)  # Quinta 10:00

        turma4 = Turma("Projeto Integrador", "Luiz Carlos", 50)
        turma4.addHorario(2)   # Terça 07:15
        turma4.addHorario(7)   # Terça 08:05

        turma5 = Turma("Programacao Orientada Objetos", "Yuri Assayag", 50)
        turma5.addHorario(17)  # Terça 10:00
        turma5.addHorario(22)  # Terça 10:50
        turma5.addHorario(4)   # Quinta 07:15
        turma5.addHorario(9)   # Quinta 08:05

        turma6 = Turma("Programacao para Dispositivos Moveis", "Yuri Assayag", 50)
        turma6.addHorario(15)  # Sexta 09:10
        turma6.addHorario(20)  # Sexta 10:00
        turma6.addHorario(25)  # Sexta 10:50

        ensalamento = Ensalamento()
        ensalamento.addSala(sala1)
        ensalamento.addTurma(turma1)
        ensalamento.addTurma(turma2)
        ensalamento.addTurma(turma3)
        ensalamento.addTurma(turma4)
        ensalamento.addTurma(turma5)
        ensalamento.addTurma(turma6)

        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())
        
    def teste1(self):
        # Número de alunos maior do que a sala comporta.
        sala1 = Sala(1, 49, 40)
        turma1 = Turma("Fund de Redes de Computadores", "Luiz Carlos", 50, [1,6])
        ensalamento = Ensalamento()
        ensalamento.addSala(sala1)
        ensalamento.addTurma(turma1)
        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())
    
    def teste2(self):
        # Horários conflitantes
        sala1 = Sala(1, 49, 50)
        turma2 = Turma("Programacao Web", "Fredy Veras", 50, [19])
        turma3 = Turma("Topicos Especiais em Informatica", "Fredy Veras", 50, [19])
        ensalamento = Ensalamento()
        ensalamento.addSala(sala1)
        ensalamento.addTurma(turma2)
        ensalamento.addTurma(turma3)
        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())
    
    def teste3(self):
        # Alocação de várias turmas em uma sala
        sala1 = Sala(1, 50, 50)
        turma1 = Turma("Matematica", "Kleber", 30, [1, 6])
        turma2 = Turma("Física", "Rose Maria", 20, [3, 4])
        turma3 = Turma("Química", "Luiz Antonio", 15, [5, 11])
        ensalamento = Ensalamento()
        ensalamento.addSala(sala1)
        ensalamento.addTurma(turma1)
        ensalamento.addTurma(turma2)
        ensalamento.addTurma(turma3)
        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())

    def teste4(self):
        # Turma com horários não conflitantes
        sala2 = Sala(1, 51, 50)
        turma4 = Turma("Biologia", "Heloide", 40, [2, 8])
        turma5 = Turma("História", "Rhaisa Laranjeira", 30, [10, 12])
        ensalamento = Ensalamento()
        ensalamento.addSala(sala2)
        ensalamento.addTurma(turma4)
        ensalamento.addTurma(turma5)
        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())

    def teste5(self):
        # Teste com uma sala vazia
        sala3 = Sala(1, 52, 50)
        turma6 = Turma("Geografia", "Petrucio", 25, [25])
        ensalamento = Ensalamento()
        ensalamento.addSala(sala3)
        ensalamento.addTurma(turma6)
        ensalamento.alocarTodas()
        print(ensalamento.relatorioTurmasPorSala())

    def mainTestes(self):
        testes = [self.teste1, self.teste2, self.teste3, self.teste4, self.teste5]
        n = 1
        for i in testes:
            print(f"\nTeste {n}: \n")
            i()
            n += 1

main = EnsalamentoMain()
print("Atividade:\n")
main.mainAll()
print("")
print("="*75)
print("\n\nTestes:\n")
main.mainTestes()