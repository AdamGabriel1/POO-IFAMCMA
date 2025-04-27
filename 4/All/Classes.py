from abc import ABC, abstractmethod
from math import pi
import math

class Animal(ABC):
    def __init__(self,cor,altura,peso):
        self.cor=cor
        self.altura=altura
        self.peso=peso

class Ave:
    def __init__(self,tipo_ave,voa,peso):
        self.tipo_ave=tipo_ave
        self.voa=voa
        self.peso=peso

    def voar(self):
        if self.voa=="Sim":
            print(f"A (o) {self.tipo_ave} de {self.peso} está voando.")
        else:
            print(f"A (o) {self.tipo_ave} {self.peso} não pode voar.")

class Cachorro:
    def __init__(self,nome,raca,idade,cor,altura,peso,genero,dono):
        self.nome=nome
        self.raca=raca
        self.idade=idade
        self.cor=cor
        self.altura=altura
        self.peso=peso
        self.genero=genero
        self.dono=dono

    def latir(self):
        print("Auuuuuuuu!!!!")

    def andar(self):
        print("Se não for mais de 5km de corrida eu não vou.")

    def comer(self):
        print("Se não for Pedigree eu não como.")

    def brincar(self):
        print("")

    def fazer_truques(self):
        print("Aqui não é esses negocio de dar a patinha não eu jogo Basquete, me respeita.")

    def receber_carinho(self):
        print("Melhor cachorro do Brasil...")

    def definir_dono(self,novo_dono):
        self.dono=novo_dono

