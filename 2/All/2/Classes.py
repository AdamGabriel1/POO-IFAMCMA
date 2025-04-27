from abc import ABC, abstractmethod
from math import pi

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
