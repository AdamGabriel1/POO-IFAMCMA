class Celular:
    def __init__(self, modelo, marca, sistema_operacional, disponibilidade, dimensoes, peso, resistencia_agua, processador, chipset, memoria_ram, gpu, armazenamento, memoria_expansivel, bateria_tipo, bateria_capacidade, tipo_tela, tamanho_tela, resolucao_tela, densidade_pixels, fps_tela, protecao_tela, camera_megapixels, camera_resolucao, camera_aperture, camera_estabilizacao, camera_autofoco, camera_flash, camera_hdr, camera_localizacao, camera_detecao_facial, camera_frontal, video_resolucao, video_auto_foco, video_fps, video_estabilizacao, video_slow_motion, video_foto_em_video, video_camera_frontal):
        self.modelo = modelo
        self.marca = marca
        self.sistema_operacional = sistema_operacional
        self.disponibilidade = disponibilidade
        self.dimensoes = dimensoes
        self.peso = peso
        self.resistencia_agua = resistencia_agua
        self.processador = processador
        self.chipset = chipset
        self.memoria_ram = memoria_ram
        self.gpu = gpu
        self.armazenamento = armazenamento
        self.memoria_expansivel = memoria_expansivel
        self.bateria_tipo = bateria_tipo
        self.bateria_capacidade = bateria_capacidade
        self.tipo_tela = tipo_tela
        self.tamanho_tela = tamanho_tela
        self.resolucao_tela = resolucao_tela
        self.densidade_pixels = densidade_pixels
        self.fps_tela = fps_tela
        self.protecao_tela = protecao_tela
        self.camera_megapixels = camera_megapixels
        self.camera_resolucao = camera_resolucao
        self.camera_aperture = camera_aperture
        self.camera_estabilizacao = camera_estabilizacao
        self.camera_autofoco = camera_autofoco
        self.camera_flash = camera_flash
        self.camera_hdr = camera_hdr
        self.camera_localizacao = camera_localizacao
        self.camera_detecao_facial = camera_detecao_facial
        self.camera_frontal = camera_frontal
        self.video_resolucao = video_resolucao
        self.video_auto_foco = video_auto_foco
        self.video_fps = video_fps
        self.video_estabilizacao = video_estabilizacao
        self.video_slow_motion = video_slow_motion
        self.video_foto_em_video = video_foto_em_video
        self.video_camera_frontal = video_camera_frontal

    def mostrar_especificacoes(self):
        print("Especificações do Celular:")

        print("\nDados Gerais:")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Sistema Operacional: {self.sistema_operacional}")
        print(f"Disponibilidade: {self.disponibilidade}")
        print(f"Dimensões: {self.dimensoes}")
        print(f"Peso: {self.peso}")
        print(f"Resistência à Água: {self.resistencia_agua}")

        print("\nDados Técnicos:")
        print(f"Processador: {self.processador}")
        print(f"Chipset: {self.chipset}")
        print(f"Memória RAM: {self.memoria_ram}")
        print(f"GPU: {self.gpu}")
        print(f"Armazenamento: {self.armazenamento}")
        print(f"Memória Expansível: {self.memoria_expansivel}")

        print("\nBateria:")
        print(f"Tipo de Bateria: {self.bateria_tipo}")
        print(f"Capacidade da Bateria: {self.bateria_capacidade}")

        print("\nTela:")
        print(f"Tipo de Tela: {self.tipo_tela}")
        print(f"Tamanho da Tela: {self.tamanho_tela}")
        print(f"Resolução da Tela: {self.resolucao_tela}")
        print(f"Densidade de Pixels: {self.densidade_pixels}")
        print(f"FPS da Tela: {self.fps_tela}")
        print(f"Proteção da Tela: {self.protecao_tela}")

        print("\nCâmera:")
        print(f"Câmera Megapixels: {self.camera_megapixels}")
        print(f"Resolução da Câmera: {self.camera_resolucao}")
        print(f"Abertura da Câmera: {self.camera_aperture}")
        print(f"Estabilização da Câmera: {self.camera_estabilizacao}")
        print(f"Autofoco da Câmera: {self.camera_autofoco}")
        print(f"Flash da Câmera: {self.camera_flash}")
        print(f"HDR da Câmera: {self.camera_hdr}")
        print(f"Localização da Câmera: {self.camera_localizacao}")
        print(f"Detecção Facial da Câmera: {self.camera_detecao_facial}")
        print(f"Câmera Frontal: {self.camera_frontal}")

        print("\nVídeo:")
        print(f"Resolução de Vídeo: {self.video_resolucao}")
        print(f"Autofoco de Vídeo: {self.video_auto_foco}")
        print(f"FPS de Vídeo: {self.video_fps}")
        print(f"Estabilização de Vídeo: {self.video_estabilizacao}")
        print(f"Slow Motion: {self.video_slow_motion}")
        print(f"Foto em Vídeo: {self.video_foto_em_video}")
        print(f"Câmera Frontal de Vídeo: {self.video_camera_frontal}")