class GerenciadorDeDados(ABC):
    def __init__(self):
        self.itens = []
        self.horarios = list(range(1, 25))
        self.datas = list(range(1, 31))
        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                      "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def rm_item(self, item):
        pass

    @abstractmethod
    def mostrar_itens(self):
        pass

    @abstractmethod
    def visu_mes(self, mes):
        pass

    @abstractmethod
    def visu_ano(self):
        pass

    def add_horario(self, novo_horario):
        if novo_horario not in self.horarios:
            self.horarios.append(novo_horario)
            print(f"Horário {novo_horario} adicionado.")
        else:
            print("Horário já existe na lista.")

    def rm_horario(self, horario):
        if horario in self.horarios:
            self.horarios.remove(horario)
            print(f"Horário {horario} removido.")
        else:
            print("Horário não encontrado.")

    def mostrar_dias_semana(self):
        print("Dias da semana:")
        for dia in self.dias_semana:
            print(dia)

    def mostrar_meses(self):
        print("Meses:")
        for mes in self.meses:
            print(mes)

    def add_data(self, nova_data):
        if nova_data not in self.datas:
            self.datas.append(nova_data)
            print(f"Data {nova_data} adicionada.")
        else:
            print("Data já existe na lista.")

    def rm_data(self, data):
        if data in self.datas:
            self.datas.remove(data)
            print(f"Data {data} removida.")
        else:
            print("Data não encontrada.")

    def determinar_dia_da_semana(self, ano, mes, dia):
        if mes < 3:
            mes += 12
            ano -= 1
        k = ano % 100
        j = ano // 100
        dia_da_semana = (dia + 13*(mes+1)//5 + k + k//4 + j//4 + 5*j) % 7
        return (dia_da_semana + 6) % 7

    def dias_num_mes(self, mes, ano):
        dias_por_mes = {
            "Janeiro": 31, "Fevereiro": 28, "Março": 31, "Abril": 30, "Maio": 31, "Junho": 30,
            "Julho": 31, "Agosto": 31, "Setembro": 30, "Outubro": 31, "Novembro": 30, "Dezembro": 31
        }
        if mes == "Fevereiro" and self.eh_bissexto(ano):
            return 29
        return dias_por_mes[mes]

    def eh_bissexto(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    def proximo_dia(self, ano, mes, dia):
        mes_idx = self.meses.index(mes) + 1
        dia += 1

        if dia > self.dias_num_mes(mes, ano):
            dia = 1
            mes_idx += 1
            if mes_idx > 12:
                mes_idx = 1
                ano += 1

        return ano, mes_idx, dia

class Calendario(GerenciadorDeDados):
    def __init__(self, ano, feriados=None, eventos=None, p_dia_da_semana="Segunda"):
        super().__init__()
        self.ano = ano
        self.p_dia_da_semana = p_dia_da_semana
        
        self.bimestres_num_ano = list(range(1, 7))
        self.trimestres_num_ano = list(range(1, 5))
        self.semestres_num_ano = list(range(1, 3))
        self.meses_de_um_bimestre = list(range(1, 3))
        self.meses_de_um_trimestre = list(range(1, 4))
        self.meses_de_um_semestre = list(range(1, 7))
        
        self.feriados = feriados or {}
        self.eventos = eventos or {}

    def add_item(self, item):
        pass

    def rm_item(self, item):
        pass

    def mostrar_itens(self):
        pass

    def add_evento(self, data, evento):
        self.eventos.setdefault(data, []).append(evento)

    def rm_evento(self, data, evento):
        eventos = self.eventos.get(data)
        if eventos and evento in eventos:
            eventos.remove(evento)
            if not eventos:
                del self.eventos[data]
        else:
            print("Evento não encontrado.")

    def visu_eventos(self, data):
        eventos = self.eventos.get(data, [])
        if eventos:
            print(f"Eventos em {data}:")
            for evento in eventos:
                print(evento)
        else:
            print("Nenhum evento encontrado para esta data.")

    def verif_feriado(self, data):
        feriado = self.feriados.get(data)
        if feriado:
            print(f"{data} é feriado: {feriado}")
        else:
            print(f"{data} não é feriado.")

    def visu_mes(self, mes):
        if mes in self.meses:
            print(f"Calendário para o mês de {mes}:")
            dias_no_mes = self.dias_num_mes(mes, self.ano)
            dia_inicio = self.determinar_dia_da_semana(self.ano, self.meses.index(mes) + 1, 1)
            print(" " * (3 * dia_inicio), end="")
            for dia in range(1, dias_no_mes + 1):
                print(f"{dia:2}", end=" ")
                if (dia + dia_inicio) % 7 == 0:
                    print()
            print()

    def visu_ano(self):
        print(f"Calendário para o ano de {self.ano}:")
        for mes in self.meses:
            self.visu_mes(mes)
            
    def determinar_ultimo_dia_mes_anterior(self, mes, ano):
        mes_anterior = self.meses[(self.meses.index(mes) - 1) % 12]
        return self.dias_num_mes(mes_anterior, ano)
            
    def mostrar_meses_por_periodo(self, periodo):
        if periodo == "bimestre":
            periodos = self.bimestres_num_ano
            meses_por_periodo = self.meses_de_um_bimestre
        elif periodo == "trimestre":
            periodos = self.trimestres_num_ano
            meses_por_periodo = self.meses_de_um_trimestre
        elif periodo == "semestre":
            periodos = self.semestres_num_ano
            meses_por_periodo = self.meses_de_um_semestre
        else:
            print("Período inválido. Escolha entre 'bimestre', 'trimestre' ou 'semestre'.")
            return

        for periodo_num in periodos:
            print(f"{periodo.capitalize()} {periodo_num}:")
            for mes_num in meses_por_periodo:
                mes = self.meses[(periodo_num - 1) * len(meses_por_periodo) + mes_num - 1]
                print(mes)
            print()
            
    def mostrar_calendario_xml(self):
        xml = "<Calendario>\n"
        dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        for mes in self.meses:
            xml += f"  <Mes>\n    <Nome>{mes}</Nome>\n"
            xml += "    <Semanas>\n"

            dia_inicio = self.determinar_dia_da_semana(self.ano, self.meses.index(mes) + 1, 1)

            if dia_inicio != 0:
                dia_anterior = self.determinar_ultimo_dia_mes_anterior(mes, self.ano)
                dias_mes_anterior = dia_anterior - dia_inicio + 1
                for i in range(dia_inicio):
                    xml += f"\t| {dias_semana[i]} {dias_mes_anterior + i} "

            dia_atual = 1
            while dia_atual <= self.dias_num_mes(mes, self.ano):
                xml += f"\t| {dias_semana[(dia_inicio + dia_atual - 1) % 7]} {dia_atual} "
                if (dia_inicio + dia_atual) % 7 == 0:
                    xml += "|\n"
                dia_atual += 1

            if (dia_inicio + dia_atual - 1) % 7 != 0:
                dias_mes_posterior = 7 - (dia_inicio + dia_atual - 1) % 7
                for i in range(dias_mes_posterior):
                    xml += f"\t| {dias_semana[(dia_inicio + dia_atual + i - 1) % 7]} {i + 1} "

            xml += "\n    <Semanas>\n  </Mes>\n"

        xml += "</Calendario>"
        with open('calendario_xml.txt', 'w') as arquivo:
            arquivo.write(xml)
        print("Abra o arquivo 'calendario_xml.txt' para ver o Calendario em XML.")
        print(xml)

class Cronograma(GerenciadorDeDados):
    def __init__(self):
        super().__init__()

    def add_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado à lista.")

    def rm_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")

    def mostrar_itens(self):
        print("Itens na lista:")
        for item in self.itens:
            print(item)

    def visu_mes(self, mes):
        pass

    def visu_ano(self):
        pass

    def opcs(self):
        opcoes = {
            "0": "Sair",
            "1": "Adicionar item à lista",
            "2": "Remover item da lista",
            "3": "Mostrar itens da lista",
            "4": "Adicionar horário",
            "5": "Remover horário",
            "6": "Mostrar dias da semana",
            "7": "Mostrar meses",
            "8": "Adicionar data",
            "9": "Remover data"
        }

        while True:
            print("|===============================|")
            for key, value in opcoes.items():
                print(f"|{key}. {value}\t\t|")
            print("|===============================|")

            escolha = input("Escolha a opção desejada: ")

            match escolha:
                case "0":
                    print("Saindo do menu.")
                    break
                case "1":
                    item = input("Insira o item que deseja adicionar à lista: ")
                    self.add_item(item)
                case "2":
                    item = input("Insira o item que deseja remover da lista: ")
                    self.rm_item(item)
                case "3":
                    self.mostrar_itens()
                case "4":
                    horario = int(input("Insira o novo horário: "))
                    self.add_horario(horario)
                case "5":
                    horario = int(input("Insira o horário que deseja remover: "))
                    self.rm_horario(horario)
                case "6":
                    self.mostrar_dias_semana()
                case "7":
                    self.mostrar_meses()
                case "8":
                    nova_data = int(input("Insira a nova data: "))
                    self.add_data(nova_data)
                case "9":
                    data = int(input("Insira a data que deseja remover: "))
                    self.rm_data(data)
                case _:
                    print("Opção inválida. Escolha novamente.")

class Entidade(ABC):
    def __init__(self, nome, endereco, telefone=None, email=None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @abstractmethod
    def info(self):
        pass

class Cliente(Entidade):
    def __init__(self, nome, cpf, data_de_nasc, endereco):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_de_nasc = data_de_nasc

    def mudar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def fazer_emprestimo(self, valor):
        print(f"Solicitação de empréstimo no nome de {self.nome} de R$ {valor}")

    def info(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_de_nasc}\nEndereço: {self.endereco}")

class Barraquinha(Entidade):
    def __init__(self, nome, endereco, telefone, email, longitude, latitude, cardapio, funcionamento, delivery, taxa_delivery):
        super().__init__(nome, endereco, telefone, email)
        self.longitude = longitude
        self.latitude = latitude
        self.cardapio = cardapio
        self.funcionamento = funcionamento
        self.delivery = delivery
        self.taxa_delivery = taxa_delivery

    def adicionar_item_ao_cardapio(self, item):
        self.cardapio.append(item)
        print(f"Item '{item}' adicionado ao cardápio.")

    def remover_item_do_cardapio(self, item):
        if item in self.cardapio:
            self.cardapio.remove(item)
            print(f"Item '{item}' removido do cardápio.")
        else:
            print(f"Item '{item}' não encontrado no cardápio.")

    def alterar_preco_de_item_ao_cardapio(self, item, novo_preco):
        for i in self.cardapio:
            if i['nome'] == item:
                i['preco'] = novo_preco
                print(f"Preço do item '{item}' alterado para R$ {novo_preco}.")
                return
        print(f"Item '{item}' não encontrado no cardápio.")

    def info(self):
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nCardápio: {self.cardapio}\nFuncionamento: {self.funcionamento}\nDelivery: {self.delivery}\nTaxa de Delivery: {self.taxa_delivery}")

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Loja(Entidade):
    def __init__(self, nome, endereco, telefone, email, horario_abertura, horario_fechamento):
        super().__init__(nome, endereco, telefone, email)
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento
        self.produtos = []

    def esta_aberta(self, hora_atual):
        if self.horario_abertura <= hora_atual < self.horario_fechamento:
            print(f"A loja {self.nome} está aberta agora.")
        else:
            print(f"A loja {self.nome} está fechada agora.")

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado à loja.")

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f"Produto '{nome_produto}' removido da loja.")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def verificar_estoque(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                print(f"Estoque de '{nome_produto}': {produto.estoque}")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def atualizar_estoque(self, nome_produto, novo_estoque):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.estoque = novo_estoque
                print(f"Estoque de '{nome_produto}' atualizado para {novo_estoque}.")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def listar_produtos(self):
        print("Produtos disponíveis na loja:")
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}")

    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                print(f"Informações de '{nome_produto}': Preço: {produto.preco}, Estoque: {produto.estoque}")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def info(self):
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}\nHorário de Abertura: {self.horario_abertura}\nHorário de Fechamento: {self.horario_fechamento}")

class Recipiente(ABC):
    def __init__(self, raio_topo, raio_base, altura, material, estilo):
        self.raio_topo = raio_topo
        self.raio_base = raio_base
        self.altura = altura
        self.material = material
        self.estilo = estilo

    @abstractmethod
    def Calcular_volume(self):
        pass

    def Encher(self):
        print(f"{self.__class__.__name__} está cheio.")

    def Esvaziar(self):
        print(f"{self.__class__.__name__} está vazio.")

class Caneca(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, formato_da_alca):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.formato_da_alca = formato_da_alca

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Caneca: {volume} unidades cúbicas")

class Copo(Recipiente):
    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume do Copo: {volume} unidades cúbicas")

class Taca(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, tipo_de_bebida):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.tipo_de_bebida = tipo_de_bebida

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Taça: {volume} unidades cúbicas")

class Jarra(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, capacidade):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.capacidade = capacidade

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Jarra: {volume} unidades cúbicas")

class Celular:
    def __init__(self):
        # Dicionário para armazenar as informações de cada celular
        self.celulares = {
            "1": {
                # DADOS GERAIS
                "\n1": "DADOS GERAIS:",
                "Modelo": "Samsung",
                "Nome": "S24 Ultra",
                "Tipo": "Smartphone",
                "Sistema Operacional": "Android 14 Samsung One UI 6.1",
                "Disponibilidade": "2024/1",
                "Dimensões": "162.3 x 79 x 8.6 mm",
                "Peso": "232 gramas",
                "Resistencia a Água": "Sim",
                # DADOS TÉCNICOS
                "\n2": "DADOS TÉCNICOS:",
                "Processador": "1x 3.39 GHz Cortex-X4 + 3x 3.1 GHz Cortex-A720 + 2x 2.9 GHz Cortex-A720 + 2x 2.2 GHz Cortex-A520",
                "Chipset": "Snapdragon 8 Gen 3 Qualcomm SM8650-AB",
                "Memória RAM": "12 GB",
                "GPU": "Adreno 750",
                "Armazenamento": "1 TB",
                "Memória Expansivel": "Não",
                # BATERIA
                "\n3": "BATERIA:",
                "Tipo": "LiPo",
                "Bateria": "5000 mAh",
                # TELA
                "\n4": "TELA:",
                "Tela": "6.8",
                "Resolução": "1440 x 3120 pixel",
                "Densidade de Pixels": "505 ppi",
                "Tipo da Tela": "Dynamic AMOLED 2X",
                "FPS": "120 Hz",
                "Proteção": "Gorilla Glass Armor",
                # CÂMERA
                "\n5": "CÂMERA:",
                "Megapixels": "200 Mp + 50 Mp + 12 Mp + 10 Mp",
                "Resolução da Câmera": "16330 x 12247 pixel",
                "Tamanho do Sensor": "1/1.3 '' + 1/2.55 '' + 1/3.52 ''",
                "Aperture Size": "F 1.7 + F 3.4 + F 2.2 + F 2.4",
                "Estabilização": "Ótica",
                "Ângulo máximo": "120 °",
                "Zoom Ótico": "5 x",
                "Autofoco": "Tem",
                "Foco por Toque": "Tem",
                "Flash": "LED",
                "HDR": "Tem",
                "Dual Shot": "Tem",
                "Localização": "Tem",
                "Detecção Facial": "Tem",
                "Câmera Frontal": "12 Mp F 2.2",
                # VÍDEO
                "\n6": "VÍDEO:",
                "Resolução da Gravação": "8K UHD",
                "Auto Focagem de Vídeo": "Tem",
                "FPS da Gravação": "30 fps",
                "Estabilização de Vídeo": "Tem",
                "Slow Motion": "960 fps",
                "Vídeo HDR": "Tem",
                "Dual Rec": "Tem",
                "Stereo Sound Rec": "Tem",
                "Foto em Vídeo": "Tem",
                "Vídeo Camera Frontal": "4K (2160p), 60fps",
                "Opções da Câmera Frontal": "HDR/Face Detection/Autofocus",
            },
            "2": {
                # DADOS GERAIS
                "\n1": "DADOS GERAIS:",
                "Modelo": "Samsung",
                "Nome": "A14 5G",
                "Tipo": "Smartphone",
                "Sistema Operacional": "Android 13 Samsung One UI Core 5",
                "Disponibilidade": "2023/1",
                "Dimensões": "167.7 x 78 x 9.1 mm",
                "Peso": "202 gramas",
                "Resistencia a Água": "Sim",
                # DADOS TÉCNICOS
                "\n2": "DADOS TÉCNICOS:",
                "Processador": "2x 2.2 GHz Cortex-A76 + 6x 2.0 GHz Cortex-A55",
                "Chipset": "Dimensity 700 MediaTek MT6833",
                "Memória RAM": "4 GB",
                "GPU": "Mali-G57 MC2",
                "Armazenamento": "128 GB",
                "Memória Expansivel": "Sim, MicroSDXC atè 1024 GB",
                # BATERIA
                "\n3": "BATERIA:",
                "Tipo": "LiPo",
                "Bateria": "5000 mAh",
                # TELA
                "\n4": "TELA:",
                "Tela": "6.6",
                "Resolução": "1080 x 2400 pixel",
                "Densidade de Pixels": "339 ppi",
                "Tipo da Tela": "PLS LCD",
                "FPS": "90 Hz",
                "Cores": "16 milhões",
                # CÂMERA
                "\n5": "CÂMERA:",
                "Megapixels": "50 Mp + 2 Mp + 2 Mp",
                "Resolução da Câmera": "8165 x 6124 pixel",
                "Aperture Size": "F 1.8 + F 2.4 + F 2.4",
                "Estabilização": "Digital",
                "Autofoco": "Tem",
                "Foco por Toque": "Tem",
                "Flash": "LED",
                "HDR": "Tem",
                "Dual Shot": "Tem",
                "Localização": "Tem",
                "Detecção Facial": "Tem",
                "Câmera Frontal": "13 Mp F 2",
                # VÍDEO
                "\n6": "VÍDEO:",
                "Resolução da Gravação": "Full HD",
                "Auto Focagem de Vídeo": "Tem",
                "FPS da Gravação": "30 fps",
                "Vídeo Camera Frontal": "4K (2160p), 60fps",
                "Opções da Câmera Frontal": "HDR/Face Detection/Autofocus",
            },
            "3": {
                # DADOS GERAIS
                "\n1": "DADOS GERAIS:",
                "Modelo": "Xiaomi",
                "Nome": "Redmi 9A",
                "Tipo": "Smartphone",
                "Sistema Operacional": "Android 10 MIUI 11",
                "Disponibilidade": "2020/2",
                "Dimensões": "164.9 x 77.07 x 9 mm",
                "Peso": "194 gramas",
                "Resistencia a Água": "Não",
                # DADOS TÉCNICOS
                "\n2": "DADOS TÉCNICOS:",
                "Processador": "4x 2.0 GHz Cortex-A53 + 4x 1.5 GHz Cortex-A53",
                "Chipset": "Helio G25 MediaTek",
                "Memória RAM": "2 GB",
                "GPU": "PowerVR GE8320",
                "Armazenamento": "32 GB",
                "Memória Expansivel": "Sim, MicroSDXC atè 512 GB",
                # BATERIA
                "\n3": "BATERIA:",
                "Tipo": "LiPo",
                "Bateria": "5000 mAh",
                # TELA
                "\n4": "TELA:",
                "Tela": "6.53",
                "Resolução": "720 x 1600 pixel",
                "Densidade de Pixels": "269 ppi",
                "Tipo da Tela": "IPS LCD",
                "FPS": "60 Hz",
                "Cores": "16 milhões",
                # CÂMERA
                "\n5": "CÂMERA:",
                "Megapixels": "13 Mp",
                "Resolução da Câmera": "4163 x 3122 pixel",
                "Aperture Size": "F 2.2",
                "Estabilização": "Digital",
                "Autofoco": "Tem",
                "Foco por Toque": "Tem",
                "Flash": "LED",
                "HDR": "Tem",
                "Dual Shot": "Tem",
                "Localização": "Tem",
                "Detecção Facial": "Tem",
                "Câmera Frontal": "5 Mp F 2.2",
                # VÍDEO
                "\n6": "VÍDEO:",
                "Resolução da Gravação": "Full HD",
                "Auto Focagem de Vídeo": "Tem",
                "FPS da Gravação": "30 fps",
                "Vídeo Camera Frontal": "Full HD, 30fps",
                "Opções da Câmera Frontal": "HDR/Face Detection/Autofocus",
            },
            "4": {
                # DADOS GERAIS
                "\n1": "DADOS GERAIS:",
                "Modelo": "Nubia",
                "Nome": "Red Magic 9 Pro Plus",
                "Tipo": "Smartphone",
                "Sistema Operacional": "Android 14 Redmagic OS 9",
                "Disponibilidade": "2023/3",
                "Dimensões": "163.98 x 76.35 x 8.9 mm",
                "Peso": "229 gramas",
                "Resistencia a Água": "Não",
                # DADOS TÉCNICOS
                "\n2": "DADOS TÉCNICOS:",
                "Processador": "1x 3.3 GHz Cortex-X4 + 3x 3.2 GHz Cortex-A720 + 2x 3.0 GHz Cortex-A720 + 2x 2.3 GHz Cortex-A520",
                "Chipset": "Snapdragon 8 Gen 3 Qualcomm SM8650-AB",
                "Memória RAM": "16 GB",
                "GPU": "Adreno 750",
                "Armazenamento": "512 GB",
                "Memória Expansivel": "Não",
                # BATERIA
                "\n3": "BATERIA:",
                "Tipo": "LiPo",
                "Bateria": "6500 mAh",
                # TELA
                "\n4": "TELA:",
                "Tela": "6.8",
                "Resolução": "1116 x 2480 pixel",
                "Densidade de Pixels": "400 ppi",
                "Tipo da Tela": "AMOLED",
                "FPS": "120 Hz",
                "Cores": "Mais de 16 milhões",
                # CÂMERA
                "\n5": "CÂMERA:",
                "Megapixels": "50 Mp + 50 Mp + 2 Mp",
                "Resolução da Câmera": "8165 x 6124 pixel",
                "Tamanho do Sensor": "1/1.57 '' + 1/2.76 ''",
                "Aperture Size": "F 2.4",
                "Estabilização": "Ótica",
                "Autofoco": "Tem",
                "Foco por Toque": "Tem",
                "Flash": "LED",
                "HDR": "Tem",
                "Dual Shot": "Tem",
                "Localização": "Tem",
                "Detecção Facial": "Tem",
                "Câmera Frontal": "16 Mp F 2",
                # VÍDEO
                "\n6": "VÍDEO:",
                "Resolução da Gravação": "8K UHD",
                "Auto Focagem de Vídeo": "Tem",
                "FPS da Gravação": "30 fps",
                "Estabilização de Vídeo": "Tem",
                "Slow Motion": "240 fps",
                "Foto em Vídeo": "Tem",
                "Vídeo Camera Frontal": "Full HD, 60fps",
                "Opções da Câmera Frontal": "HDR",
            },
            "5": {
                # DADOS GERAIS
                "\n1": "DADOS GERAIS:",
                "Modelo": "Motorola",
                "Nome": "Moto E7",
                "Tipo": "Smartphone",
                "Sistema Operacional": "Android 10",
                "Disponibilidade": "2020/4",
                "Dimensões": "165 x 78.8 x 8.9 mm",
                "Peso": "180 gramas",
                # DADOS TÉCNICOS
                "\n2": "DADOS TÉCNICOS:",
                "Processador": "4x 2.0 GHz Cortex-A53 + 4x 1.5 GHz Cortex-A53",
                "Chipset": "Helio G25 MediaTek",
                "Memória RAM": "2 GB",
                "GPU": "PowerVR GE8320",
                "Armazenamento": "32 GB",
                "Memória Expansivel": "Slot híbrido SIM/MicroSD MicroSDXC atè 512 GB",
                # BATERIA
                "\n3": "BATERIA:",
                "Tipo": "LiPo",
                "Bateria": "4000 mAh",
                # TELA
                "\n4": "TELA:",
                "Tela": "6.5",
                "Resolução": "720 x 1600 pixel",
                "Densidade de Pixels": "270 ppi",
                "Tipo da Tela": "IPS LCD",
                "FPS": "60 Hz",
                "Cores": "16 milhões",
                # CÂMERA
                "\n5": "CÂMERA:",
                "Megapixels": "48Mp + 2Mp",
                "Resolução da Câmera": "8000 x 6000 pixel",
                "Tamanho do Sensor": "1/2.0 ''",
                "Aperture Size": "F 1.7 + F 2.4",
                "Estabilização": "Digital",
                "Ângulo máximo": "85 °",
                "Autofoco": "Tem",
                "Foco por Toque": "Tem",
                "Flash": "LED",
                "HDR": "Tem",
                "Dual Shot": "Tem",
                "Localização": "Tem",
                "Detecção Facial": "Tem",
                "Câmera Frontal": "5 Mp F 2.2",
                # VÍDEO
                "\n6": "VÍDEO:",
                "Resolução da Gravação": "Full HD",
                "Auto Focagem de Vídeo": "Tem",
                "FPS da Gravação": "30 fps",
                "Estabilização de Vídeo": "Não Tem",
                "Foto em Vídeo": "Tem",
                "Vídeo Camera Frontal": "Full HD, 30fps",
                "Opções da Câmera Frontal": "HDR",
            },
        }

    def especificacoes(self):
        while True:
            print("|================================|")
            print("|       Todos os Celulares       |")
            print("|1. S24 Ultra                    |")
            print("|2. A14 5G                       |")
            print("|3. Redmi 9A                     |")
            print("|4. Red Magic 9 Pro Plus         |")
            print("|5. Moto E7                      |")
            print("|0. Sair                         |")
            print("|================================|")
            escolha = input("Digite o número do Celular que você quer ver as especificações: ")

            if escolha == "0":
                print("Fim do Programa.")
                break
            elif escolha in self.celulares:
                celular = self.celulares.get(escolha)
                print(f"\nEspecificações do Celular: ")
                for chave, valor in celular.items():
                    print(f"{chave.capitalize()}: {valor}")
                print("\n")
            else:
                print("Número errado, tente novamente.")

class RelogioBase(ABC):
    def __init__(self, seg, min, hora, dia, mes, ano):
        self.seg = seg
        self.min = min
        self.hora = hora
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.ano_bi = 366
        self.ano_no = 365
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    @abstractmethod
    def informacoes(self):
        pass
    
    @abstractmethod
    def conversoes(self):
        pass

    @abstractmethod
    def verificacoes(self):
        pass
    
    # Funções de Informações
    def data(self):
        print("\n|===============================|")
        print("|             Data              |")
        print(f"|Dia: {self.dia}\t\t\t|")
        print(f"|Mês: {self.mes}\t\t\t|")
        print(f"|Ano: {self.ano}\t\t\t|")
        print("|===============================|\n")

    def horario(self):
        print("\n|===============================|")
        print("|            Horario            |")
        print(f"|Segundos: {self.seg}\t\t\t|")
        print(f"|Minutos: {self.min}\t\t\t|")
        print(f"|Hora: {self.hora}\t\t\t|")
        print("|===============================|\n")
        
    def fmeses(self):
        print("\n|===============================|")
        print("|             Meses             |")
        for i in range(12):
            print(f"|{i+1}. {self.meses[i]}\t\t\t|")
        print("|===============================|\n")

    # Funções de Conversões
    def seg_min(self):
        seg2=input("Diga de quantos segundos você quer transformar para minutos: ")
        r=(int(seg2)/60)
        print(f"De {seg2} segundos foram possiveis calcular {r} minutos")

    def min_seg(self):
        min2=input("Diga de quantos minutos você quer transformar para segundos: ")
        r=(int(min2)*60)
        print(f"De {min2} minutos foram possiveis calcular {r} segundos")

    def min_hora(self):
        min2=input("Diga de quantos minutos você quer transformar para horas: ")
        r=(int(min2)/60)
        print(f"De {min2} minutos foram possiveis calcular {r} horas")

    def hora_min(self):
        hora2=input("Diga de quantas horas você quer transformar para minutos: ")
        r=(int(hora2)*60)
        print(f"De {hora2} horas foram possiveis calcular {r} minutos")

    def seg_hora(self):
        seg2=input("Diga de quantos segundos você quer transformar para horas: ")
        r=(int(seg2)/3600)
        print(f"De {seg2} segundos foram possiveis calcular {r} horas")

    def hora_seg(self):
        hora2=input("Diga de quantos horas você quer transformar para segundos: ")
        r=(int(hora2)*3600)
        print(f"De {hora2} horas foram possiveis calcular {r} segundos")

    def dia_mes(self):
        dia2=input("Diga de quantos dias você quer transformar para meses: ")
        r=(int(dia2)/30)
        print(f"De {dia2} dias foram possiveis calcular {r} meses")

    def mes_dia(self):
        mes2=input("Diga de quantos meses você quer transformar para dias: ")
        r=(int(mes2)*30)
        print(f"De {mes2} meses foram possiveis calcular {r} dias")

    def mes_ano(self):
        mes2=input("Diga de quantos meses você quer transformar para anos: ")
        r=(int(mes2)/12)
        print(f"De {mes2} meses foram possiveis calcular {r} anos")

    def ano_mes(self):
        ano2=input("Diga de quantos anos você quer transformar para meses: ")
        r=(int(ano2)*12)
        print(f"De {ano2} anos foram possiveis calcular {r} meses")

    def ano_dia(self):
        ano2=input("Diga de quantos anos você quer transformar para dias: ")
        r=((int(ano2)/12)/30)
        print(f"De {ano2} anos foram possiveis calcular {r} dias")

    def dia_ano(self):
        dia2=input("Diga de quantos dias você quer transformar para anos: ")
        r=((int(dia2)*12)*30)
        print(f"De {dia2} dias foram possiveis calcular {r} anos")

    def ano_dec(self):
        ano2=input("Diga de quantos anos você quer transformar para décadas: ")
        r=(int(ano2)/10)
        print(f"De {ano2} anos foram possiveis calcular {r} décadas")

    def dec_ano(self):
        dec2=input("Diga de quantas décadas você quer transformar para anos: ")
        r=(int(dec2)*10)
        print(f"De {dec2} décadas foram possiveis calcular {r} anos")

    def dec_sec(self):
        dec2=input("Diga de quantas décadas você quer transformar para séculos: ")
        r=(int(dec2)/10)
        print(f"De {dec2} décadas foram possiveis calcular {r} séculos")

    def sec_dec(self):
        sec2=input("Diga de quantos séculos você quer transformar para décadas: ")
        r=(int(sec2)*10)
        print(f"De {sec2} séculos foram possiveis calcular {r} décadas")

    def sec_ano(self):
        sec2=input("Diga de quantos séculos você quer transformar para anos: ")
        r=(int(sec2)*100)
        print(f"De {sec2} séculos foram possiveis calcular {r} anos")

    def ano_sec(self):
        ano2=input("Diga de quantos anos você quer transformar para séculos: ")
        r=(int(ano2)*100)
        print(f"De {ano2} anos foram possiveis calcular {r} séculos")
        
    # Funções de Verificações
    def vr_bissexto(self):
        ano2=int(input("Diga qual o ano que você quer saber se é Bissexto: "))
        if (ano2 % 4 == 0 and ano2 % 100 != 0) or (ano2 % 400 == 0):
            print(f"O ano {ano2} é bissexto.")
        else:
            print(f"O ano {ano2} é normal.")

    def vr_data_hora(self):
        hora2=int(input("Digite as horas: "))
        min2=int(input("Digite os minutos: "))
        seg2=int(input("Digite os segundos: "))
        if (0 <= hora2 < 24) and (0 <= min2 < 60) and (0 <= seg2 < 60):
            print("Data e hora corretas.")
        else:
            print("Data e hora incorretas.")

class Relogio(RelogioBase):        
    def informacoes(self):
        while True:
            print("|===============================|")
            print("|          Informações          |")
            print("|1. Data                        |")
            print("|2. Horario                     |")
            print("|3. Meses                       |")
            print("|0. Sair                        |")
            print("|===============================|")
            con=input("Digite o número da Informação que você quer saber: ")
            match con:
                case "0":
                    self.all_f()
                    break

                case "1":
                    self.data()

                case "2":
                    self.horario()

                case "3":
                    self.fmeses()

                case _:
                    print("Número errado tente novamente.")
                    self.informacoes()

    def conversoes(self):
        while True:
            print("|==============================|")
            print("|          Conversões          |")
            print("|1. Seg para Min               |")
            print("|2. Min para Seg               |")
            print("|3. Seg para Hora              |")
            print("|4. Hora para Seg              |")
            print("|5. Dia para Mês               |")
            print("|6. Mês para Dia               |")
            print("|7. Mês para Ano               |")
            print("|8. Ano para Mês               |")
            print("|9. Ano para Dia               |")
            print("|10. Dia para Ano              |")
            print("|11. Ano para Década           |")
            print("|12. Década para Ano           |")
            print("|13. Década para Século        |")
            print("|14. Século para Década        |")
            print("|15. Século para Ano           |")
            print("|16. Ano para Século           |")
            print("|0. Sair                       |")
            print("|==============================|")
            con = input("Digite o número da Conversão que você quer fazer: ")
            match con:
                case "0":
                    self.all_f()
                    break
                
                case "1":
                    self.seg_min()
                    
                case "2":
                    self.min_seg()
                    
                case "3":
                    self.seg_hora()
                    
                case "4":
                    self.hora_seg()
                    
                case "5":
                    self.dia_mes()
                    
                case "6":
                    self.mes_dia()
                    
                case "7":
                    self.mes_ano()
                    
                case "8":
                    self.ano_mes()
                    
                case "9":
                    self.ano_dia()
                    
                case "10":
                    self.dia_ano()
                    
                case "11":
                    self.ano_dec()
                    
                case "12":
                    self.dec_ano()
                    
                case "13":
                    self.dec_sec()
                    
                case "14":
                    self.sec_dec()
                    
                case "15":
                    self.sec_ano()
                    
                case "16":
                    self.ano_sec()
                    
                case _:
                    print("Número errado tente novamente.")
                    self.conversoes()

    def verificacoes(self):
        while True:
            print("|======================================|")
            print("|             Verificações             |")
            print("|1. Se é ano Bissexto ou Normal        |")
            print("|2. Se a data e hora estão certas      |")
            print("|0. Sair                               |")
            print("|======================================|")
            con = input("Digite o número da Verificação que você quer fazer: ")
            match con:
                case "0":
                    self.all_f()
                    break
                
                case "1":
                    self.vr_bissexto()
                    
                case "2":
                    self.vr_data_hora()
                    
                case _:
                    print("Número errado tente novamente.")
                    self.verificacoes()
                
    def all_f(self):
        while True:
            print("|================================|")
            print("|        Todas as Funções        |")
            print("|1. Informações                  |")
            print("|2. Conversões                   |")
            print("|3. Verificações                 |")
            print("|0. Sair                         |")
            print("|================================|")
            con=input("Digite o número da Função que você quer usar: ")
            match con:
                case "0":
                    print("Fim do Programa.")
                    break

                case "1":
                    self.informacoes()

                case "2":
                    self.conversoes()

                case "3":
                    self.verificacoes()

                case _:
                    print("Número errado tente novamente.")
                    self.all_f()
            
class Relogioatt(Relogio):
    def __init__(self, seg, min, hora, dia, mes, ano):
        super().__init__(seg, min, hora, dia, mes, ano)
        # Mais inicializações se necessário

    def informacoes(self):
        super().informacoes()
        # Funcionalidades adicionais, se necessário

    def conversoes(self):
        super().conversoes()
        # Funcionalidades adicionais, se necessário

    def verificacoes(self):
        super().verificacoes()
        # Funcionalidades adicionais, se necessário

class Veiculo(ABC):
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.motor = False
        self.velocidade = 0
        self.distancia = 0

    def mudar_marcha(self):
        print("Mudando marcha.")

    def calcular_velocidade_media(self):
        if self.tempo > 0:
            velocidade_media = self.distancia / self.tempo
            print(f"Velocidade média: {velocidade_media} km/h")
        else:
            print("Tempo não pode ser zero.")

    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"Veículo pintado de {self.cor}.")

    def att_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço atualizado para {self.preco}.")
        
