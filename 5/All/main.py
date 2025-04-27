# Professor João Renato        
# Classes Normais
from Classes import Ave, Cachorro # Animais
from Classes import Calendario, Cronograma # Datas/Gerenciamento
from Classes import Cliente, Barraquinha, Produto, Loja # Estabelecimentos
from Classes import Caneca, Copo, Taca, Jarra # Recipientes
from Classes import Celular, Relogio, Relogioatt # Objetos
from Classes import Aviao, Carro, Moto, Motoatt # Veiculos

# Classes Abstratas
from Classes import VIP # Ex 1
from Classes import Retangulo, Triangulo # Ex 2
from Classes import TriAtleta # Ex 3
from Classes import ContaCorrente, Poupanca, ContaImposto # Ex4

# Interfaces
from Classes import Menu # Ex 1
from Classes import InfoClientePessoaFisica, InfoClientePessoaJuridica, ClienteFidelizacao # Ex 2

# Relacionamentos
from Classes import Farol, MotoR, Pedido # Ex 1
from Classes import ItemPedido # Ex 2
# Lista de Exercícios/Ex 3
from Classes import DVDPLAYER, DVDMIDIA # Ex 1
from Classes import Pessoa, Musico, Engenheiro # Ex 2
from Classes import Baterista, Saxofonista, Musico2, Orquestra # Ex 3
from Classes import Baterista2, Saxofonista2, Musico3, Orquestra2 # Ex 4
from Classes import Aluno, Curso # Ex 5
from Classes import Casa, TabuleiroDeXadrez # Ex 6
from Classes import C1, C2, PropriedadesDaRelacao # Ex 7
from Classes import School, Department, Student, Course, Instructor # Ex 8
from Classes import Carro2 # Ex 4 

# Professor Yuri
# Exercicios
from Classes import Mestre, Sensor, Conexao, Astromech # Ex 1
from Classes import IniciadoJedi, TreinadorJedi, SessaoJedi # Ex 2
from Classes import EnsalamentoMain
from Classes import Atividades
from Classes import Animal2, Cachorro2, Gato2
from Classes import FormaGeometrica, Circulo, Retangulo
from Classes import Pessoa2, Professor2, Aluno2
from Classes import SerVivo, Macaco, Humano

# Meus Projetos
from Classes import Utilitarios