class Aviao(Veiculo):
    def __init__(self, companhia_aerea, modelo, ano, cor, tipo_motor, tipo_transmissao, vm, preco, disponibilidade, quilometragem):
        super().__init__(modelo, cor)
        self.companhia_aerea = companhia_aerea
        self.ano = ano
        self.tipo_motor = tipo_motor
        self.tipo_transmissao = tipo_transmissao
        self.vm = vm
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quilometragem = quilometragem

        self.altitude = 0
        self.tempo_voo = 0
        self.horas_motor = 0
        self.passageiros = 0
        self.carga = 0
        self.manutencao_registrada = False
        self.tempo_manutencao = 0

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor do avião {self.modelo} ligado.")
        else:
            print(f"O motor do avião {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            self.altitude = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 50
            print("Acelerando o avião.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 50
            print("Freando o avião.")
        else:
            print("O avião já está parado.")

    def decolar(self):
        if self.motor and self.velocidade >= 200:
            self.altitude += 10000
            print(f"Avião {self.modelo} decolou.")
        else:
            print("É necessário ligar o motor e acelerar mais para decolar.")

    def voar(self, distancia):
        if self.motor and self.altitude > 0:
            self.distancia += distancia
            self.tempo_voo += distancia / self.velocidade
            print(f"Avião {self.modelo} voou {distancia} km.")
        else:
            print("O avião precisa estar em altitude para voar.")

    def atualizar_quilometragem(self, km):
        self.quilometragem += km
        print(f"Quilometragem atualizada para {self.quilometragem} km.")

    def verificar_manutencao(self):
        if self.quilometragem > 10000:
            self.manutencao_registrada = True
            self.tempo_manutencao += 10
            print("Manutenção realizada.")
        else:
            print("Manutenção não necessária.")

    def info(self):
        print(f"Companhia Aérea: {self.companhia_aerea}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Altitude: {self.altitude} metros")
        print(f"Distância percorrida: {self.distancia} km")
        print(f"Tempo de voo: {self.tempo_voo} horas")
        print(f"Horas de motor: {self.horas_motor} horas")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Passageiros a bordo: {self.passageiros}")
        print(f"Carga a bordo: {self.carga} kg")
        if self.manutencao_registrada:
            print(f"Tempo total de manutenção: {self.tempo_manutencao} horas")
            
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, tipo_motor, tipo_transmissao, vm, preco, disponibilidade, quilometragem):
        super().__init__(modelo, cor)
        self.marca = marca
        self.ano = ano
        self.tipo_motor = tipo_motor
        self.tipo_transmissao = tipo_transmissao
        self.vm = vm
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quilometragem = quilometragem

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor do carro {self.modelo} ligado.")
        else:
            print(f"O motor do carro {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 10
            print("Acelerando o carro.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print("Freando o carro.")
        else:
            print("O carro já está parado.")

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Disponibilidade: {'Sim' if self.disponibilidade else 'Não'}")
        
class Moto(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(modelo, cor)
        self.marca = marca

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"A moto {self.marca} {self.modelo} acelerou para {self.velocidade} km/h.")

class Motoatt(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor da moto {self.modelo} ligado.")
        else:
            print(f"O motor da moto {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 5
            print("Acelerando a moto.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("Freando a moto.")
        else:
            print("A moto já está parada.")

    def info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")

# Exercícios Classes Abstratas

# Exercício 1
class Ingresso:
    def __init__(self, valor):
        self.valor=valor

    def imprimeValor(self):
        print(self.valor)

class VIP(Ingresso):
    def __init__(self, valor, valor_add):
        Ingresso.__init__(self, valor)
        self.valor_add=valor_add

    def imprimeValor(self):
        print(self.valor+self.valor_add)

# Exercício 2
class Forma:
    def __init__(self, area, perimetro):
        self.area=area
        self.primetro=perimetro

class Retangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=base*altura
        return self.area

    def calculaPerimetro(self, base, altura):
        self.perimetro=2*(base*altura)
        return self.perimetro

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=(base*altura)/2
        return self.area

    def calculaPerimetro(self, a, b, c):
        self.perimetro=a+b+c
        return self.perimetro

# Exercício 3
class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado=aposentado
        self.peso=peso

    def aposentar(self):
        self.aposentado=True

    def aquecer(self):
        print(f"{__name__} está aquecendo")

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def pedalar(self):
        print(f"{__name__} está pedalando")

class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def correr(self):
        print(f"{__name__} está correndo")

class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def nadar(self):
        print(f"{__name__} está nadando")

class TriAtleta(Ciclista, Corredor, Nadador):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

# Exercício 4
class ContaCorrente:
    def __init__(self, numero):
        self.numero=numero
        self.saldo=0.0

    def creditar(self, valor):
        self.saldo=self.saldo+valor

    def debitar(self, valor):
        self.saldo=self.saldo-valor

class Poupanca(ContaCorrente):
    def __init__(self, numero, taxa):
        ContaCorrente.__init__(self, numero)
        self.taxa=taxa

    def renderJuros(self):
        self.saldo=self.saldo+self.taxa*(self.saldo/100)

class ContaImposto(ContaCorrente):
    def __init__(self, numero, percentualImposto):
        ContaCorrente.__init__(self, numero)
        self.percentualImposto=percentualImposto

    def calculaImposto(self):
        self.saldo=self.saldo-(self.saldo*self.percentualImposto)
        
class OperacaoMatematica(ABC):
    @abstractmethod
    def calcula(self,a: int, b: int):
        raise NotImplementedError
        
class Soma(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        soma=a+b
        print(f"A soma de A + B é: {soma}")

class Subtracao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        subtracao=a-b
        print(f"A subtração de A - B é: {subtracao}")
        
class Multiplicacao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        multiplicacao=a*b
        print(f"A multiplicação de A * B é: {multiplicacao}")

class Divisao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        divisao=a/b
        print(f"A divisão de A / B é: {divisao}")
        
class Menu:
    def __init__(self) -> None:
        pass

    def menu(self):
        while True:
            print("="*50)
            print("Operações Matemáticas:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("0. Sair")
            print("="*50)
            i=input("Insira a sua escolha: ")
            match i:
                case "1":
                    som1=Soma()
                    som1.calcula(10,50)

                case "2":
                    sub1=Subtracao()
                    sub1.calcula(50,30)

                case "3":
                    mult1=Multiplicacao()
                    mult1.calcula(10,10)

                case "4":
                    div1=Divisao()
                    div1.calcula(10,5)

                case "0":
                    break

                case _:
                    print("Tente novamente.")
                    
class InfoCliente(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError
        
class InfoClientePessoaFisica(InfoCliente):
    def __init__(self,cpf: str):
        self.cpf=cpf

    def info(self):
        print(f"CPF: {self.cpf}")
        
class InfoClientePessoaJuridica(InfoCliente):
    def __init__(self,cnpj: str):
        self.cnpj=cnpj

    def info(self):
        print(f"CNPJ: {self.cnpj}")
        
class Cliente:
    def __init__(self,nome,endereco):
        self.nome=nome
        self.endereco=endereco
        
class ClienteFidelizacao(Cliente):
    def __init__(self,nome: str,endereco: str,bonus: float,validade: str):
        super().__init__(nome,endereco)
        self.bonus=bonus
        self.validade=validade

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Bonus: {self.bonus}")
        print(f"Validade: {self.validade}")

class Farol:
    def __init__(self,tipo,potencia):
        self.__tipo=tipo
        self.__potencia=potencia

    @property
    def tipo(self):
        return self.__tipo#getters
    
    @property
    def potencia(self):
        return self.__potencia#getters
    
    def acender(self):
        print("Acendendo farol...")

    def apagar(self):
        print("Apagando farol")
        
class MotoR:
    def __init__(self,marca,modelo):
        self.__marca=marca
        self.__modelo=modelo
        self.__farol=None
        self.farois=[]
        self.__qtdRodas=2

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def farol(self):
        return self.__farol
    
    @farol.setter
    def farol(self,farol):
        self.__farol=farol

    def liga(self):
        print("Ligando moto")

    def desliga(self):
        print("Desligando moto")

    def acelera(self):
        print("Acelerando moto")

    def freia(self):
        print("Freiando moto")

    def instalaFarol(self,farol):
        self.farois.append(farol)
        
class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
        
class Pedido:
    def __init__(self):
        self.itempedido = []

    def add_item(self, item):
        self.itempedido.append(item)

    def obter_total(self):
        self.valor_total = 0
        for item in self.itempedido:
            self.valor_total += item.valor_total()
        return self.valor_total

class ItemPedido(Produto):
    def __init__(self, codigo: int, valor: float, descricao: str, quantidade: int):
        super().__init__(codigo, valor, descricao)
        self.__quantidade = quantidade

    def quantidade(self) -> int:
        return self.__quantidade

    def valor_total(self) -> float:
        return self.valor * self.__quantidade
        
class DVDMIDIA:
    pass
    
class DVDPLAYER:
    def play(self,filme):
        self.filme=filme
        
class Pessoa:
    def __init__(self,nome: str,cpf: str,AnoNascimento: int):
        self.__nome=nome
        self.__cpf=cpf
        self.__AnoNascimento=AnoNascimento

    def setNome(self,valor: str):
        self.__nome=valor

    def setCPF(self,valor: str):
        self.__cpf=valor

    def setAnoNascimento(self,valor: int):
        self.__AnoNascimento=valor
    
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getCPF(self):
        return self.__cpf
    
    @property
    def getAnoNascimento(self):
        return self.__AnoNascimento
        
class Musico(Pessoa):
    def __init__(self,nome: str,cpf: str,AnoNascimento: int,instrumentista: bool,cantor: bool,compositor: bool):
        super().__init__(nome,cpf,AnoNascimento)
        self.__instrumentista=instrumentista
        self.__cantor=cantor
        self.__compositor=compositor

    def setInstrumentista(self,valor: bool):
        self.__instrumentista=valor

    def setCantor(self,valor: bool):
        self.__cantor=valor

    def setCompositor(self,valor: bool):
        self.__compositor=valor

    def getInstrumentista(self):
        return self.__instrumentista

    def getCantor(self):
        return self.__cantor

    def getCompositor(self):
        return self.__compositor

class Engenheiro(Pessoa):
    def __init__(self,nome: str,cpf: str,AnoNascimento: int,numeroCREA: str):
        super().__init__(nome,cpf,AnoNascimento)
        self.__numeroCREA=numeroCREA

    def setNumeroCREA(self,valor: str):
        self.__numeroCREA=valor

    @property
    def getNumeroCREA(self):
        return self.__numeroCREA
        
class Baterista:
    def toca_com(self,classe):
        print(f"{classe} toca com Baterista")
        
class Saxofonista:
    def toca_com(self,classe):
        print(f"{classe} toca com Saxofonista")

class Musico2:
    def toca_em(self,classe):
        print(f"{classe} toca em Orquestra")

class Orquestra:
    def toca_em(self,classe):
        print(f"{classe} toca em Orquestra")

class Baterista2:
    def __init__(self):
        self.saxofonista = []
    
    def add_saxofonista(self,saxofonista):
        self.saxofonista.append(saxofonista)
    
    def toca_com(self):
        for classe in self.saxofonista:
            print(f"{classe} toca com Baterista")
            
class Saxofonista2:
    def toca_com(self,classe):
        print(f"{classe} toca com Saxofonista")
        
class Musico3:
    def toca_em(self,classe):
        print(f"{classe} toca em Orquestra")
        
class Orquestra2:
    def __init__(self):
        self.musico = []
    
    def add_musico(self,musico):
        self.musico.append(musico)
    
    def toca_em(self):
        for classe in self.musico:
            print(f"{classe} toca em Orquestra")

class Aluno:
    pass
    
class Curso:
    def __init__(self,aluno):
        self.aluno=aluno

class Casa:
    def contem(self,classe):
        print(f"{classe} contem")
        
class TabuleiroDeXadrez:
    def contem(self,classe):
        print(f"{classe} contem[64]")

class C1:
    pass

class C2:
    pass

class PropriedadesDaRelacao(C1, C2):
    pass
    
class School:
    pass
    
class Department:
    def has(self,classe):
        print(f"Department has {classe}")
        
class Student:
    def attends(self,classe):
        print(f"Student attends {classe}")
    
    def member(self,classe):
        print(f"Student member {classe}")

class Course:
    pass
    
class Instructor:
    def teaches(self,classe):
        print(f"Instructor teaches {classe}")
        
    def assignedTo(self,classe):
        print(f"Instructor assignedTo {classe}")

class Carro2:
    def __init__(self,ano: int,modelo: str,placa: str,cor: str):
        self.ano=ano
        self.modelo=modelo
        self.placa=placa
        self.cor=cor

    def acelerar(self):
        print("O carro está acelerando a 2000 km/h")

    def frear(self):
        print("O carro está à 50 km/h")

    def businar(self):
        print("Barulho de busina")

class Mestre:
    def __init__(self,nome: str, anoNascimento: int, afiliacao: str, posto: str):
        self.nome=nome
        self.anoNascimento=anoNascimento
        self.afiliacao=afiliacao
        self.posto=posto

    def getIdade(self, anoReferencia: int):
        idade = anoReferencia - self.anoNascimento
        return idade

    def possuiForca(self):
        if self.posto=="Jedi" or self.posto=="Sith":
            return True
        
        else:
            return False
        
    def getAnoNascimentoString(self):
        if self.anoNascimento<0:
            saida = str(self.anoNascimento) + "ABY"
        
        else:
            saida = str(self.anoNascimento) + "DBY"
        
        return saida
        
    def getDescricao(self):
        saida = f"Mestre: nome={self.nome}, anoNascimento={self.getAnoNascimentoString()}, afiliacao={self.afiliacao}, posto={self.posto}, possuiForca={self.possuiForca()}"
        return saida

class Sensor:
    def __init__(self, cor: str, resolucao: float, framesPorSegundo: int):
        self.cor=cor
        self.resolucao=resolucao
        self.framesPorSegundo=framesPorSegundo

    def getMPixelsPorSegundo(self):
        saida = self.resolucao * float(self.framesPorSegundo)
        return saida

    def getDescricao(self):
        saida = f"Sensor: {self.cor}, resolucao={self.resolucao}Mp, framesPorSegundo={self.framesPorSegundo}fps, mPixelsPorSegundo={self.getMPixelsPorSegundo()}Mpps"
        return saida

class Conexao:
    def __init__(self, tipoPorta: str, idProtocolo: int, taxaTransmissao: int):
        self.tipoPorta=tipoPorta
        self.idProtocolo=idProtocolo
        self.taxaTransmissao=taxaTransmissao

    def getProtocoloString(self):
        if self.idProtocolo==1:
            return "Rotoscope"
        
        elif self.idProtocolo==2:
            return "Acustico"
        
        elif self.idProtocolo==3:
            return "Radio"
        
        else:
            return "Outros"

    def getTaxaMBps(self):
        saida = self.taxaTransmissao/1024
        return saida

    def getDescricao(self):
        saida = f"Conexao: tipoPorta={self.tipoPorta}, potocolo={self.getProtocoloString()}, taxaTransmissao={self.getTaxaMBps()}MBps"
        return saida

class Astromech:
    def __init__(self, modelo: str, mestre: Mestre, sensor: Sensor, conexao: Conexao):
        self.modelo=modelo
        self.mestre=mestre
        self.sensor=sensor
        self.conexao=conexao

    def getDescricao(self):
        saida = f"Astromech modelo {self.modelo}. \n{self.mestre.getDescricao()}. \n{self.sensor.getDescricao()}. \n{self.conexao.getDescricao()}"
        return saida

class IniciadoJedi:
    def __init__(self,nome: str,especie: str,anoNascimento: int):
        self.nome=nome
        self.especie=especie
        self.anoNascimento=anoNascimento

    def getDescricao(self):
        return f"{self.nome} (especie={self.especie}, nascimento={self.getAnoNascimento()})"

    def getAnoNascimento(self):
        if self.anoNascimento<0:
            saida = f"{self.anoNascimento} DBY"
        
        else:
            saida = f"{self.anoNascimento} ABY"
        
        return saida

class TreinadorJedi:
    def __init__(self,titulacao: str, nome: str):
        self.titulacao=titulacao
        self.nome=nome

    def getDescricao(self):
        return f"{self.titulacao} {self.nome}"
    
class SessaoJedi:
    def __init__(self,nome: str, treinador: TreinadorJedi):
        self.nome=nome
        self.treinador=treinador
        self.iniciados=[]

    def addIniciado(self,iniciado: str):
        self.iniciados.append(iniciado)

    def getIniciado(self,nome: str):
        for i in self.iniciados:
            if nome==i:
                return i.nome

        return None

    def getMediaAnoNascimento(self):
        media=0
        i=0
        for iniciados in self.iniciados:
            media=iniciados.anoNascimento+media
            i=i+1
        media=media/i
        return media

    def getDescricao(self):
        saida=f"--> SESSÃO {self.nome} (Treinador: {self.treinador.getDescricao()})"
        for iniciados in self.iniciados:
            saida=f"{saida}\n - Iniciado: {iniciados.getDescricao()}"

        return saida
    
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

class Atividades:
    def a1(self):
        print("1. Calcule a média de valores da lista de números abaixo:\nlista_numeros = [10, 50, 30, 20, 50, 60, 75, 90]\n")
        lista_numeros=[10, 50, 30, 20, 50, 60, 75, 90]
        
        soma=0
        
        for i in lista_numeros:
            soma+=i
            
        media=soma/len(lista_numeros)
        print(media)

    def a2(self):
        print("2. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.\nDepois modifique o programa para que ele mostre os números um ao lado do outro.\n")
        saida=""
        
        for i in range(1, 20):
            saida+=f"{i}\n"
            
        print(saida)
        
        saida=""
        
        for i in range(1, 20):
            saida+=f"{i} "
            
        print(saida)
    
    def a3(self):
        print("3. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.\n")
        saida=""
        for i in range(50):
            if i%2==1:
                saida+=f"{i} "
        print(saida)

    def a4(self):
        print("4. Faça um programa que, dado a lista de números abaixo, determine o menor valor, o maior valor e a soma dos valores.\nlista_numeros = [5, 2, 1, 8, 10, 30, 50, 9, 22, 11, 7]\n")
        lista_numeros = [5, 2, 1, 8, 10, 30, 50, 9, 22, 11, 7]

        menor_valor = lista_numeros[0]
        maior_valor = lista_numeros[0]
        soma_valores = 0

        for numero in lista_numeros:
            soma_valores += numero

            if numero < menor_valor:
                menor_valor = numero
            
            if numero > maior_valor:
                maior_valor = numero

        print(f"Menor valor: {menor_valor}")
        print(f"Maior valor: {maior_valor}")
        print(f"Soma dos valores: {soma_valores}")
    
    def a5(self):
        print("5. Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, João e Pedro. Com base nas listas, imprima qual amigo gastou mais.\ngastos_joao = [300, 500, 200, 800]\ngastos_pedro = [200, 400, 500, 700]\n")
        gastos_joao = [300, 500, 200, 800]
        gastos_pedro = [200, 400, 500, 700]
        
        soma_joao=0
        soma_pedro=0
        
        for i in gastos_joao:
            soma_joao+=i
            
        for i in gastos_pedro:
            soma_pedro+=i
            
        if soma_joao>soma_pedro:
            print("João gastou mais que Pedro")
        else:
            print("Pedro gastou mais que João")
        
    def a6(self):
        print("6. Partindo de uma lista de palavras qualquer, como:\npalavras = ['python', 'asimov', 'código', 'web', 'programação']\nCrie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).\n")
        palavras = ["python", "asimov", "código", "web", "programação"]

        maior_palavra = palavras[0]
        menor_palavra = palavras[0]

        for palavra in palavras:
            if len(palavra) > len(maior_palavra):
                maior_palavra = palavra
            
            if len(palavra) < len(menor_palavra):
                menor_palavra = palavra

        print(f"Maior palavra: {maior_palavra}")
        print(f"Menor palavra: {menor_palavra}")
    
    def a7(self):
        print("7. Você fez uma pequena pesquisa de preferência entre três produtos A, B e C. Na entrevista, cada entrevistado precisava escolher seu produto preferido. Os votos obtidos nessa pesquisa estão representados na lista abaixo:\nvotos = ['A', 'B', 'A', 'C', 'C', 'A', 'C', 'C', 'B', 'A']\nAgora, seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, crie um dicionário onde a chave é cada produto, e o valor é o número de votos que o produto recebeu.\n")
        votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

        contagem_votos = {}

        for voto in votos:
            if voto in contagem_votos:
                contagem_votos[voto] += 1
            else:
                contagem_votos[voto] = 1

        print(contagem_votos)

        produto_mais_votado = max(contagem_votos, key=contagem_votos.get)
        print(f"Produto mais votado: {produto_mais_votado} ({contagem_votos[produto_mais_votado]} votos)")
    
    def a8(self):
        print("8. Calcule a soma de todos os números pares entre 2 e 100 (inclusive)\n")
        soma=0
        for i in range(100):
            if i%2==0:
                soma=+i
        print(soma)
    
    def a9(self):
        print("9. Calcule a soma de todos os quadrados entre 1 e 100 (inclusive)\nObs: para elevar um número ao quadrado utilize o “**2” logo após o número.\nExemplo: 2**2 = 4\n")
        soma=0
        for i in range(100):
            q=i**2
            soma+=q
        print(soma)
        
    def a10(self):
        print("""
10. O que estes laços imprimem?
a. for i in range(1, 10):
    print(i)
b. for i in range(1, 10, 2):
    print(i)
c. for i in range(10, 1, ‐1):
    print(i)
d. for i in range(10):
    print(i)
e. for i in range(1, 10):
    if i % 2 == 0:
        print(i)
""")
        print("""a. 
1
2
3
4
5
6
7
8
9
""")
        print("""b.
1
3
5
7
9
""")
        print(f"c. Erro: SyntaxError: invalid character '‐' (U+2010)")
            
        print("""d.
0
1
2
3
4
5
6
7
8
9
""")
        print("""d.
2
4
6
8
""")

    def a11(self):
        print("""11. Quantas iterações os seguintes laços executam?
a. for i in range(1, 11) . . .
b. for i in range(10) . . .
c. for i in range(10, 0, −1) . . .
d. for i in range(−10, 11) . . .
e. for i in range(10, 0) . . .
f. for i in range(−10, 11, 2) . . .
g. for i in range(−10, 11, 3) . . .""")

        print("""
Interações:
a: 10
b: 10
c: 10
d: 21
e: 0
f: 11
g: 7""")
    
    def a12(self):
        print("""
12. O que o seguinte segmento de programa imprime? Encontre a resposta, rastreando
o código, não usando o computador.
a. n = 1
for i in range(2, 5) :
n = n + i
print(n)
""")
        print("""A saída é: 
3
6
10""")
    
    def a13(self):
        faltas = [["Brasil", "Italia", [10, 9]], 
                ["Brasil", "Espanha", [5, 7]], 
                ["Italia", "Espanha", [7, 8]]]

        total_faltas = {}

        for jogo in faltas:
            time1, time2, (faltas_time1, faltas_time2) = jogo
            
            if time1 in total_faltas:
                total_faltas[time1] += faltas_time1
            else:
                total_faltas[time1] = faltas_time1
            
            if time2 in total_faltas:
                total_faltas[time2] += faltas_time2
            else:
                total_faltas[time2] = faltas_time2

        total_campeonato = sum(total_faltas.values())
        print(f"Total de faltas do campeonato: {total_campeonato}")

        time_mais_faltas = max(total_faltas, key=total_faltas.get)
        print(f"Time que fez mais faltas: {time_mais_faltas} com {total_faltas[time_mais_faltas]} faltas")

        time_menos_faltas = min(total_faltas, key=total_faltas.get)
        print(f"Time que fez menos faltas: {time_menos_faltas} com {total_faltas[time_menos_faltas]} faltas")
        
    def __init__(self):
        funcoes=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11,self.a12,self.a13]
        n=1
        for i in funcoes:
            print(f"Atividade {n}:")
            i()
            print("\n")
            n+=1
            
class Animal2(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
        
class Cachorro2(Animal2):
    def emitir_som(self):
        print("Au au!")
        
class Gato2(Animal2):
    def emitir_som(self):
        print("Miau!")
        
class FormaGeometrica(ABC):
    def __init__(self, posX:int, posY: int):
        self.posX = posX
        self.posY = posY
        
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimetro(self):
        pass
    
    def getPosString(self):
        saida = "posicao (" + str(self.posX) + ", " + str(self.posY) + ")"
        return saida
        
class Circulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, raio: float):
        super().__init__(posX, posY)
        self.raio = raio
        
    def getArea(self):
        super().getArea()
        return math.pi * self.raio**2
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * math.pi * self.raio
    
    def toString(self):
        print(f"Círculo na posição {super().getPosString()} com raio de {self.raio}cm")
        
class Retangulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, largura: float, altura: float):
        super().__init__(posX, posY)
        self.largura = largura
        self.altura = altura
        
    def getArea(self):
        super().getArea()
        return self.largura * self.altura
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * (self.largura + self.altura)
    
    def toString(self):
        print(f"Retangulo na posição {super().getPosString()} com largura de {self.largura}")
        
class Pessoa2(ABC):
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        raise NotImplementedError
    
class Professor2(Pessoa2):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Professor2.")
        
class Aluno2(Pessoa2):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Aluno2.")
        
class SerVivo(ABC):
    @abstractmethod
    def respirar(self):
        raise NotImplementedError
    
class Macaco(SerVivo):
    def respirar(self):
        print("Respirando como um macaco")

class Humano(SerVivo):
    def respirar(self):
        print("Respirando como um humano")
            
class Menu:
    def __init__(self, titulo: str, opcoes: list[str]):
        self.titulo = titulo
        self.opcoes = opcoes
        self.largura = 50  # Define a largura máxima do menu

    def desenhar(self):
        # Linha superior
        print(f"|{'=' * (self.largura - 2)}|")
        
        # Título centralizado
        print(f"|{self.titulo.center(self.largura - 2)}|")
        
        # Opções formatadas
        i=1
        for idx, opcao in enumerate(self.opcoes, start=1):
            linha = f"{idx}. {opcao}"  # Exemplo: "1. Comprimento"
            print(f"|{linha.ljust(self.largura - 2)}|")
            i+=1
        # Linha para a opção "Voltar"
        print(f"|{i}{'. Ver Histórico'.ljust(self.largura - 3)}|")
        print(f"|{'0. Voltar'.ljust(self.largura - 2)}|")
        
        # Linha inferior
        print(f"|{'=' * (self.largura - 2)}|")

class Base:
    @staticmethod
    def dec_bin(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            bin_inteira = bin(parte_inteira)[2:]
            bin_decimal = []
            while parte_decimal > 0 and len(bin_decimal) < 20:  # Limite para precisão
                parte_decimal *= 2
                bit = int(parte_decimal)
                bin_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{bin_inteira}.{''.join(bin_decimal)}"
        else:
            resultado = bin(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else bin(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_oct(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            oct_inteira = oct(parte_inteira)[2:]
            oct_decimal = []
            while parte_decimal > 0 and len(oct_decimal) < 20:  # Limite para precisão
                parte_decimal *= 8
                bit = int(parte_decimal)
                oct_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{oct_inteira}.{''.join(oct_decimal)}"
        else:
            resultado = oct(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else oct(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_hex(numero):
        if isinstance(numero, float):
            import struct
            hexadecimal = struct.pack('>f', numero).hex()  # IEEE 754
            resultado = f"0x{hexadecimal}"
        else:
            resultado = hex(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else hex(int(numero))[2:]
        return resultado

    @staticmethod
    def bin_dec(binario):
        """Converte um número binário para decimal."""
        return int(binario, 2)

    @staticmethod
    def oct_dec(octal):
        """Converte um número octal para decimal."""
        return int(octal, 8)

    @staticmethod
    def hex_decl(hexadecimal):
        """Converte um número hexadecimal para decimal."""
        return int(hexadecimal, 16)

    @staticmethod
    def dec_para_qualquer_base(numero, base):
        """Converte um número decimal para qualquer base (2 a 36)."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while numero > 0:
            resultado = caracteres[numero % base] + resultado
            numero //= base
        return resultado or "0"

    @staticmethod
    def qualquer_base_para_dec(numero, base):
        """Converte um número de qualquer base (2 a 36) para decimal."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        return int(numero, base)

    def raiz_quadrada(self, num):
        """Calcula a raiz quadrada de um número usando o método de Newton."""
        if num < 0:
            return complex(0, abs(num) ** 0.5)  # Para números negativos, retorna a parte imaginária
        x = num
        y = (x + 1) / 2
        while y < x:
            x = y
            y = (x + num / x) / 2
        return x

    def saida(self, num):
        print(f"Sistemas: Decimal: {num}, Octal: {self.dec_oct(num)}, Hexadecimal: {self.dec_hex(num)}, Binário {self.dec_bin(num)}")

    def __def__():
        nome_funcao = inspect.currentframe().f_code.co_name
        print("O nome desta função é:", nome_funcao)

class Utilitarios:
    def __init__(self):
        menu_opcoes = ["Utilitários Matemáticos","Verificadores de Números","Utilitários de Texto","Conversores de Unidades","Finanças","Jogos"]
        while True:
            menu = Menu("Menu Principal", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": 
                    print("Fim do Programa.")
                    break
                case "1": UttsMaths()
                case "2": VerifNums()
                case "3": UttsTexto()
                case "4": ConvUni()
                case "5": Financas()
                case "6": Jogos()
                case _: print("Opção inválida. Por favor, escolha novamente.")
                
class UttsMaths:
    def __init__(self):
        menu_opcoes=["Calculadora Completa","Tabuada","Funções Matemáticas","Calculo de Estatística","Resolver Equações","Operações com Vetores","Operações com Matrizes","Geometria","Teorema","Número Complexo"]
        while True:
            menu = Menu("Utilitários Matemáticos", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": return
                case "1": CalculadoraCompleta()
                case "2": Tabuada()
                case "3": FuncoesMatematicas()
                case "4": Estatisticas()
                case "5": Equacoes()
                case "6": OperacoesVetores()
                case "7": OperacoesMatrizes()
                case "8": Geometria()
                case "9": Teoremas()
                case "10": NumeroComplexo()
                case "11": Fracao()
                case _: print("Opção inválida. Por favor, escolha novamente.")
              
class CalculadoraCompleta(Base):
    def __init__(self):
        """Exibe o menu de operações da calculadora."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes=["Adição","Subtração","Multiplicação","Divisão","Potência","Raiz Quadrada","Fatorial","Combinação","Permutação","Derivada","Integral"]
        menu = Menu("Calculadora Completa", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")
            match opcao:
                case "0": return
                case "1": self.operacao("Adição", self.adicao)
                case "2": self.operacao("Subtração", self.subtracao)
                case "3": self.operacao("Multiplicação", self.multiplicacao)
                case "4": self.operacao("Divisão", self.divisao, divisao=True)
                case "5": self.operacao("Potência", self.potencia, potencia=True)
                case "6": self.operacao("Raiz Quadrada", self.raiz_quadrada, raiz_quadrada=True)
                case "7": self.operacao_fatorial()
                case "8": self.operacao_combinacao()
                case "9": self.operacao_permutacao()
                case "10": self.calcular_derivada()
                case "11": self.calcular_integral()
                case "12": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")

    def operacao_fatorial(self):
        n = int(input("Digite n: "))
        resultado = self.fatorial(n)
        print(f"Fatorial de {n}: {resultado}")
        self.adicionar_historico(f"Fatorial de {n}", resultado)

    def operacao_combinacao(self):
        n = int(input("Digite n: "))
        k = int(input("Digite k: "))
        resultado = self.combinacao(n, k)
        print(f"Combinação C({n},{k}): {resultado}")
        self.adicionar_historico(f"Combinação C({n},{k})", resultado)

    def operacao_permutacao(self):
        n = int(input("Digite n: "))
        k = int(input("Digite k: "))
        resultado = self.permutacao(n, k)
        print(f"Permutação P({n},{k}): {resultado}")
        self.adicionar_historico(f"Permutação P({n},{k})", resultado)

    def operacao(self, nome_operacao, operacao, divisao=False, potencia=False, raiz_quadrada=False):
        """Realiza operações matemáticas básicas e avançadas."""
        try:
            if divisao:
                a = float(input("Entre com o dividendo: "))
                b = float(input("Entre com o divisor: "))
                if b == 0:
                    print("Erro: Divisão por zero não permitida.")
                    return
                resultado = operacao(a, b)
            elif potencia:
                a = float(input("Entre com a base: "))
                b = float(input("Entre com o expoente: "))
                resultado = operacao(a, b)
            elif raiz_quadrada:
                num = float(input("Entre com o número: "))
                resultado = operacao(num)
            else:
                a = float(input("Entre com o primeiro número: "))
                b = float(input("Entre com o segundo número: "))
                resultado = operacao(a, b)
            
            print(f"Resultado da {nome_operacao}: {resultado}")
            self.adicionar_historico(f"{nome_operacao} de {a} e {b}", resultado)
        except ValueError:
            print("Erro: Entrada inválida.")

    def adicao(self, a, b):
        r = a + b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def subtracao(self, a, b):
        r = a - b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def multiplicacao(self, a, b):
        r = a * b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def divisao(self, a, b):
        r = a / b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def potencia(self, a, b):
        r = a ** b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def fatorial(self, n):
        """Calcula o fatorial de um número inteiro não negativo."""
        if n < 0:
            raise ValueError("Fatorial não é definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def combinacao(self, n, k):
        """Calcula a combinação de n elementos tomados k a k."""
        if k > n:
            return 0
        return self.fatorial(n) // (self.fatorial(k) * self.fatorial(n - k))

    def permutacao(self, n, k):
        """Calcula a permutação de n elementos tomados k a k."""
        if k > n:
            return 0
        return self.fatorial(n) // self.fatorial(n - k)

    def calcular_derivada(self):
        print("Cálculo de Derivada de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        derivada = [(n - i) * coeficientes[i] for i in range(len(coeficientes) - 1)]
        derivada_str = " + ".join(f"{coef}x^{n - i - 1}" for i, coef in enumerate(derivada) if coef != 0)
        print("Derivada: ", derivada_str)
        self.adicionar_historico(f"Derivada do polinômio de grau {n}", derivada_str)

    def calcular_integral(self):
        print("Cálculo de Integral de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        integral = [coeficientes[i] / (n - i + 1) for i in range(len(coeficientes))]
        integral_str = " + ".join(f"{coef}x^{n - i + 1}" for i, coef in enumerate(integral))
        print("Integral: ", integral_str)
        self.adicionar_historico(f"Integral do polinômio de grau {n}", integral_str)
        
    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

# --- TABUADA ---
class Tabuada:
    def __init__(self):
        """Mostra a tabuada de multiplicação para um número dado, com intervalo definido pelo usuário."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Tabuada"]
        menu = Menu("Funções Matemáticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    try:
                        num = int(input("Digite o número para ver sua tabuada: "))
                        inicio = int(input("Digite o início do intervalo: "))
                        fim = int(input("Digite o fim do intervalo: "))
                        for i in range(inicio, fim + 1):
                            resultado = num * i
                            print(f"{num} x {i} = {resultado}")
                            self.adicionar_historico(num, i, resultado)
                    except ValueError:
                        print("Erro: Entrada inválida.")
                case "2": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, num, i, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{num} x {i} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

# --- FUNÇÕES MATEMÁTICAS ---
class FuncoesMatematicas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Logaritmo", "Exponencial", "Seno", "Cosseno", "Tangente"]
        menu = Menu("Funções Matemáticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            num = float(input("Digite o número: "))
            match func:
                case "1":
                    resultado = self.logaritmo(num)
                    print(f"Logaritmo de {num}: {resultado}")
                    self.adicionar_historico("Logaritmo", num, resultado)
                case "2":
                    resultado = self.exponencial(num)
                    print(f"Exponencial de {num}: {resultado}")
                    self.adicionar_historico("Exponencial", num, resultado)
                case "3":
                    resultado = self.seno(num)
                    print(f"Seno de {num}: {resultado}")
                    self.adicionar_historico("Seno", num, resultado)
                case "4":
                    resultado = self.cosseno(num)
                    print(f"Cosseno de {num}: {resultado}")
                    self.adicionar_historico("Cosseno", num, resultado)
                case "5":
                    resultado = self.tangente(num)
                    print(f"Tangente de {num}: {resultado}")
                    self.adicionar_historico("Tangente", num, resultado)
                case "6": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, funcao, num, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{funcao} de {num} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def logaritmo(self, x, base=10):
        """Calcula o logaritmo de x na base especificada."""
        if x <= 0:
            raise ValueError("Logaritmo indefinido para valores menores ou iguais a zero.")
        return self.exponencial(self.logaritmo_base_e(x)) / self.exponencial(self.logaritmo_base_e(base))

    def logaritmo_base_e(self, x):
        """Calcula o logaritmo natural (base e) usando a série de Taylor."""
        if x <= 0:
            raise ValueError("Logaritmo indefinido para valores menores ou iguais a zero.")
        resultado = 0
        termo = (x - 1)  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo / n
            n += 1
            termo *= (x - 1) / n
        return resultado

    def exponencial(self, x):
        """Calcula e^x usando a série de Taylor."""
        resultado = 1.0
        termo = 1.0
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            termo *= x / n
            resultado += termo
            n += 1
        return resultado

    def seno(self, x):
        """Calcula o seno de x usando a série de Taylor."""
        resultado = 0.0
        termo = x  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo
            termo *= -x * x / ((2 * n) * (2 * n + 1))  # Fórmula do termo seguinte
            n += 1
        return resultado

    def cosseno(self, x):
        """Calcula o cosseno de x usando a série de Taylor."""
        resultado = 0.0
        termo = 1.0  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo
            termo *= -x * x / ((2 * n - 1) * (2 * n))  # Fórmula do termo seguinte
            n += 1
        return resultado

    def tangente(self, x):
        """Calcula a tangente de x como seno/cosseno."""
        seno_val = self.seno(x)
        cosseno_val = self.cosseno(x)
        if cosseno_val == 0:
            raise ValueError("Tangente indefinida para valores onde o cosseno é zero.")
        return seno_val / cosseno_val
        
class Estatisticas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calcular Média", "Calcular Mediana", "Calcular Moda", "Calcular Desvio Padrão"]
        menu = Menu("Estatísticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            if func == "0":
                return
            numeros = input("Digite os números separados por vírgula: ")
            lista_numeros = [float(num.strip()) for num in numeros.split(",")]
            match func:
                case "1":
                    resultado = self.calcular_media(lista_numeros)
                    print(f"Média: {resultado}")
                    self.adicionar_historico("Média", lista_numeros, resultado)
                case "2":
                    resultado = self.calcular_mediana(lista_numeros)
                    print(f"Mediana: {resultado}")
                    self.adicionar_historico("Mediana", lista_numeros, resultado)
                case "3":
                    resultado = self.calcular_moda(lista_numeros)
                    print(f"Moda: {resultado}")
                    self.adicionar_historico("Moda", lista_numeros, resultado)
                case "4":
                    resultado = self.calcular_desvio_padrao(lista_numeros)
                    print(f"Desvio Padrão: {resultado}")
                    self.adicionar_historico("Desvio Padrão", lista_numeros, resultado)
                case "5": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, funcao, numeros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{funcao} de {numeros} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def calcular_media(self, lista):
        """Calcula a média de uma lista de números."""
        return sum(lista) / len(lista) if lista else 0

    def calcular_mediana(self, lista):
        """Calcula a mediana de uma lista de números."""
        lista.sort()
        n = len(lista)
        meio = n // 2
        if n % 2 == 0:
            return (lista[meio - 1] + lista[meio]) / 2
        else:
            return lista[meio]

    def calcular_moda(self, lista):
        """Calcula a moda de uma lista de números."""
        contagem = Counter(lista)
        max_freq = max(contagem.values())
        modas = [num for num, freq in contagem.items() if freq == max_freq]
        return modas

    def calcular_desvio_padrao(self, lista):
        """Calcula o desvio padrão de uma lista de números."""
        media = self.calcular_media(lista)
        variancia = sum((x - media) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5

class Equacoes(Base):
    def __init__(self):
        """Resolve equações de primeiro e segundo grau."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Primero Grau", "Segundo Grau"]
        menu = Menu("Equações", menu_opcoes)
        while True:
            menu.desenhar()
            grau = input("Escolha uma opção: ")
            try:
                if opcao == "1":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    solucao = -b / a
                    print(f"Solução da equação linear: x = {solucao}")
                    self.adicionar_historico("Equação de 1º grau", a, b, solucao)
                elif opcao == "2":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    c = float(input("Coeficiente c: "))
                    discriminante = b**2 - (4 * a * c)
                    if discriminante >= 0:
                        raiz1 = (-b + self.raiz_quadrada(discriminante)) / (2 * a)
                        raiz2 = (-b - self.raiz_quadrada(discriminante)) / (2 * a)
                        print(f"As raízes são x1 = {raiz1} e x2 = {raiz2}")
                        self.adicionar_historico("Equação de 2º grau", a, b, c, raiz1, raiz2)
                    else:
                        print("Sem solução real.")
                elif opcao == "3": self.ver_historico()
            except ValueError:
                print("Erro: Entrada inválida.")

    def adicionar_historico(self, tipo_equacao, *coeficientes):
        """Adiciona a solução ao histórico."""
        if len(coeficientes) == 3:  # Primeiro grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]} => x={coeficientes[2]}")
        elif len(coeficientes) == 5:  # Segundo grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]}, c={coeficientes[2]} => x1={coeficientes[3]}, x2={coeficientes[4]}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)
            
class OperacoesVetores:
    def __init__(self):
        """Realiza operações com vetores."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Subtração", "Produto Escalar", "Produto Vetorial"]
        menu = Menu("Operações com Vetores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")

            tamanho = int(input("Digite o tamanho dos vetores: "))
            print("Preencha os valores do primeiro vetor:")
            vetor1 = Vetor.criar_vetor(tamanho)

            print("Preencha os valores do segundo vetor:")
            vetor2 = Vetor.criar_vetor(tamanho if opcao in ["1", "2", "3"] else 3)  # Produto vetorial exige vetores 3D
            match opcao:
                case "1":
                    self.resultado = vetor1.adicionar(vetor2)
                    self.adicionar_historico("Adição", vetor1, vetor2, self.resultado)
                case "2":
                    self.resultado = vetor1.subtrair(vetor2)
                    self.adicionar_historico("Subtração", vetor1, vetor2, self.resultado)
                case "3":
                    escalar = vetor1.produto_escalar(vetor2)
                    print(f"Resultado do Produto Escalar: {escalar}")
                    self.adicionar_historico("Produto Escalar", vetor1, vetor2, escalar)
                    continue
                case "4":
                    self.resultado = vetor1.produto_vetorial(vetor2)
                    self.adicionar_historico("Produto Vetorial", vetor1, vetor2, self.resultado)
                case "5": self.ver_historico()
                case _:
                print("Opção inválida.")
                continue

            self.vetor_resultado()

    def adicionar_historico(self, operacao, vetor1, vetor2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {vetor1.componentes} e {vetor2.componentes} => {resultado.componentes}")

    def vetor_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrar_vetor()

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class Vetor:
    def __init__(self, componentes):
        self.componentes = componentes

    def mostrar_vetor(self):
        print(f"Vetor: {self.componentes}")

    def adicionar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem somados.")
        resultado = [a + b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def subtrair(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem subtraídos.")
        resultado = [a - b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def produto_escalar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para o produto escalar.")
        return sum(a * b for a, b in zip(self.componentes, outro.componentes))

    def produto_vetorial(self, outro):
        if len(self.componentes) != 3 or len(outro.componentes) != 3:
            raise ValueError("O produto vetorial só é definido para vetores 3D.")
        x1, y1, z1 = self.componentes
        x2, y2, z2 = outro.componentes
        resultado = [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2,
        ]
        return Vetor(resultado)

    @staticmethod
    def criar_vetor(tamanho):
        componentes = []
        for i in range(tamanho):
            valor = float(input(f"Insira o valor do componente {i + 1}: "))
            componentes.append(valor)
        return Vetor(componentes)


class OperacoesMatrizes:
    def __init__(self):
        """Realiza operações com matrizes."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Multiplicação", "Transposição"]
        menu = Menu("Operações com Matrizes", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")

            tamanho = input("Digite o tamanho da matriz (ex: 2x2): ")
            valor_inicial = float(input("Digite o valor inicial: "))
            tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

            if tipo_progressao == 'PA':
                razao = float(input("Digite a razão da PA: "))
                matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
            elif tipo_progressao == 'PG':
                razao = float(input("Digite a razão da PG: "))
                matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
            else:
                print("Tipo de progressão inválido.")
                continue

            print("Matriz criada:")
            self.imprimir_matriz(matriz1)

            tamanho = input("Digite o tamanho da segunda matriz (ex: 2x2): ")
            valor_inicial = float(input("Digite o valor inicial da segunda matriz: "))
            tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

            if tipo_progressao == 'PA':
                razao = float(input("Digite a razão da PA: "))
                matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
            elif tipo_progressao == 'PG':
                razao = float(input("Digite a razão da PG: "))
                matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
            else:
                print("Tipo de progressão inválido.")
                continue

            print("Segunda matriz criada:")
            self.imprimir_matriz(matriz2)

            match opcao:
                case "0":
                    return
                case "1":
                    self.resultado = matriz1.adicionar(matriz2)
                    self.adicionar_historico("Adição", matriz1, matriz2, self.resultado)
                case "2":
                    self.resultado = matriz1.multiplicar(matriz2)
                    self.adicionar_historico("Multiplicação", matriz1, matriz2, self.resultado)
                case "3":
                    self.resultado = matriz1.transpor()
                    self.adicionar_historico("Transposição", matriz1, None, self.resultado)
                case "4": self.ver_historico()

            self.matrizes_resultado()

    def adicionar_historico(self, operacao, matriz1, matriz2, resultado):
        """Adiciona a operação ao histórico."""
        if matriz2 is not None:
            self.historico.append(f"{operacao}: {matriz1.matriz} e {matriz2.matriz} => {resultado.matriz}")
        else:
            self.historico.append(f"{operacao}: {matriz1.matriz} => {resultado.matriz}")

    def matrizes_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrarMatriz()

    def imprimir_matriz(self, matriz):
        for linha in matriz.matriz:
            print(f"[{', '.join(map(str, linha))}],")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class Matriz:
    def __init__(self, nLinhas, nColunas):
        self.nLinhas = nLinhas
        self.nColunas = nColunas
        self.matriz = [[0 for _ in range(nColunas)] for _ in range(nLinhas)]

    def addValores(self):
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                self.matriz[l][c] = float(input(f"Insira o valor para a Matriz em Linha: {l} e Coluna: {c}: "))

    def mostrarMatriz(self):
        saida = ""
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                numero = self.matriz[l][c]
                saida += f"{numero}\t"
            saida += "\n"
        print(f"\nSaida da Matriz {self.nLinhas}x{self.nColunas}:")
        print(saida)

    def transpor(self):
        transposta = Matriz(self.nColunas, self.nLinhas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                transposta.matriz[c][l] = self.matriz[l][c]
        return transposta

    def adicionar(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
        resultado = Matriz(self.nLinhas, self.nColunas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                resultado.matriz[l][c] = self.matriz[l][c] + outra.matriz[l][c]
        return resultado

    def multiplicar(self, outra):
        if self.nColunas != outra.nLinhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        resultado = Matriz(self.nLinhas, outra.nColunas)
        for i in range(self.nLinhas):
            for j in range(outra.nColunas):
                resultado.matriz[i][j] = sum(self.matriz[i][k] * outra.matriz[k][j] for k in range(self.nColunas))
        return resultado

    def igual(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            return False
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                if self.matriz[l][c] != outra.matriz[l][c]:
                    return False
        return True

    @staticmethod
    def criar_matriz(tamanho, valor_inicial, progressao, razao=1):
        linhas, colunas = map(int, tamanho.split('x'))
        matriz = Matriz(linhas, colunas)
        valor_atual = valor_inicial

        if progressao == 'PA':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual += razao

        elif progressao == 'PG':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual *= razao

        return matriz
        
class Geometria:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Calcular Área do Círculo",
            "Calcular Área do Retângulo",
            "Calcular Perímetro do Triângulo",
            "Calcular Volume do Cubo"
        ]
        menu = Menu("Geometria", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "0":
                    return
                case "1": 
                    raio = float(input("Digite o raio do círculo: "))
                    area = self.calcular_area_circulo(raio)
                    print(f"Área do Círculo: {area}")
                    self.adicionar_historico("Área do Círculo", {"raio": raio}, area)
                case "2": 
                    largura = float(input("Digite a largura do retângulo: "))
                    altura = float(input("Digite a altura do retângulo: "))
                    area = self.calcular_area_retangulo(largura, altura)
                    print(f"Área do Retângulo: {area}")
                    self.adicionar_historico("Área do Retângulo", {"largura": largura, "altura": altura}, area)
                case "3":
                    a = float(input("Digite o comprimento do lado A: "))
                    b = float(input("Digite o comprimento do lado B: "))
                    c = float(input("Digite o comprimento do lado C: "))
                    perimetro = self.calcular_perimetro_triangulo(a, b, c)
                    print(f"Perímetro do Triângulo: {perimetro}")
                    self.adicionar_historico("Perímetro do Triângulo", {"a": a, "b": b, "c": c}, perimetro)
                case "4": 
                    lado = float(input("Digite o comprimento do lado do cubo: "))
                    volume = self.calcular_volume_cubo(lado)
                    print(f"Volume do Cubo: {volume}")
                    self.adicionar_historico("Volume do Cubo", {"lado": lado}, volume)
                case "5": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, parametros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {parametros} => {resultado}")

    def calcular_area_circulo(self, raio):
        """Calcula a área de um círculo dado o raio."""
        return 3.14 * raio ** 2

    def calcular_area_retangulo(self, largura, altura):
        """Calcula a área de um retângulo dado a largura e a altura."""
        return largura * altura

    def calcular_perimetro_triangulo(self, a, b, c):
        """Calcula o perímetro de um triângulo dado os comprimentos dos lados."""
        return a + b + c

    def calcular_volume_cubo(self, lado):
        """Calcula o volume de um cubo dado o comprimento do lado."""
        return lado ** 3

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class Teoremas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Teorema de Pitágoras",
            "Teorema de Tales"
        ]
        menu = Menu("Teoremas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha um teorema: ")
            match func:
                case "0":
                    return
                case "1":
                    a = float(input("Digite o comprimento do lado A: "))
                    b = float(input("Digite o comprimento do lado B: "))
                    hipotenusa = self.teorema_pitagoras(a, b)
                    print(f"Comprimento da hipotenusa: {hipotenusa}")
                    self.adicionar_historico("Teorema de Pitágoras", {"a": a, "b": b}, hipotenusa)
                case "2":
                    # Exemplo simples do Teorema de Tales
                    a = float(input("Digite o comprimento do segmento A: "))
                    b = float(input("Digite o comprimento do segmento B: "))
                    c = float(input("Digite o comprimento do segmento C: "))
                    proporcao = self.teorema_tales(a, b, c)
                    print(f"Proporção: {proporcao}")
                    self.adicionar_historico("Teorema de Tales", {"a": a, "b": b, "c": c}, proporcao)
                case "3": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, teorema, parametros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{teorema}: {parametros} => {resultado}")

    def teorema_pitagoras(self, a, b):
        """Calcula a hipotenusa de um triângulo retângulo."""
        return (a**2 + b**2) ** 0.5

    def teorema_tales(self, a, b, c):
        """Calcula a proporção do Teorema de Tales."""
        return (a / b) * c

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class NumeroComplexo:
    def __init__(self):
        r1 = float(input("Parte real do primeiro número complexo: "))
        i1 = float(input("Parte imaginária do primeiro número complexo: "))
        r2 = float(input("Parte real do segundo número complexo: "))
        i2 = float(input("Parte imaginária do segundo número complexo: "))

        self.z1 = NumeroComplexoIndividual(r1, i1)
        self.z2 = NumeroComplexoIndividual(r2, i2)
        self.historico = []  # Lista para armazenar o histórico

        menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Módulo do primeiro número"]
        menu = Menu("Número Complexo", menu_opcoes)
        while True:
            menu.desenhar()
            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.z1.soma(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Soma", self.z1, self.z2, resultado)
                case "2":
                    resultado = self.z1.subtracao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Subtração", self.z1, self.z2, resultado)
                case "3":
                    resultado = self.z1.multiplicacao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Multiplicação", self.z1, self.z2, resultado)
                case "4":
                    resultado = self.z1.divisao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Divisão", self.z1, self.z2, resultado)
                case "5":
                    print(f"Módulo: {self.z1.modulo()}")
                case "6": self.ver_historico()
                case _:
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, z1, z2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {z1.exibir()} e {z2.exibir()} => {resultado.exibir()}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class NumeroComplexoIndividual:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def exibir(self):
        sinal = '+' if self.imaginario >= 0 else '-'
        return f"{self.real} {sinal} {abs(self.imaginario)}i"

    def soma(self, outro):
        real = self.real + outro.real
        imaginario = self.imaginario + outro.imaginario
        return NumeroComplexoIndividual(real, imaginario)

    def subtracao(self, outro):
        real = self.real - outro.real
        imaginario = self.imaginario - outro.imaginario
        return NumeroComplexoIndividual(real, imaginario)

    def multiplicacao(self, outro):
        real = self.real * outro.real - self.imaginario * outro.imaginario
        imaginario = self.real * outro.imaginario + self.imaginario * outro.real
        return NumeroComplexoIndividual(real, imaginario)

    def divisao(self, outro):
        denominador = outro.real ** 2 + outro.imaginario ** 2
        real = (self.real * outro.real + self.imaginario * outro.imaginario) / denominador
        imaginario = (self.imaginario * outro.real - self.real * outro.imaginario) / denominador
        return NumeroComplexoIndividual(real, imaginario)

    def modulo(self):
        return (self.real ** 2 + self.imaginario ** 2) ** 0.5


class Fracao:
    def __init__(self):
        n1 = int(input("Numerador da primeira fração: "))
        d1 = int(input("Denominador da primeira fração: "))
        n2 = int(input("Numerador da segunda fração: "))
        d2 = int(input("Denominador da segunda fração: "))

        self.f1 = FracaoIndividual(n1, d1)
        self.f2 = FracaoIndividual(n2, d2)
        self.historico = []  # Lista para armazenar o histórico

        menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
        menu = Menu("Fração", menu_opcoes)
        while True:
            menu.desenhar()
            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.f1.soma(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Soma", self.f1, self.f2, resultado)
                case "2":
                    resultado = self.f1.subtracao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Subtração", self.f1, self.f2, resultado)
                case "3":
                    resultado = self.f1.multiplicacao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Multiplicação", self.f1, self.f2, resultado)
                case "4":
                    resultado = self.f1.divisao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Divisão", self.f1, self.f2, resultado)
                case "5": self.ver_historico()
                case _:
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, f1, f2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {f1.exibir()} e {f2.exibir()} => {resultado.exibir()}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class FracaoIndividual:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError("Denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador

    def exibir(self):
        return f"{self.numerador}/{self.denominador}"

    def soma(self, outra):
        novo_numerador = self.numerador * outra.denominador + self.denominador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def subtracao(self, outra):
        novo_numerador = self.numerador * outra.denominador - self.denominador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def multiplicacao(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def divisao(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def simplificar(self):
        def calcular_mdc(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        mdc = calcular_mdc(self.numerador, self.denominador)
        return FracaoIndividual(self.numerador // mdc, self.denominador // mdc)

class VerifNums(Base):
    def __init__(self):
        """Menu de opções para verificar propriedades de um número: paridade, primo, palíndromo, Fibonacci, etc."""
        self.historico = []  # Inicializa o histórico
        menu_opcoes = [
            "Positivo, Negativo, Zero", "Primo", "Par, Ímpar", "Palíndromo", 
            "Fibonacci", "Perfeito", "Amigável", "Cálculo de MDC e MMC", 
            "Listar Fibonacci até N", "Listar Números Perfeitos até N", 
            "Contar Dígitos de um Número", "Listar Números Primos até N", 
            "Mágico", "Triangular", "Catalan", "Quadrado Perfeito", 
            "Cubo Perfeito", "Número Abundante/Deficiente", "Número de Harshad",
            "Mostrar Histórico"  # Opção para mostrar o histórico
        ]
        menu = Menu("Verificar Número", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            try:
                if opcao == "0": return
                elif opcao in ["1", "2", "3", "4", "5", "6", "11", "13", "14", "15", "16", "17", "18", "19"]:
                    num = int(input("Digite o número: "))
                    resultado = ""
                    match opcao:
                        case "1": resultado = f"{num} é positivo." if num > 0 else f"{num} é negativo." if num < 0 else "Zero."
                        case "2": resultado = f"{num} é primo." if self.eh_primo(num) else f"{num} não é primo."
                        case "3": resultado = f"{num} é par." if num % 2 == 0 else f"{num} é ímpar."
                        case "4": resultado = f"{num} é palíndromo." if str(num) == str(num)[::-1] else f"{num} não é palíndromo."
                        case "5": resultado = f"{num} pertence à sequência de Fibonacci." if self.eh_fibonacci(num) else f"{num} não pertence."
                        case "6": resultado = f"{num} é um número perfeito." if self.eh_perfeito(num) else f"{num} não é perfeito."
                        case "11": resultado = f"Número de dígitos no número '{num}': {self.contar_digitos(num)}"
                        case "13": resultado = f"{num} é um número mágico" if self.eh_numero_magico(num) else f"{num} não é mágico"
                        case "14": resultado = f"{num} é um número triangular" if self.eh_numero_triangulo(num) else f"{num} não é triangular"
                        case "15": resultado = f"{num} é um número de Catalan" if self.eh_numero_catalan(num) else f"{num} não é um número de Catalan."
                        case "16": resultado = f"{num} é um quadrado perfeito." if self.eh_quadrado_perfeito(num) else f"{num} não é um quadrado perfeito."
                        case "17": resultado = f"{num} é um cubo perfeito." if self.eh_cubo_perfeito(num) else f"{num} não é um cubo perfeito."
                        case "18": resultado = f"{num} é um número {self.classificar_numero(num)}."
                        case "19": resultado = f"{num} é um número de Harshad." if self.eh_harshad(num) else f"{num} não é um número de Harshad."
                    
                    # Armazenar resultado no histórico
                    self.historico.append(f"{resultado} (Número: {num})")
                    print(resultado)

                elif opcao in ["9", "10", "12"]:
                    match opcao:
                        case "9": self.listar_fibonacci()
                        case "10": self.listar_numeros_perfeitos()
                        case "12": self.listar_primos_intervalo()
                else:
                    match opcao:
                        case "7":
                            a = int(input("Insira um número: "))
                            b = int(input("Insira um número: "))
                            resultado = f"{a} e {b} são números amigáveis." if self.eh_amigavel(a, b) else f"{a} e {b} não são amigáveis."
                            self.historico.append(resultado)
                            print(resultado)
                        case "8": self.calcular_mdc_mmc()
                        case "20": self.mostrar_historico()  # Adiciona opção para mostrar histórico
                        case _: print("Opção inválida.")
            except ValueError as e:
                print("Erro: Entrada inválida. Por favor, insira números inteiros.")

    def mostrar_historico(self):
        """Mostra o histórico das operações realizadas."""
        print("\nHistórico de Operações:")
        for entrada in self.historico:
            print(f"- {entrada}")
        print()  # Linha em branco para melhor separação

    def eh_primo(self, num):
        """Verifica se um número é primo."""
        if num <= 1:
            return False
        for i in range(2, int(self.raiz_quadrada(num)) + 1):
            if num % i == 0:
                return False
        return True

    def eh_fibonacci(self, num):
        """Verifica se um número pertence à sequência de Fibonacci."""
        def eh_quadrado_perfeito(x):
            s = int(self.raiz_quadrada(x))
            return s * s == x
        return eh_quadrado_perfeito(5 * num * num + 4) or eh_quadrado_perfeito(5 * num * num - 4)

    def eh_perfeito(self, n):
        """Verifica se um número é perfeito."""
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return soma_divisores == n
        
    def eh_amigavel(self, a, b):
        """Verifica se dois números são amigáveis."""
        soma_a = sum(i for i in range(1, a) if a % i == 0)
        soma_b = sum(i for i in range(1, b) if b % i == 0)
        return soma_a == b and soma_b == a

    def calcular_mdc_mmc(self):
        """Permite o cálculo de MDC e MMC de uma lista de números fornecida pelo usuário."""
        try:
            print("\n|============================|")
            print("|    Cálculo de MDC e MMC    |")
            print("|============================|")
            numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
            
            if len(numeros) < 2:
                print("Erro: Insira pelo menos dois números.")
                return
            
            mdc = self.calcular_mdc_lista(numeros)
            mmc = self.calcular_mmc_lista(numeros)
            
            resultado = f"MDC dos números {numeros}: {mdc}\nMMC dos números {numeros}: {mmc}"
            self.historico.append(resultado)  # Armazenar no histórico
            print(resultado)
        except ValueError:
            print("Erro: Certifique-se de digitar apenas números inteiros separados por espaço.")

    def calcular_mdc_lista(self, numeros):
        """Calcula o MDC de uma lista de números."""
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        resultado = numeros[0]
        for num in numeros[1:]:
            resultado = mdc(resultado, num)
        return resultado

    def calcular_mmc_lista(self, numeros):
        """Calcula o MMC de uma lista de números."""
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        def mmc(a, b):
            return abs(a * b) // mdc(a, b)

        resultado = numeros[0]
        for num in numeros[1:]:
            resultado = mmc(resultado, num)
        return resultado
        
    def contar_digitos(self, num):
        """Conta o número de dígitos em um número."""
        return len(str(abs(num)))

    def listar_fibonacci(self):
        """Lista os números de Fibonacci até um número N fornecido pelo usuário."""
        n = int(input("Até qual número deseja listar os Fibonacci? "))
        fib = [0, 1]
        while fib[-1] + fib[-2] <= n:
            fib.append(fib[-1] + fib[-2])
        print(f"Números de Fibonacci até {n}: {fib}")
        self.historico.append(f"Fibonacci até {n}: {fib}")  # Armazenar no histórico

    def listar_numeros_perfeitos(self):
        """Lista os números perfeitos até um número N fornecido pelo usuário."""
        n = int(input("Até qual número deseja listar os números perfeitos? "))
        perfeitos = []
        for i in range(1, n + 1):
            if self.eh_perfeito(i):
                perfeitos.append(i)
        print(f"Números perfeitos até {n}: {perfeitos}")
        self.historico.append(f"Números perfeitos até {n}: {perfeitos}")  # Armazenar no histórico

    def listar_primos_intervalo(self):
        """Lista os números primos em um intervalo fornecido pelo usuário."""
        inicio = int(input("Digite o início do intervalo: "))
        fim = int(input("Digite o fim do intervalo: "))
        primos = [num for num in range(inicio, fim + 1) if self.eh_primo(num)]
        print(f"Números primos entre {inicio} e {fim}: {primos}")
        self.historico.append(f"Números primos entre {inicio} e {fim}: {primos}")  # Armazenar no histórico

    def eh_numero_magico(self, num):
        """Verifica se um número é mágico."""
        while num >= 10:
            num = sum(int(d) for d in str(num))
        return num == 1

    def eh_numero_triangulo(self, num):
        """Verifica se um número é triangular."""
        n = int(((-1 + (1 + 8 * num) ** 0.5) / 2))
        return n * (n + 1) // 2 == num

    def eh_numero_catalan(self, num):
        """Verifica se um número é um número de Catalan."""
        n = 0
        catalan = 1
        while catalan < num:
            n += 1
            catalan = (2 * (2 * n + 1) * catalan) // (n + 2)
        return catalan == num

    def eh_quadrado_perfeito(self, num):
        """Verifica se um número é um quadrado perfeito."""
        raiz = int(num ** 0.5)
        return raiz * raiz == num

    def eh_cubo_perfeito(self, num):
        """Verifica se um número é um cubo perfeito."""
        raiz = int(num ** (1/3))
        return raiz * raiz * raiz == num

    def classificar_numero(self, n):
        """Classifica um número como perfeito, abundante ou deficiente."""
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        if soma_divisores == n:
            return "Perfeito"
        elif soma_divisores > n:
            return "Abundante"
        else:
            return "Deficiente"

    def eh_harshad(self, num):
        """Verifica se um número é um número de Harshad."""
        soma_digitos = sum(int(d) for d in str(num))
        return num % soma_digitos == 0
        
# --- CONVERSORES ---
class ConvUni(Base):
    def __init__(self):
        self.historico = []  # Para armazenar o histórico de conversões
        self.unidades = {
            "comprimento": {
                "1": ("Quilômetros", 1000),
                "2": ("Metros", 1),
                "3": ("Centímetros", 0.01),
                "4": ("Milhas", 1609.34),
                "5": ("Pés", 0.3048),
                "6": ("Polegadas", 0.0254),
            },
            "área": {
                "1": ("Metro Quadrado", 1),
                "2": ("Hectare", 10000),
                "3": ("Acre", 4046.86),
                "4": ("Kilômetro Quadrado", 1000000),
                "5": ("Centímetro Quadrado", 0.0001),
                "6": ("Milha Quadrada", 2589988.11),
            },
            "volume": {
                "1": ("Metro Cúbico", 1),
                "2": ("Litro", 0.001),
                "3": ("Mililitro", 0.000001),
                "4": ("Centímetro Cúbico", 0.000001),
                "5": ("Kilômetro Cúbico", 1000000000),
                "6": ("Hectômetro Cúbico", 1000000),
            },
            "tempo": {
                "1": ("Segundos", 1),
                "2": ("Minutos", 60),
                "3": ("Horas", 3600),
                "4": ("Dias", 86400),
                "5": ("Anos", 31557600),
            },
            "velocidade": {
                "1": ("m/s", 1),
                "2": ("km/h", 3.6),
            },
            "moeda": {
                "USD": 1.0,
                "BRL": 5.25,
                "EUR": 0.85,
            },
            "temperatura": {
                "1": {
                    "nome": "Celsius",
                    "simbolo": "C",
                    "conversao": {
                        "F": lambda c: c * 9 / 5 + 32,  # Para Fahrenheit
                        "K": lambda c: c + 273.15,     # Para Kelvin
                        "R": lambda c: (c + 273.15) * 9 / 5,  # Para Rankine
                    },
                },
                "2": {
                    "nome": "Fahrenheit",
                    "simbolo": "F",
                    "conversao": {
                        "C": lambda f: (f - 32) * 5 / 9,           # Para Celsius
                        "K": lambda f: (f - 32) * 5 / 9 + 273.15,  # Para Kelvin
                        "R": lambda f: f + 459.67,                 # Para Rankine
                    },
                },
                "3": {
                    "nome": "Kelvin",
                    "simbolo": "K",
                    "conversao": {
                        "C": lambda k: k - 273.15,                 # Para Celsius
                        "F": lambda k: (k - 273.15) * 9 / 5 + 32,  # Para Fahrenheit
                        "R": lambda k: k * 9 / 5,                  # Para Rankine
                    },
                },
                "4": {
                    "nome": "Rankine",
                    "simbolo": "R",
                    "conversao": {
                        "C": lambda r: (r - 491.67) * 5 / 9,       # Para Celsius
                        "F": lambda r: r - 459.67,                 # Para Fahrenheit
                        "K": lambda r: r * 5 / 9,                  # Para Kelvin
                    },
                },
            },
            "pressao": {
                "1": ("Pascal", 1),
                "2": ("Bar", 100000),
                "3": ("Atmosfera", 101325),
                "4": ("Milímetro de Mercúrio", 133.322),
                "5": ("Torr", 133.322),
                "6": ("PSI", 6894.76),
                "7": ("Kilopascal", 1000),
            },
            "massa": {
                "1": ("Quilograma", 1),
                "2": ("Grama", 0.001),
                "3": ("Miligrama", 0.000001),
                "4": ("Libra", 0.453592),
                "5": ("Onça", 0.0283495),
                "6": ("Tonelada", 1000),
                "7": ("Micrograma", 1e-6),  # Adicionando microgramas
                "8": ("Tonelada métrica", 1000),  # Adicionando toneladas métricas
            },
            "energia": {
                "1": ("Joule", 1),
                "2": ("Kilojoule", 1000),
                "3": ("Caloria", 4.184),
                "4": ("Kilocaloria", 4184),
                "5": ("Watt-hora", 3600),
                "6": ("Joules por segundo (Watts)", 1),  # Adicionando Watts
                "7": ("Calorias por segundo", 4.184),  # Adicionando calorias por segundo
                "8": ("Kilowatt-hora", 3600000),
                "9": ("BTU", 1055.06),
                "10": ("Erg", 1e-7),
            },
            "dados": {
                "1": ("Byte", 1),
                "2": ("Kilobyte", 1024),
                "3": ("Megabyte", 1024**2),
                "4": ("Gigabyte", 1024**3),
                "5": ("Terabyte", 1024**4),
                "6": ("Bit", 1/8),
                "7": ("Kilobit", 1024 / 8),
                "8": ("Megabit", (1024**2) / 8),
                "9": ("Gigabit", (1024**3) / 8),
                "10": ("Terabit", (1024**4) / 8),
            },
            "forca": {
                "1": ("Newton", 1),
                "2": ("Libra-força", 4.44822),
                "3": ("Dina", 1e-5),
            },
            "angulo": {
                "1": ("Grau", 1),
                "2": ("Minuto de Arco", 1/60),
                "3": ("Segundo de Arco", 1/3600),
                "4": ("Radianos", 57.2958),
            },
            "densidade": {
                "1": ("Quilograma por metro cúbico", 1),
                "2": ("Grama por centímetro cúbico", 1000),
                "3": ("Libra por pé cúbico", 16.0185),
            },
            "frequencia": {
                "1": ("Hertz", 1),
                "2": ("Kilohertz", 1000),
                "3": ("Megahertz", 1_000_000),
                "4": ("Gigahertz", 1_000_000_000),
            },
            "iluminancia": {
                "1": ("Lux", 1),
                "2": ("Foot-candle", 10.764),
            },
            "luminancia": {
                "1": ("Candela por metro quadrado", 1),
                "2": ("Foot-lambert", 3.426),
                "3": ("Nit", 1),
            },
            "potencia": {
                "1": ("Watt", 1),
                "2": ("Cavalo-vapor", 745.7),
                "3": ("BTU/h", 0.293071),
            },
            "eletricidade": {
                "1": ("Ampere", 1),
                "2": ("Volt", 1),
                "3": ("Ohm", 1),
                "4": ("Farad", 1),
                "5": ("Coulomb", 1),
                "6": ("Watt-hora", 3600),
                "7": ("Quilowatt-hora", 3600000),
            },
            "radioatividade": {
                "1": ("Becquerel", 1),
                "2": ("Curie", 3.7e10),
                "3": ("Gray", 1),
                "4": ("Sievert", 1),
            },
            "velocidade_angular": {
                "1": ("Radianos por segundo", 1),
                "2": ("RPM", 2 * 3.14159 / 60),
            },
            "fluxo_massa": {
                "1": ("Quilograma por segundo", 1),
                "2": ("Libra por segundo", 0.453592),
            },
        }
        
        menu_opcoes = ["Conversão de Unidades", "Conversão de Moeda", "Adicionar Unidade Personalizada", "Mostrar Histórico"]
        menu = Menu("Conversores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.conversores_unidades()
                case "2": self.conversao_moeda()
                case "3": self.adicionar_unidade_personalizada()
                case "4": self.mostrar_historico()
                case "0": break
                case _: print("Opção inválida. Tente novamente.")

    def adicionar_unidade_personalizada(self):
        tipo = input("Digite o tipo da unidade (ex: massa, energia): ")
        nome = input("Digite o nome da nova unidade: ")
        fator = float(self.obter_input_float("Digite o fator de conversão para a unidade base: "))
        
        if tipo in self.unidades:
            novo_id = str(len(self.unidades[tipo]) + 1)
            self.unidades[tipo][novo_id] = (nome, fator)
            print("Unidade adicionada com sucesso!")
        else:
            print("Tipo de unidade inválido.")

    def obter_input_float(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                
    def mostrar_historico(self):
        print("Histórico de Conversões:")
        for entrada in self.historico:
            valor, unidade, conversoes = entrada
            print(f"{valor} {unidade} convertido para:")
            for conv in conversoes:
                print(f"  - {conv[0]} {conv[1]}")

    def conversores_unidades(self):
        while True:
            menu_opcoes=["Comprimento","Área","Volume","Tempo","Velocidade","Temperatura","Pressão","Massa",
                         "Energia","Dados","Força","Ângulo","Densidade","Frequência","Iluminância","Luminância",
                         "Potência","Eletricidade","Radioatividade","Velocidade Angular","Fluxo de Massa",]
            menu = Menu("Conversores", menu_opcoes)
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.converter("comprimento")
                case "2": self.converter("área")
                case "3": self.converter("volume")
                case "4": self.converter("tempo")
                case "5": self.converter("velocidade")
                case "6": self.converter_temperatura()
                case "7": self.converter("pressao")
                case "8": self.converter("massa")
                case "9": self.converter("energia")
                case "10": self.converter("dados")
                case "11": self.converter("forca")
                case "12": self.converter("angulo")
                case "13": self.converter("densidade")
                case "14": self.converter("frequencia")
                case "15": self.converter("iluminancia")
                case "16": self.converter("luminancia")
                case "17": self.converter("potencia")
                case "18": self.converter("eletricidade")
                case "19": self.converter("radioatividade")
                case "20": self.converter("velocidade_angular")
                case "21": self.converter("fluxo_massa")
                case "0": break
                case _: print("Opção inválida. Tente novamente.")

    def converter(self, tipo):
        unidades = self.unidades[tipo]
        print(f"|============================|")
        print(f"| Escolha uma unidade de {tipo} |")
        for key, (nome, _) in unidades.items():
            print(f"|{key}. {nome:<24}|")
        print("|0. Sair                     |")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem == "0":
            self.conversores_unidades()
            return
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = self.obter_input_float(f"Digite o valor em {unidades[unidade_origem][0]}: ")
        
        # Converte para a unidade base e calcula para todas as unidades
        valor_em_base = valor * unidades[unidade_origem][1]
        self.historico.append((valor, unidades[unidade_origem][0], []))  # Adiciona ao histórico

        print(f"\nConversão de {valor} {unidades[unidade_origem][0]} para todas as unidades disponíveis:")
        for key, (nome, fator) in unidades.items():
            valor_convertido = valor_em_base / fator
            self.historico[-1][2].append((valor_convertido, nome))  # Armazena a conversão
            print(f"{valor_convertido} {nome}")

    def converter_temperatura(self):
        unidades = self.unidades["temperatura"]
        print(f"|============================|")
        print(f"| Escolha uma unidade de temperatura |")
        for key, unidade in unidades.items():
            print(f"|{key}. {unidade['nome']:<24}|")
        print("|0. Sair                     |")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem == "0":
            return
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = self.obter_input_float(f"Digite o valor em {unidades[unidade_origem]['nome']}: ")
        
        print(f"\nConversão de {valor} {unidades[unidade_origem]['simbolo']} para todas as unidades disponíveis:")
        for key, unidade_destino in unidades.items():
            if key == unidade_origem:
                continue  # Pula a unidade de origem
            # Realiza a conversão utilizando a função correspondente
            conversao_func = unidades[unidade_origem]["conversao"][unidade_destino["simbolo"]]
            valor_convertido = conversao_func(valor)
            print(f"{valor_convertido:.2f} {unidade_destino['nome']} ({unidade_destino['simbolo']})")

    def conversao_moeda(self):
        valor = self.obter_input_float("Digite o valor em moeda: ")
        origem = input("Moeda de origem (USD, BRL, EUR): ")
        destino = input("Moeda de destino (USD, BRL, EUR): ")
        if origem in self.unidades["moeda"] and destino in self.unidades["moeda"]:
            valor_convertido = valor * (self.unidades["moeda"][destino] / self.unidades["moeda"][origem])
            print(f"Resultado: {valor} {origem} = {valor_convertido:.2f} {destino}")
        else:
            print("Erro: Moeda inválida.")
            
class UttsTexto:
    def __init__(self):
        menu_opcoes=["Analise de Texto"]
        menu = Menu("Utilitários de Texto", menu_opcoes)
        menu.desenhar()
        escolha = input("Escolha uma opção: ")
        match escolha:
            case "0": return
            case "1": AnaliseTexto()
            case _: print("Opção inválida. Por favor, escolha novamente.")

# --- ANÁLISE DE TEXTO ---
class AnaliseTexto:
    def __init__(self):
        """Contagem de palavras e caracteres no texto, e frequência de palavras e caracteres."""
        texto = input("Digite o texto para análise: ")
        palavras = texto.split()

        contador_palavras = Counter(palavras)
        contador_caracteres = Counter(texto)
        print(f"Número total de palavras: {len(palavras)}")
        print("Frequência de palavras:", dict(contador_palavras))
        print("Frequência de caracteres:", dict(contador_caracteres))
        
class Financas:
    def __init__(self):
        menu_opcoes=["Calculadora Financeira","Simulador Financeiro"]
        menu = Menu("Financas", menu_opcoes)
        menu.desenhar()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "0": return
            case "1": CalculadoraFinanceira()
            case "2": SimuladorFinanceiro()
            case _: print("Opção inválida. Tente novamente.")

class CalculadoraFinanceira:
    def __init__(self):
        menu_opcoes=["Calcular ROI","Calcular Margem de Lucro"]
        menu = Menu("Calculadora Financeira", menu_opcoes)
        menu.desenhar()
        func = input("Escolha uma função: ")
        match func:
            case "1":
                investimento = float(input("Digite o investimento inicial: "))
                retorno = float(input("Digite o retorno total: "))
                print(f"ROI: {self.calcular_roi(investimento, retorno)}%")
            case "2":
                receita = float(input("Digite a receita total: "))
                custo = float(input("Digite o custo total: "))
                print(f"Margem de Lucro: {self.calcular_margem_lucro(receita, custo)}%")
            case _: 
                print("Opção inválida.")

    def calcular_roi(self, investimento, retorno):
        """Calcula o Retorno sobre Investimento (ROI)."""
        return ((retorno - investimento) / investimento) * 100

    def calcular_margem_lucro(self, receita, custo):
        """Calcula a margem de lucro."""
        return ((receita - custo) / receita) * 100 if receita else 0

class SimuladorFinanceiro:
    def __init__(self):
        menu_opcoes = ["Calcular Juros Compostos","Calcular Investimento Futuro","Calcular Valor Presente"]
        menu = Menu("Simulador Financeiro", menu_opcoes)
        menu.desenhar()
        func = input("Escolha uma função: ")
        match func:
            case "1":
                capital = float(input("Digite o capital inicial: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Juros Compostos: {self.calcular_juros_compostos(capital, taxa, tempo)}")
            case "2":
                capital = float(input("Digite o capital inicial: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Investimento Futuro: {self.calcular_investimento_futuro(capital, taxa, tempo)}")
            case "3":
                montante = float(input("Digite o montante: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Valor Presente: {self.calcular_valor_presente(montante, taxa, tempo)}")
            case _: 
                print("Opção inválida.")

    def calcular_juros_compostos(self, capital, taxa, tempo):
        """Calcula o montante total com juros compostos."""
        return capital * (1 + taxa) ** tempo

    def calcular_investimento_futuro(self, capital, taxa, tempo):
        """Calcula o valor futuro do investimento."""
        return self.calcular_juros_compostos(capital, taxa, tempo)

    def calcular_valor_presente(self, montante, taxa, tempo):
        """Calcula o valor presente dado um montante futuro."""
        return montante / ((1 + taxa) ** tempo)
        
# --- JOGOS ---
class Jogos:
    def quiz_matematico(self):
        print("Escolha a dificuldade: ")
        dificuldade = input("1. Fácil (1-10)\n2. Médio (1-50)\n3. Difícil (1-100): ")
        intervalo = {"1": 10, "2": 50, "3": 100}.get(dificuldade, 10)
        operacao = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").lower()
        pontos = 0

        for _ in range(5):
            num1 = random.randint(1, intervalo)
            num2 = random.randint(1, intervalo)
            if operacao == "soma":
                resposta_correta = num1 + num2
                simbolo = "+"
            elif operacao == "subtracao":
                resposta_correta = num1 - num2
                simbolo = "-"
            elif operacao == "multiplicacao":
                resposta_correta = num1 * num2
                simbolo = "*"
            elif operacao == "divisao" and num2 != 0:
                resposta_correta = num1 // num2
                simbolo = "/"
            else:
                print("Operação inválida.")
                return

            resposta_usuario = int(input(f"Quanto é {num1} {simbolo} {num2}? "))
            if resposta_usuario == resposta_correta:
                print("Correto!")
                pontos += 1
            else:
                print(f"Incorreto. A resposta correta é {resposta_correta}.")
        print(f"Pontuação final: {pontos}/5")

    def sudoku_basico(self):
        self.tabuleiro = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        while True:
            self.print_tabuleiro()
            try:
                x = int(input("Linha (0-8) ou -1 para sair: "))
                if x == -1:
                    break
                y = int(input("Coluna (0-8): "))
                valor = int(input("Valor (1-9): "))

                if self.eh_valido(x, y, valor):
                    self.tabuleiro[x][y] = valor
                    print("Valor inserido!")
                else:
                    print("Movimento inválido!")
            except (ValueError, IndexError):
                print("Entrada inválida! Tente novamente.")
            
    def print_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(str(x) if x != 0 else "." for x in linha))
        print()  # Linha em branco para separação

    def eh_valido(self, x, y, valor):
        # Verifica linha e coluna
        for i in range(9):
            if self.tabuleiro[x][i] == valor or self.tabuleiro[i][y] == valor:
                return False
        
        # Verifica o quadrante 3x3
        quad_x = (x // 3) * 3
        quad_y = (y // 3) * 3
        for i in range(quad_x, quad_x + 3):
            for j in range(quad_y, quad_y + 3):
                if self.tabuleiro[i][j] == valor:
                    return False
        
        return True

    def __init__(self):
        menu_opcoes=["Quiz","Sudoku",]
        menu = Menu("Jogos", menu_opcoes)
        menu.desenhar()
        opcao = input("Escolha uma função: ")
        match opcao:
            case "1": self.quiz_matematico()
            case "2": self.sudoku_basico()
            case _: print("Opção inválida.")

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

    def menu_jogo_da_velha(self):
        print("\n|=============================|")
        print("|1. Iniciar Jogo              |")
        print("|0. Voltar                    |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            self.iniciar_jogo()
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def iniciar_jogo(self):
        for _ in range(9):
            self.imprimir_tabuleiro()
            linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0-2): "))
            if self.fazer_jogada(linha, coluna):
                if self.verificar_vencedor():
                    self.imprimir_tabuleiro()
                    print(f"Jogador {self.jogador_atual} venceu!")
                    return
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        self.imprimir_tabuleiro()
        print("Empate!")

    def fazer_jogada(self, linha, coluna):
        """Faz a jogada do jogador atual."""
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        else:
            print("Casa já ocupada! Tente novamente.")
            return False

    def verificar_vencedor(self):
        """Verifica se houve um vencedor."""
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return True
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro do jogo da velha."""
        for linha in self.tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)

class SudokuSolver:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def menu_sudoku(self):
        print("\n|============================|")
        print("|1. Resolver Sudoku           |")
        print("|0. Voltar                   |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            if self.resolver():
                print("Sudoku resolvido:")
                self.imprimir_tabuleiro()
            else:
                print("Não foi possível resolver o Sudoku.")
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def resolver(self):
        """Resolve o Sudoku usando backtracking."""
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:  # Encontrar uma célula vazia
                    for num in range(1, 10):
                        if self.eh_valido(i, j, num):
                            self.tabuleiro[i][j] = num
                            if self.resolver():
                                return True
                            self.tabuleiro[i][j] = 0  # Backtrack
                    return False
        return True

    def eh_valido(self, linha, coluna, num):
        """Verifica se um número pode ser colocado na célula."""
        for x in range(9):
            if self.tabuleiro[linha][x] == num or self.tabuleiro[x][coluna] == num:
                return False
        # Verificar a subgrade 3x3
        start_row, start_col = 3 * (linha // 3), 3 * (coluna // 3)
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[start_row + i][start_col + j] == num:
                    return False
        return True

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro de Sudoku."""
        for linha in self.tabuleiro:
            print(" ".join(str(num) for num in linha))