def verificar_classes():
    print("|=========================|")
    print("|         Classes         |")
    print("|1. Classes Normais       |")
    print("|2. Classes Abstratas     |")
    print("|3. Interfaces            |")
    print("|4. Relacionamentos       |")
    print("|5. Professor: Yuri       |")
    print("|6. Meus Projetos         |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o tipo de Exercícios de Classes que voce quer usar: ")
    print(f"O tipo de Exercícios de Classes que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            print("Fim do Programa.")
            exit

        case "1":
            cn()

        case "2":
            ca()
            
        case "3":
            inter()
            
        case "4":
            rela()
            
        case "5":
            yuri()
            
        case "6":
            proj()

        case _:
            print("Tipo de Exercícios de Classes errado tente novamente:")
            verificar_classes()

def cn():
    print("|=========================|")
    print("|         Metodos         |")
    print("|1. Animais               |")
    print("|2. Datas/Gerenciamento   |")
    print("|3. Estabelecimentos      |")
    print("|4. Recipientes           |")
    print("|5. Objetos               |")
    print("|6. Veiculos              |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()

        case "1":
            animais()

        case "2":
            datas_gerenciamento()

        case "3":
            estabelecimentos()

        case "4":
            recipientes()
            
        case "5":
            objetos()

        case "6":
            veiculos()

        case _:
            print("Metodo errado tente novamente:")
            cn()

def animais():
    print("|=========================|")
    print("|         Animais         |")
    print("|1. Ave                   |")
    print("|2. Cachorro              |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            galinha=Ave("Galinha","Sim","5 kg")
            bemteve=Ave("Bem-te-vi","Não","2 kg")

            galinha.voar()
            bemteve.voar()
                
        case "2":
            Doberman=Cachorro("Dob","Doberman",15,"Preto e Branco",20,16,"Macho","Nome")

            print(f"Nome: {Doberman.nome}")
            print(f"Raça: {Doberman.raca}")
            print(f"Idade: {Doberman.idade}")
            print(f"Cor: {Doberman.cor}")
            print(f"Altura: {Doberman.altura}cm")
            print(f"Peso: {Doberman.peso}kg")
            print(f"Gênero: {Doberman.genero}")
            print(f"Nome do Dono: {Doberman.dono}")

            Doberman.latir()
            Doberman.andar()
            Doberman.comer()
            Doberman.brincar()
            Doberman.fazer_truques()
            Doberman.receber_carinho()
            Doberman.definir_dono("Novo Nome")
            print(f"Nome do Dono: {Doberman.dono}")

        case _:
            print("Metodo errado tente novamente:")
            animais()

def datas_gerenciamento():
    print("|=========================|")
    print("|  Datas e Gerenciamento  |")
    print("|1. Calendario            |")
    print("|2. Cronograma            |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            cal = Calendario(2024,None,None,1)

            cal.add_evento(1,"Teste1")
            cal.add_evento(2,"Teste2")
            cal.rm_evento(1, "Teste1")

            cal.visu_eventos(2)
            cal.visu_mes("Janeiro")
            cal.visu_ano()

            cal.verif_feriado(2)

            cal.proximo_dia(2024, "Fevereiro", 28)

            cal.mostrar_meses_por_periodo("bimestre")
            cal.mostrar_meses_por_periodo("trimestre")
            cal.mostrar_meses_por_periodo("semestre")

            cal.mostrar_calendario_xml()
                
        case "2":
            c=Cronograma()
            c.opcs()

        case _:
            print("Metodo errado tente novamente:")
            datas_gerenciamento()

def estabelecimentos():
    print("|=========================|")
    print("|     Estabelecimentos    |")
    print("|1. Cliente               |")
    print("|2. Barraquinha           |")
    print("|3. Loja                  |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            joao=Cliente("Joao da Silva",23632,"06/06/1995","Rua A, Bairro B, Maues-AM")

            print(joao.nome)

            maria=Cliente("Maria Alburquerque", "65456", "11/11/2000", "Rua B, 2, Bairro A, Maues-AM")
            print(maria.endereco)

            print(joao.endereco)
            joao.mudar_endereco("Rua C, 3, Bairro X, Maues-AM")
            print(joao.endereco)

            maria.fazer_emprestimo('2000')
            joao.fazer_emprestimo('30')

        case "2":
            Barraquinha1=Barraquinha("Barraquinha de Maués", "Bairro: A, Rua: A, Número: A", "123456789", "barraquinha@email.com", 1.2356, 0.243657,
                                     "Carne: Temos\n"
                                     "Frango: Temos\n"
                                     "Suco: Temos\n"
                                     "Lanche: Não Temos", True, True, 40)
            Barraquinha1.info()
            Barraquinha1.funcionamento=False
            Barraquinha1.delivery=False
            Barraquinha1.taxa_delivery=0
            Barraquinha1.info()

        case "3":
            l1 = Loja("Loja de Maués", "Bairro: A, Rua: A, Número: A", "123456789", "loja@email.com", 6, 18)
            l1.info()

            produto1 = Produto("Camiseta", 20, 100)
            produto2 = Produto("Calça Jeans", 50, 50)
            l1.adicionar_produto(produto1)
            l1.adicionar_produto(produto2)

            l1.esta_aberta(10)

            l1.atualizar_estoque("Camiseta", 80)

            l1.listar_produtos()

            l1.buscar_produto("Calça Jeans")

        case _:
            print("Metodo errado tente novamente:")
            estabelecimentos()
            
def recipientes():
    print("|=========================|")
    print("|       Recipientes       |")
    print("|1. Ex da Aula            |")
    print("|2. Caneca                |")
    print("|3. Copo                  |")
    print("|4. Taça                  |")
    print("|5. Jarra                 |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            print("Aqui serao testadas as classes...")
            
            copoAmericano=Copo(0.25,0.2,0.3,"vidro","americano")

            copoAmericano.Calcular_volume()

            print(copoAmericano.altura)
            copoAmericano.altura=0.4
            print("Novo valor da altura...")
            print(copoAmericano.altura)
            
        case "2":
            
            caneca = Caneca(5, 5, 10, "cerâmica", "moderno", "redonda")
            caneca.Calcular_volume()
            caneca.Encher()
            caneca.Esvaziar()
            
        case "3":

            copo = Copo(4, 4, 8, "vidro", "clássico")
            copo.Calcular_volume()
            copo.Encher()
            copo.Esvaziar()
            
        case "4":

            taca = Taca(6, 4, 12, "vidro", "elegante", "vinho")
            taca.Calcular_volume()
            taca.Encher()
            taca.Esvaziar()
            
        case "5":

            jarra = Jarra(8, 6, 15, "vidro", "moderno", "2 litros")
            jarra.Calcular_volume()
            jarra.Encher()
            jarra.Esvaziar()
            
        case _:
            print("Metodo errado tente novamente:")
            recipientes()

def objetos():
    print("|=========================|")
    print("|         Objetos         |")
    print("|1. Celular               |")
    print("|2. Relogio               |")
    print("|3. Relogioatt            |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            c1=Celular()
            c1.especificacoes()

        case "2":
            r=Relogio(60,60,24,30,"Janeiro",2024)

            r.all_f()


        case "3":
            r=Relogioatt(60,60,24,30,"Janeiro",2024)

            r.all_f()

        case _:
            print("Metodo errado tente novamente:")
            objetos()

def veiculos():
    print("|=========================|")
    print("|         Veiculos        |")
    print("|1. Avião                 |")
    print("|2. Carro                 |")
    print("|3. Moto                  |")
    print("|4. Motoatt               |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            cn()

        case "1":
            aviao1 = Aviao("Emirates", "Boeing 777", 2015, "Branco", "Turbofan", "Automática", 900, 10000000, True, 100000)
            aviao1.ligar_motor()
            aviao1.decolar()
            aviao1.voar(500)
            aviao1.atualizar_quilometragem(500)
            aviao1.verificar_manutencao()
            aviao1.info()

        case "2":
            fiat_uno = Carro("Fiat", "Uno", 1984, "Preto", "Fire 1.0 Evo 8V Flex", "5 marchas, manual", "152 km/h", "R$ 9.553", "1ª geração 1984-2013", 0)
            fuscao_preto = Carro("Volkswagen", "Fusca Type 1", 1938, "Preto", "1.2L F4", "4 marchas, manual", "112 km/h", "R$ 20.000,00 a 150.000,00", "1938–2003 (total)", 0)

            fiat_uno.ligar_motor()
            fiat_uno.acelerar()
            fiat_uno.velocidade = 40
            fiat_uno.mudar_marcha()

            print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo}:")
            fiat_uno.info()

            fiat_uno.distancia = 100
            fiat_uno.tempo = 2
            fiat_uno.calcular_velocidade_media()

            fiat_uno.frear()
            fiat_uno.desligar_motor()

            print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo} após desligar:")
            fiat_uno.info()

            fiat_uno.pintar("Cinza")

            print("\n")
            fuscao_preto.ligar_motor()
            fuscao_preto.acelerar()
            fuscao_preto.velocidade = 70
            fuscao_preto.mudar_marcha()

            print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo}:")
            fuscao_preto.info()

            fuscao_preto.distancia = 400
            fuscao_preto.tempo = 5
            fuscao_preto.calcular_velocidade_media()

            fuscao_preto.frear()
            fuscao_preto.desligar_motor()

            print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo} após desligar:")
            fuscao_preto.info()

            fuscao_preto.att_preco("R$ 50.000,00 a 150.000,00")

        case "3":
            moto1 = Moto("Suzuki", "V-Strom 650", "Preto")
            moto2 = Moto("Honda", "CBR 1000RR", "Vermelho")

            moto1.acelerar(20)
            moto2.acelerar(30)

        case "4":
            moto1 = Motoatt("Suzuki", "Vermelha")
            moto2 = Motoatt("Honda", "Azul")

            moto1.ligar_motor()
            moto1.acelerar()
            moto1.velocidade = 40
            moto1.mudar_marcha()

            print("\nInformações da Moto 1:")
            moto1.info()

            moto1.distancia = 100
            moto1.tempo = 2
            moto1.calcular_velocidade_media()

            moto1.frear()
            moto1.desligar_motor()

            print("\nInformações da Moto 1 após desligar:")
            moto1.info()

            print("\n")
            moto2.ligar_motor()
            moto2.acelerar()
            moto2.velocidade = 70
            moto2.mudar_marcha()

            print("\nInformações da Moto 2:")
            moto2.info()

            moto2.distancia = 400
            moto2.tempo = 5
            moto2.calcular_velocidade_media()

            moto2.frear()
            moto2.desligar_motor()

            print("\nInformações da Moto 2 após desligar:")
            moto2.info()

        case _:
            print("Metodo errado tente novamente:")
            veiculos()

def ca():
    print("|=========================|")
    print("|  Exs Classes Abstratas  |")
    print("|1. Exercício 1           |")
    print("|2. Exercício 2           |")
    print("|3. Exercício 3           |")
    print("|4. Exercício 4           |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            # Exercício 1
            vip1=VIP(5,10)
            vip1.imprimeValor()
    
        case "2":
            # Exercício 2
            r1=Retangulo(0, 0)
            print(r1.calculaArea(5, 10))
            print(r1.calculaPerimetro(5, 10))

            t1=Triangulo(0, 0)
            print(t1.calculaArea(2, 5))
            print(t1.calculaPerimetro(1, 2, 3))

        case "3":
            # Exercício 3
            tr1=TriAtleta(False, 40)
            tr1.aquecer()
            tr1.correr()
            tr1.nadar()
            tr1.pedalar()

        case "4":
            # Exercício 4
            c1=ContaCorrente(1)
            p1=Poupanca(2, 0.1)
            ci1=ContaImposto(3, 0.05)

            print(c1.numero)
            print(c1.saldo)
            c1.creditar(2000.0)
            print(c1.saldo)
            c1.debitar(500.0)
            print(c1.saldo)

            print(p1.numero)
            print(p1.saldo)
            p1.creditar(2000.0)
            print(p1.saldo)
            p1.debitar(500.0)
            print(p1.saldo)
            p1.renderJuros()
            print(p1.saldo)

            print(ci1.numero)
            print(ci1.saldo)
            ci1.creditar(2000.0)
            print(ci1.saldo)
            ci1.debitar(500.0)
            print(ci1.saldo)
            ci1.calculaImposto()
            print(ci1.saldo)

        case _:
            print("Metodo errado tente novamente:")
            ca()
            
def inter():
    print("|=========================|")
    print("|  Exercícios Interfaces  |")
    print("|1. Exercício 1           |")
    print("|2. Exercício 2           |")
    print("|0. Sair                  |")
    print("|=========================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            menu1=Menu()
            menu1.menu()
            
        case "2":
            icpf=InfoClientePessoaFisica("123456789")
            icpj=InfoClientePessoaJuridica("123456789-0000")
            cf=ClienteFidelizacao("José","Rua: A, Bairro: A, Cidade: ABCD",1000.0,"10/10/2010")

            icpf.info()
            print(" ")
            icpj.info()
            print(" ")
            cf.info()

        case _:
            print("Metodo errado tente novamente:")
            inter()
            
def rela():
    print("|================================|")
    print("|   Exercícios Relacionamentos   |")
    print("|1. Exercício 1                  |")
    print("|2. Exercício 2                  |")
    print("|3. Exercício 3                  |")
    print("|4. Exercício 4                  |")
    print("|0. Sair                         |")
    print("|================================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()
            
        case "1":
            moto1=MotoR("Yamaha","Fazer")
            farolDaFrente=Farol("Xenon",40)
            farolDeTras=Farol("Xenon",40)

            #agregando
            moto1.instalaFarol(farolDaFrente)
            moto1.instalaFarol(farolDeTras)

            #associando
            moto1.farois[0].acender()
            moto1.farois[0].apagar()
            moto1.farois[1].acender()
            moto1.farois[1].apagar()
        
        case "2":
            pedido1 = Pedido()

            itempedido1 = ItemPedido(codigo=1, valor=100, descricao="Produto 1", quantidade=2)
            itempedido2 = ItemPedido(codigo=2, valor=200, descricao="Produto 2", quantidade=1)

            pedido1.add_item(itempedido1)
            pedido1.add_item(itempedido2)

            total = pedido1.obter_total()
            print(f"Total do pedido: R${total:.2f}")
        
        case "3":
            print("Lista de Exercícios: ")
            print("Exercício 1:\nNão tem saída")
            player=DVDPLAYER()
            midia=DVDMIDIA()

            player.play(midia)
            
            print("\n\nExercício 2:\nNão tem Implementação")
            
            print("\n\nExercício 3:")
            baterista=Baterista()
            saxofonista=Saxofonista()
            musico=Musico2()
            orquestra=Orquestra()

            baterista.toca_com("Saxofonista")
            saxofonista.toca_com("Baterista")

            musico.toca_em("Orquestra")
            orquestra.toca_em("Musico")
            
            print("\n\nExercício 4:")
            baterista=Baterista2()
            saxofonista1=Saxofonista2()
            saxofonista2=Saxofonista2()
            saxofonista3=Saxofonista2()
            saxofonista4=Saxofonista2()
            musico1=Musico3()
            musico2=Musico3()
            orquestra=Orquestra2()

            saxofonista1.toca_com(baterista)

            baterista.add_saxofonista(saxofonista1)
            baterista.add_saxofonista(saxofonista2)
            baterista.add_saxofonista(saxofonista3)
            baterista.add_saxofonista(saxofonista4)
            baterista.toca_com()

            musico1.toca_em(orquestra)

            orquestra.add_musico(musico1)
            orquestra.add_musico(musico2)
            orquestra.toca_em()
            
            print("\n\nExercício 5:\nNão tem saída")
            aluno=Aluno()
            curso=Curso(aluno)
            
            print("\n\nExercício 6:")
            casa=Casa()
            tabuleiro=TabuleiroDeXadrez()

            casa.contem(tabuleiro)
            tabuleiro.contem(casa)
            
            print("\n\nExercício 7:\nNão tem implementação")
            
            print("\n\nExercício 8:")
            school=School()
            department=Department()
            student=Student()
            course=Course()
            instructor=Instructor()

            department.has(school)

            student.attends(course)
            student.member(school)

            instructor.teaches(course)
            instructor.assignedTo(department)
        
        case "4":
            meuCarro=Carro2(1945,"Fiat uno","ABC1234","Branco")

            meuCarro.acelerar()
            meuCarro.frear()
            meuCarro.businar()
        
        case _:
            print("Metodo errado tente novamente:")
            rela()

def yuri():
    print("|================================|")
    print("|     Exercícios Prof: Yuri      |")
    print("|1. Exercício 1                  |")
    print("|2. Exercício 2                  |")
    print("|3. Exercício 3                  |")
    print("|4. Lista de Exs Laços Rep       |")
    print("|5. Exercício 5                  |")
    print("|6. Exercício 6                  |")
    print("|0. Sair                         |")
    print("|================================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()

        case "1":
            novoMestre=Mestre("Luke Skywalker",100,"Alianca para Restauracao da Republica","Jedi")
            print(novoMestre.getIdade(5))
            print(novoMestre.possuiForca())
            print(novoMestre.getAnoNascimentoString())
            print(novoMestre.getDescricao())

            novoSensor=Sensor("Azul",512.0,240)
            print(novoSensor.getMPixelsPorSegundo())
            print(novoSensor.getDescricao())

            novaConexao=Conexao("SCOMP Link",1,4096000)
            print(novaConexao.getProtocoloString())
            print(novaConexao.getTaxaMBps())
            print(novaConexao.getDescricao())

            astromech1=Astromech("R2-D2",novoMestre,novoSensor,novaConexao)
            print(astromech1.getDescricao())
            
        case "2":
            treinador=TreinadorJedi("Grão Mestre","Fae Coven")
            iniciado1=IniciadoJedi("Katooni","Tholothian",23)
            iniciado2=IniciadoJedi("Byph","Ithorian",21)
            iniciado3=IniciadoJedi("Gungi","Wookiee",23)
            iniciado4=IniciadoJedi("Petro","Human",22)
            sessaojedi=SessaoJedi("Instruções de Uso da Força",treinador)

            sessaojedi.addIniciado(iniciado1)
            sessaojedi.addIniciado(iniciado2)
            sessaojedi.addIniciado(iniciado3)
            sessaojedi.addIniciado(iniciado4)

            print(sessaojedi.getIniciado(iniciado1))
            print(sessaojedi.getIniciado(iniciado2))
            print(sessaojedi.getIniciado(iniciado3))
            print(sessaojedi.getIniciado(iniciado4))
            print(sessaojedi.getIniciado("sla"))

            print(sessaojedi.getMediaAnoNascimento())

            print(sessaojedi.getDescricao())

        case "3":
            main = EnsalamentoMain()
            print("Atividade:\n")
            main.mainAll()
            print("")
            print("="*75)
            print("\n\nTestes:\n")
            main.mainTestes()
            
        case "4":
            Atividades()
            
        case "5":
            while True: 
                print("|===========================|")
                print("|        Exercicio 9        |")
                print("|1. Exemplos Exceções       |")
                print("|2. Exemplos Assert         |")
                print("|3. Tarefa                  |")
                print("|0. Sair                    |")
                print("|===========================|")
                opcao=input("Insira a opção que você quer: ")
                match opcao:
                    case "0": break
                    case "1":
                        while True: 
                            print("|===========================|")
                            print("|     Exemplos Exceções     |")
                            print("|1. Exemplo 1               |")
                            print("|2. Exemplo 2               |")
                            print("|3. Exemplo 3               |")
                            print("|4. Exemplo 4               |")
                            print("|5. Exemplo 5               |")
                            print("|0. Sair                    |")
                            print("|===========================|")
                            opcao=input("Insira a opção que você quer: ")
                            match opcao:
                                case "0": break
                                case "1":
                                    print("Exemplo 1: ")
                                    while True:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                    print(f"O resultado é: {resultado}")
                                    print("... continua o programa")

                                    print("Exemplo 2: ")
                                    try:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                        print(f"O resultado é: {resultado}")
                                    except ZeroDivisionError:
                                        print("Erro: Não é possível dividir por zero!")
                                    except ValueError:
                                        print("Erro: Entrada inválida! Por favor, digite um número.")
                                    print("... continua o programa")

                                    print("Exemplo 3: ")
                                    while True:
                                        try:
                                            x = int(input("Digite um número: "))
                                            y = int(input("Digite outro número: "))
                                            resultado = x / y
                                            print(f"O resultado é: {resultado}")
                                        except Exception as e:
                                            print(f"Ocorreu um erro: {e}")
                                    print("... continua o programa")
                                    
                                case "2":
                                    print("Exemplo 1: ")
                                    try:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                    except ZeroDivisionError:
                                        print("Erro: Não é possível dividir por zero!")
                                    except ValueError:
                                        print("Erro: Entrada inválida! Por favor, digite um número.")
                                    else:
                                        print(f"O resultado é: {resultado}")
                                    print("... continua o programa")

                                    print("Exemplo 2: ")
                                    try:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                    except ZeroDivisionError:
                                        print("Erro: Não é possível dividir por zero!")
                                    except ValueError:
                                        print("Erro: Entrada inválida! Por favor, digite um número.")
                                    else:
                                        print(f"O resultado é: {resultado}")
                                    print("... continua o programa")
                                    
                                    print("Exemplo 3: ")
                                    try:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                    except ZeroDivisionError:
                                        print("Erro: Não é possível dividir por zero!")
                                    except ValueError:
                                        print("Erro: Entrada inválida! Por favor, digite um número.")
                                    finally:
                                        print(f"O resultado é: {resultado}")
                                    print("Execução finalizada.")
                                
                                case "3":
                                    try:
                                        x = int(input("Digite um número: "))
                                        y = int(input("Digite outro número: "))
                                        resultado = x / y
                                    except ZeroDivisionError:
                                        print("Erro: Não é possível dividir por zero!")
                                    except ValueError:
                                        print("Erro: Entrada inválida! Por favor, digite um número.")
                                    finally:
                                        print(f"O resultado é: {resultado}")
                                    print("Execução finalizada.")
                                    
                                case "4":
                                    class ErrorNovoException(Exception):
                                        def __init__(self, mensagem):
                                            self.mensagem = mensagem
                                            super().__init__(self.mensagem)
                                        def dividir(a, b):
                                            if b == 3:
                                                raise ErrorNovoException("Não é possível dividir por 3!")
                                            return a / b
                                    try:
                                        resultado = dividir(10, 2)
                                    except ErrorNovoException as e:
                                        print(f"Erro: {e.mensagem}")
                                    else:
                                        print("resultado:", resultado)
                                    print("... continua o programa")

                                case "5":
                                    print("Exemplo 1: ")
                                    try:
                                        f = open('arquivo_inexistente.txt', 'r')
                                    except FileNotFoundError:
                                        print("Erro: Arquivo não encontrado!")
                                    print("... continua o programa")
                                    
                                    print("Exemplo 2: ")
                                    try:
                                        numero = int(input("Digite um número: "))
                                    except ValueError:
                                        print("Erro: Você não digitou um número válido!")
                                    print("... continua o programa")
                                    
                                    print("Exemplo 3.1: ")
                                    capitais = {'Brasil': 'Brasília', 'França': 'Paris', 'EUA': 'Washington', 'Japão': 'Tóquio'}
                                    while True:
                                        try:
                                            entrada = input("Entre com um país: ")
                                            print(capitais[entrada])
                                        except:
                                            print("País não encontrado")
                                            pais = entrada
                                            capital = input("Entre com a capital de " + pais)
                                            capitais[pais] = capital
                                            
                                    print("Exemplo 3.2: ")
                                    capitais = {'Brasil': 'Brasília', 'França': 'Paris', 'EUA': 'Washington', 'Japão': 'Tóquio'}
                                    entrada = input("Entre com um país: ")
                                    try:
                                        print(capitais[entrada])
                                    except KeyError:
                                        print("Erro: Chave não encontrada no dicionário!")
                                    print("... continua o programa")
                                    
                                    print("Exemplo 4: ")
                                    try:
                                        resultado = 'abc' + 123
                                    except TypeError:
                                        print("Erro: Não é possível somar uma string e um número!")
                                    print("... continua o programa")

                                    print("Exemplo 5: ")
                                    try:
                                        import biblioteca_inexistente
                                    except ModuleNotFoundError:
                                        print("Erro: Biblioteca não encontrada!")
                                    print("... continua o programa")

                                case _: print("Opção errada, tente novamente.")
                   
                    case "2":
                        while True: 
                            print("|===========================|")
                            print("|     Exemplos Assert       |")
                            print("|1. Exemplo 1               |")
                            print("|2. Exemplo 2               |")
                            print("|3. Exemplo 3               |")
                            print("|4. Exemplo 4               |")
                            print("|5. Exemplo 5               |")
                            print("|0. Sair                    |")
                            print("|===========================|")
                            opcao=input("Insira a opção que você quer: ")
                            match opcao:
                                case "0": break
                                case "1":
                                    print("Exemplo 1:")
                                    def divide(x, y):
                                        assert y != 0, "Divisão por zero não é permitida"
                                        return x / y
                                    print(divide(50, 5))
                                    print(divide(10, 0))
                                    print(divide(10, 2))

                                case "2":
                                    print("Exemplo 2: ")
                                    def encontrar_maior(lista):
                                        if len(lista) == 0:
                                            return -1
                                        return max(lista)
                                    print(encontrar_maior([1, 2, 3, 4]))
                                    print(encontrar_maior([21, 421, 4, 432, 253, 523]))
                                    print("... continua o codigo")

                                case "3":
                                    print("Exemplo 3: ")
                                    def calcular_imc(peso, altura):
                                        assert peso > 0 and altura > 0, "Peso e altura devem ser maiores que zero"
                                        return peso / altura**2
                                    resultado = calcular_imc(-70, 1.75)
                                    resultado = calcular_imc(73, 1.90)
                                    print(resultado)
                                    print("... continua o programa")

                                case "4":
                                    print("Exemplo 4: ")
                                    class Pilha:
                                        def __init__(self):
                                            self.items = []
                                        def empilhar(self, item):
                                            self.items.append(item)
                                        def desempilhar(self):
                                            assert len(self.items) > 0, "Não é possível desempilhar de uma pilha"
                                            return self.items.pop()
                                    p = Pilha()
                                    p.empilhar(1)
                                    p.empilhar(5)
                                    print(p.items)
                                    print(p.desempilhar())
                                    print(p.desempilhar())
                                    print(p.items)
                                    p.empilhar(3)
                                    p.empilhar(2)
                                    print(p.items)

                                case "5":
                                    print("Exemplo 5: ")
                                    import requests
                                    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
                                    requisicao_dic = requisicao.json()
                                    cotacao = requisicao_dic["USDBRL"]["bid"]
                                    print(type(cotacao), cotacao)
                                    preco_produto = 100 # DOLAR
                                    cotacao = float(cotacao)
                                    assert type(cotacao) == float, "Cotacao não é do tipo FLOAT"
                                    faturamento = preco_produto * cotacao
                                    print('o preco do produto de ', preco_produto, 'em dolares, é igual a ', faturamento)

                                    preco_produto_2 = 1265 # DOLAR
                                    faturamento_2 = preco_produto_2 * cotacao
                                    print('o preco do produto de ', preco_produto_2, 'em dolares, é igual a ', faturamento_2)

                                case "6":
                                    print("Exemplo 6: ")
                                    def soma(a, b):
                                        assert isinstance(a, int) and isinstance(b, int), "A e B devem ser inteiros"
                                        return a + b
                                    print(soma(2, 3))
                                    print(soma('a', 3))
                                    print(soma('a', 'b'))
                                    print(soma(50, 10))
                                    print("akjsdlkjsadlkja")
                                    
                                case _: print("Opção errada, tente novamente.")
                                
                    case "3":
                        def divisao(a, b):
                            assert b != 0, "b deve ser diferente de zero"
                            return a / b

                        def soma(a, b):
                            return a + b
                            
                        def calcular_imc(peso, altura):
                            assert altura > 0, "Altura deve ser maior que zero."
                            assert peso > 0, "Peso deve ser maior que zero."
                            return peso / (altura ** 2)
                            
                        def encontrar_maior(lista):
                            assert len(lista) > 0, "A lista não pode estar vazia."
                            return max(lista)

                        for i in range(2):
                            print("\nDivisão:")
                            a=int(input("Insira um número: "))
                            b=int(input("Insira um número: "))
                            print(f"A divisão de A por B é: {divisao(a, b)}")

                            print("\nSoma:")
                            a=int(input("Insira um número: "))
                            b=int(input("Insira um número: "))
                            print(f"A soma de A e B é: {soma(a, b)}")

                            print("\nIMC:")
                            peso=float(input("Insira o seu peso: "))
                            altura=float(input("Insira a sua altura: "))
                            print(f"O seu IMC é: {calcular_imc(peso, altura)}")

                            print("\nLista:")
                            lista=list(input("Insira uma lista, exemplo '1, 2, 3, 4, 5': "))
                            print(f"O maior valor da lista é: {encontrar_maior(lista)}")

                        def dividir_numeros(a, b):
                            try:
                                return a / b
                            except ZeroDivisionError:
                                return "Erro: Divisão por zero."
                            except TypeError:
                                return "Erro: Entrada inválida"

                        def dividir_numeros_2(a, b):
                            try:
                                resultado = a / b
                            except ZeroDivisionError:
                                return "Erro: Divisão por zero."
                            except TypeError:
                                return "Erro: Entrada inválida"
                            else:
                                return resultado
                                
                        def dividir_numeros_3(a, b):
                            try:
                                return a / b
                            except ZeroDivisionError:
                                return "Erro: Divisão por zero."
                            except TypeError:
                                return "Erro: Entrada inválida"
                            finally:
                                print("Operação de divisão concluída.")
                                
                        def ler_arquivo(nome_arquivo):
                            try:
                                with open(nome_arquivo, "r") as file:
                                    return file.read()
                            except FileNotFoundError:
                                return "Erro: Arquivo não encontrado."
                                
                        def buscar_chave(dicionario, chave):
                            try:
                                return dicionario[chave]
                            except KeyError:
                                return "Erro: Chave não encontrada."
                                
                        def importar_biblioteca(nome_biblioteca):
                            try:
                                __import__(nome_biblioteca)
                                return f"Biblioteca '{nome_biblioteca}' importada com sucesso."
                            except ImportError:
                                return f"Erro: Biblioteca {nome_biblioteca} não encontrada."

                        print("\nDivisão Try, Except 1:")
                        print(dividir_numeros(10, 0))
                        print(dividir_numeros(10, 'a'))

                        print("\nDivisão Try, Except 2:")
                        print(dividir_numeros_2(20, 2))
                        print(dividir_numeros_2(50, 5))

                        print("\nDivisão Try, Except 3:")
                        print(dividir_numeros_3(50, 2))
                        print(dividir_numeros_3(100, 2))

                        print("\nLer Arquivo")
                        print(ler_arquivo("arquivo.txt"))

                        print("\nDicionario")
                        dicionario = {"a": 1, "b": 2}
                        print(buscar_chave(dicionario, "a"))
                        print(buscar_chave(dicionario, "c"))

                        print("\nBiblioteca")
                        print(importar_biblioteca("os"))
                        print(importar_biblioteca("biblioteca"))
                        
                    case _: print("Opção errada, tente novamente.")
            
        case "6":
            while True: 
                print("|===========================|")
                print("|        Exercicio 10       |")
                print("|1. Exemplos                |")
                print("|2. Tarefa 1                |")
                print("|3. Tarefa 2                |")
                print("|0. Sair                    |")
                print("|===========================|")
                opcao=input("Insira a opção que você quer: ")
                match opcao:
                    case "0": break
                    case "1":
                        Animal21 = Cachorro2()
                        Animal21.emitir_som()
                        Animal22 = Gato2()
                        Animal22.emitir_som()
                        
                        obj_um = Circulo(10, 10, 5.0)
                        print(obj_um.getArea())
                        print(obj_um.getPerimetro())
                        obj_um.toString()
                    
                        obj_dois = Retangulo(12, 65, 2.0, 7.0)
                        print(obj_dois.getArea())
                        print(obj_dois.getPerimetro())
                        obj_dois.toString()
                        
                    case "2":
                        Professor2=Professor2("Yuri", 15)
                        Aluno2=Aluno2("Adam", 15)

                        Professor2.apresentar()
                        Aluno2.apresentar()
                    
                    case "3":
                        macaco=Macaco()
                        macaco.respirar()

                        humano=Humano()
                        humano.respirar()
                        
                    case _: print("Opção errada, tente novamente.")

        case _:
            print("Metodo errado tente novamente:")
            yuri()
            
def proj():
    print("|================================|")
    print("|         Meus Projetos          |")
    print("|1. Utilitarios                  |")
    print("|0. Sair                         |")
    print("|================================|")
    mtd=input("Fale o metodo que voce quer usar: ")
    print(f"O metodo que você escolheu foi: {mtd}")
    match mtd:
        case "0":
            verificar_classes()

        case "1":
            app=Utilitarios()
            
        case _:
            print("Metodo errado tente novamente:")
            proj()
            
verificar_classes()
