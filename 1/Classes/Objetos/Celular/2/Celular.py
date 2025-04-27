class Celular:
    def __init__(self):
        self.especificacoes()

    def especificacoes(self):
        while True:
            print("|================================|")
            print("|       Todos os Celulares       |")
            print("|1. S24 Ultra                    |")
            print("|2. A14 5G                       |")
            print("|3. Redmi 9A                     |")
            print("|4. Red Magic 9 Pro Plus         |")
            print("|0. Sair                         |")
            print("|================================|")
            con=input("Digite o número do Celular que você quer ver as especificações: ")
            if con=="0":
                print("Fim do Programa.")
                break

            elif con=="1":
                self.s24ultra()

            elif con=="2":
                self.a14_5g()

            elif con=="3":
                self.r_9a()
            
            elif con=="4":
                self.r_m_9pp()

            else:
                print("Número errado tente novamente.")
                self.especificacoes

    def s24ultra(self):
        # DADOS GERAIS
        self.modelo="Samsung"
        self.nm_disp="S24 Ultra"
        self.tipo="Smartphone"
        self.so="Android 14 Samsung One UI 6.1"
        self.disponibilidade="2024/1"
        self.dimensoes="162.3 x 79 x 8.6 mm"
        self.peso="232 gramas"
        self.r_a_agua="Sim"
        self.dd_gr=f"Modelo: {self.modelo}\nNome do Dispositivo: {self.nm_disp}\nTipo: {self.tipo}\nSistema Operacional: {self.so}\nDisponibilidade: {self.disponibilidade}\nDimensões: {self.dimensoes}\nPeso: {self.peso}\nResistencia a Água: {self.r_a_agua}"

        # DADOS TÉCNICOS
        self.processador="1x 3.39 GHz Cortex-X4 + 3x 3.1 GHz Cortex-A720 + 2x 2.9 GHz Cortex-A720 + 2x 2.2 GHz Cortex-A520"
        self.chipset="Snapdragon 8 Gen 3 Qualcomm SM8650-AB"
        self.mem_ram="12 GB"
        self.gpu="Adreno 750"
        self.armazenamento="1 TB"
        self.memoria_expansivel="Não"
        self.dd_tec=f"Processador: {self.processador}\nChipset: {self.chipset}\nMemória RAM: {self.mem_ram}\nGPU: {self.gpu}\nArmazenamento: {self.armazenamento}\nMemória Expansivel: {self.memoria_expansivel}"

        # BATERIA
        self.tipo="LiPo"
        self.bateria="5000 mAh"
        self.bateria_all=f"Tipo: {self.tipo}\nBateria: {self.bateria}"

        # TELA
        self.resolucao="720x720"
        self.tela="6.8"
        self.resolucao="1440 x 3120 pixel"
        self.den_de_pixels="505 ppi"
        self.tipo="Dynamic AMOLED 2X"
        self.fps="120 Hz"
        self.protecao="Gorilla Glass Armor"
        self.tela_all=f"Resolução: {self.resolucao}\nTela: {self.tela}\nResolução: {self.resolucao}\nDensidade de Pixels: {self.den_de_pixels}\nTipo da Tela: {self.tipo}\nFPS: {self.fps}\nProteção: {self.protecao}"

        # CÂMERA
        self.megapixel="200 Mp + 50 Mp + 12 Mp + 10 Mp"
        self.resolucao="16330 x 12247 pixel"
        self.tamanho_do_sensor="1/1.3 '' + 1/2.55 '' + 1/3.52 ''"
        self.aperture_size="F 1.7 + F 3.4 + F 2.2 + F 2.4"
        self.estabilizacao="Ótica"
        self.angulo_maximo="120 °"
        self.zoom_otico="5 x"
        self.autofoco="Tem"
        self.foco_por_toque="Tem"
        self.flash="LED"
        self.hdr="Tem"
        self.dual_shot="Tem"
        self.localizacao="Tem"
        self.deteccao_facial="Tem"
        self.camera_frontal="12 Mp F 2.2"
        self.camera_all=f"Megapixels: {self.megapixel}\nResolução: {self.resolucao}\nTamanho do Sensor: {self.tamanho_do_sensor}\nAperture Size: {self.aperture_size}\nEstabilização: {self.estabilizacao}\nÂngulo Máximo: {self.angulo_maximo}\nZoom Otico: {self.zoom_otico}\nAutofoco: {self.autofoco}\nFoco por Toque: {self.foco_por_toque}\nFlash: {self.flash}\nHDR: {self.hdr}\nDual Shot: {self.dual_shot}\nLocalização: {self.localizacao}\nDetecção Facial: {self.deteccao_facial}\nCamera Frontal: {self.camera_frontal}"

        # VÍDEO
        self.resolucao_da_gravacao="8K UHD"
        self.auto_focagem_de_video="Tem"
        self.fps_da_gravacao="30 fps"
        self.estabilizacao_de_video="Tem"
        self.slow_motion="960 fps"
        self.video_hdr="Tem"
        self.dual_rec="Tem"
        self.stereo_sound_rec="Tem"
        self.foto_em_video="Tem"
        self.video_camera_frontal="4K (2160p), 60fps"
        self.opcoes_da_camera_frontal="HDR/Face Detection/Autofocus"
        self.video_all=f"Resolução da Gravação: {self.resolucao_da_gravacao}\nAuto Focagem de Vídeo: {self.auto_focagem_de_video}\nFPS da gravação: {self.fps_da_gravacao}\nEstabilização de Vídeo: {self.estabilizacao_de_video}\nSlow Motion: {self.slow_motion}\nVídeo HDR: {self.video_hdr}\nDual Rec: {self.dual_rec}\nStereo Sound Rec: {self.stereo_sound_rec}\nFoto em Vídeo: {self.foto_em_video}\nVídeo Camera Frontal: {self.video_camera_frontal}\nOpções da Câmera Frontal: {self.opcoes_da_camera_frontal}"

        # Print das Especificações
        print(f"\nDADOS GERAIS\n{self.dd_gr}\n")
        print(f"\nDADOS TÉCNICOS\n{self.dd_tec}\n")
        print(f"\nBATERIA\n{self.bateria_all}\n")
        print(f"\nTELA\n{self.tela_all}\n")
        print(f"\nCÂMERA\n{self.camera_all}\n")
        print(f"\nVÍDEO\n{self.video_all}\n")

    def a14_5g(self):
        # DADOS GERAIS
        self.modelo="Samsung"
        self.nm_disp="A14 5G"
        self.tipo="Smartphone"
        self.so="Android 13 Samsung One UI Core 5"
        self.disponibilidade="2023/1"
        self.dimensoes="167.7 x 78 x 9.1 mm"
        self.peso="202 gramas"
        self.r_a_agua="Sim"
        self.dd_gr=f"Modelo: {self.modelo}\nNome do Dispositivo: {self.nm_disp}\nTipo: {self.tipo}\nSistema Operacional: {self.so}\nDisponibilidade: {self.disponibilidade}\nDimensões: {self.dimensoes}\nPeso: {self.peso}\nResistencia a Água: {self.r_a_agua}"

        # DADOS TÉCNICOS
        self.processador="2x 2.2 GHz Cortex-A76 + 6x 2.0 GHz Cortex-A55"
        self.chipset="Dimensity 700 MediaTek MT6833"
        self.mem_ram="4 GB"
        self.gpu="Mali-G57 MC2"
        self.armazenamento="128 GB"
        self.memoria_expansivel="Sim, MicroSDXC atè 1024 GB"
        self.dd_tec=f"Processador: {self.processador}\nChipset: {self.chipset}\nMemória RAM: {self.mem_ram}\nGPU: {self.gpu}\nArmazenamento: {self.armazenamento}\nMemória Expansivel: {self.memoria_expansivel}"

        # BATERIA
        self.tipo="LiPo"
        self.bateria="5000 mAh"
        self.bateria_all=f"Tipo: {self.tipo}\nBateria: {self.bateria}"

        # TELA
        self.polegadas="6.6"
        self.resolucao="1080 x 2400 pixel"
        self.den_de_pixels="399 ppi"
        self.tipo="PLS LCD"
        self.fps="90 Hz"
        self.cores="16 milhões"
        self.tela_all=f"Polegadas: {self.polegadas}\nTela: {self.tela}\nResolução: {self.resolucao}\nDensidade de Pixels: {self.den_de_pixels}\nTipo da Tela: {self.tipo}\nFPS: {self.fps}\nCores: {self.cores}"

        # CÂMERA
        self.megapixel="50 Mp + 2 Mp + 2 Mp"
        self.resolucao="8165 x 6124 pixel"
        self.aperture_size="F 1.8 + F 2.4 + F 2.4"
        self.estabilizacao="Digital"
        self.autofoco="Tem"
        self.foco_por_toque="Tem"
        self.flash="LED"
        self.hdr="Tem"
        self.dual_shot="Tem"
        self.localizacao="Tem"
        self.deteccao_facial="Tem"
        self.camera_frontal="13 Mp F 2"
        self.camera_all=f"Megapixels: {self.megapixel}\nResolução: {self.resolucao}\nAperture Size: {self.aperture_size}\nEstabilização: {self.estabilizacao}\nAutofoco: {self.autofoco}\nFoco por Toque: {self.foco_por_toque}\nFlash: {self.flash}\nHDR: {self.hdr}\nDual Shot: {self.dual_shot}\nLocalização: {self.localizacao}\nDetecção Facial: {self.deteccao_facial}\nCamera Frontal: {self.camera_frontal}"

        # VÍDEO
        self.resolucao_da_gravacao="Full HD"
        self.auto_focagem_de_video="Tem"
        self.fps_da_gravacao="30 fps"
        self.video_camera_frontal="4K (2160p), 60fps"
        self.opcoes_da_camera_frontal="HDR/Face Detection/Autofocus"
        self.video_all=f"Resolução da Gravação: {self.resolucao_da_gravacao}\nAuto Focagem de Vídeo: {self.auto_focagem_de_video}\nFPS da gravação: {self.fps_da_gravacao}\nVídeo Camera Frontal: {self.video_camera_frontal}"

        # Print das Especificações
        print(f"\nDADOS GERAIS\n{self.dd_gr}\n")
        print(f"\nDADOS TÉCNICOS\n{self.dd_tec}\n")
        print(f"\nBATERIA\n{self.bateria_all}\n")
        print(f"\nTELA\n{self.tela_all}\n")
        print(f"\nCÂMERA\n{self.camera_all}\n")
        print(f"\nVÍDEO\n{self.video_all}\n")

    def r_9a(self):
        # DADOS GERAIS
        self.modelo="Xiaomi Redmi"
        self.nm_disp="9A"
        self.tipo="Smartphone"
        self.so="Android 10 MIUI 11"
        self.disponibilidade="2020/2"
        self.dimensoes="164.9 x 77.07 x 9 mm"
        self.peso="194 gramas"
        self.dd_gr=f"Modelo: {self.modelo}\nNome do Dispositivo: {self.nm_disp}\nTipo: {self.tipo}\nSistema Operacional: {self.so}\nDisponibilidade: {self.disponibilidade}\nDimensões: {self.dimensoes}\nPeso: {self.peso}"

        # DADOS TÉCNICOS
        self.processador="4x 2.0 GHz Cortex-A53 + 4x 1.5 GHz Cortex-A53"
        self.chipset="Helio G25 MediaTek"
        self.mem_ram="2 GB"
        self.gpu="PowerVR GE8320"
        self.armazenamento="32 GB"
        self.memoria_expansivel="Sim, MicroSDXC atè 512 GB"
        self.dd_tec=f"Processador: {self.processador}\nChipset: {self.chipset}\nMemória RAM: {self.mem_ram}\nGPU: {self.gpu}\nArmazenamento: {self.armazenamento}\nMemória Expansivel: {self.memoria_expansivel}"

        # BATERIA
        self.tipo="LiPo"
        self.bateria="5000 mAh"
        self.bateria_all=f"Tipo: {self.tipo}\nBateria: {self.bateria}"

        # TELA
        self.polegadas="6.53"
        self.resolucao="720 x 1600 pixel"
        self.den_de_pixels="269 ppi"
        self.tipo="IPS LCD"
        self.fps="60 Hz"
        self.cores="16 milhões"
        self.tela_all=f"Polegadas: {self.polegadas}\nResolução: {self.resolucao}\nDensidade de Pixels: {self.den_de_pixels}\nTipo da Tela: {self.tipo}\nFPS: {self.fps}\nCores: {self.cores}"

        # CÂMERA
        self.megapixel="13 Mp"
        self.resolucao="4163 x 3122 pixel"
        self.aperture_size="F 2.2"
        self.estabilizacao="Digital"
        self.autofoco="Tem"
        self.foco_por_toque="Tem"
        self.flash="LED"
        self.hdr="Tem"
        self.localizacao="Tem"
        self.deteccao_facial="Tem"
        self.camera_frontal="5 Mp F 2.2"
        self.camera_all=f"Megapixels: {self.megapixel}\nResolução: {self.resolucao}\nAperture Size: {self.aperture_size}\nEstabilização: {self.estabilizacao}\nAutofoco: {self.autofoco}\nFoco por Toque: {self.foco_por_toque}\nFlash: {self.flash}\nHDR: {self.hdr}\nLocalização: {self.localizacao}\nDetecção Facial: {self.deteccao_facial}\nCamera Frontal: {self.camera_frontal}"

        # VÍDEO
        self.resolucao_da_gravacao="Full HD"
        self.auto_focagem_de_video="Tem"
        self.fps_da_gravacao="30 fps"
        self.video_camera_frontal="Full HD, 30fps"
        self.opcoes_da_camera_frontal="HDR/Face Detection"
        self.video_all=f"Resolução da Gravação: {self.resolucao_da_gravacao}\nAuto Focagem de Vídeo: {self.auto_focagem_de_video}\nFPS da gravação: {self.fps_da_gravacao}\nVídeo Camera Frontal: {self.video_camera_frontal}"

        # Print das Especificações
        print(f"\nDADOS GERAIS\n{self.dd_gr}\n")
        print(f"\nDADOS TÉCNICOS\n{self.dd_tec}\n")
        print(f"\nBATERIA\n{self.bateria_all}\n")
        print(f"\nTELA\n{self.tela_all}\n")
        print(f"\nCÂMERA\n{self.camera_all}\n")
        print(f"\nVÍDEO\n{self.video_all}\n")

    def r_m_9pp(self):
        # DADOS GERAIS
        self.modelo="Nubia"
        self.nm_disp="Red Magic 9 Pro Plus"
        self.tipo="Smartphone"
        self.so="Android 14 Redmagic OS 9"
        self.disponibilidade="2023/3"
        self.dimensoes="163.98 x 76.35 x 8.9 mm"
        self.peso="229 gramas"
        self.dd_gr=f"Modelo: {self.modelo}\nNome do Dispositivo: {self.nm_disp}\nTipo: {self.tipo}\nSistema Operacional: {self.so}\nDisponibilidade: {self.disponibilidade}\nDimensões: {self.dimensoes}\nPeso: {self.peso}"

        # DADOS TÉCNICOS
        self.processador="1x 3.3 GHz Cortex-X4 + 3x 3.2 GHz Cortex-A720 + 2x 3.0 GHz Cortex-A720 + 2x 2.3 GHz Cortex-A520"
        self.chipset="Snapdragon 8 Gen 3 Qualcomm SM8650-AB"
        self.mem_ram="16 GB"
        self.gpu="Adreno 750"
        self.armazenamento="512 GB"
        self.memoria_expansivel="Não"
        self.dd_tec=f"Processador: {self.processador}\nChipset: {self.chipset}\nMemória RAM: {self.mem_ram}\nGPU: {self.gpu}\nArmazenamento: {self.armazenamento}\nMemória Expansivel: {self.memoria_expansivel}"

        # BATERIA
        self.tipo="LiPo"
        self.bateria="6500 mAh"
        self.bateria_all=f"Tipo: {self.tipo}\nBateria: {self.bateria}"

        # TELA
        self.tela="6.8"
        self.resolucao="1116 x 2480 pixel"
        self.den_de_pixels="400 ppi"
        self.tipo="AMOLED"
        self.fps="120 Hz"
        self.cores="mais de 16 milhões"
        self.tela_all=f"Tela: {self.tela}\nResolução: {self.resolucao}\nDensidade de Pixels: {self.den_de_pixels}\nTipo da Tela: {self.tipo}\nFPS: {self.fps}\ncores: {self.cores}"

        # CÂMERA
        self.megapixel="50 Mp + 50 Mp + 2 Mp"
        self.resolucao="8165 x 6124 pixel"
        self.tamanho_do_sensor="1/1.57 '' + 1/2.76 ''"
        self.aperture_size="F 2.4"
        self.estabilizacao="Ótica"
        self.autofoco="Tem"
        self.foco_por_toque="Tem"
        self.flash="LED"
        self.hdr="Tem"
        self.localizacao="Tem"
        self.deteccao_facial="Tem"
        self.camera_frontal="16 Mp F 2"
        self.camera_all=f"Megapixels: {self.megapixel}\nResolução: {self.resolucao}\nTamanho do Sensor: {self.tamanho_do_sensor}\nAperture Size: {self.aperture_size}\nEstabilização: {self.estabilizacao}\nAutofoco: {self.autofoco}\nFoco por Toque: {self.foco_por_toque}\nFlash: {self.flash}\nHDR: {self.hdr}\nLocalização: {self.localizacao}\nDetecção Facial: {self.deteccao_facial}\nCamera Frontal: {self.camera_frontal}"

        # VÍDEO
        self.resolucao_da_gravacao="8K UHD"
        self.auto_focagem_de_video="Tem"
        self.fps_da_gravacao="30 fps"
        self.estabilizacao_de_video="Tem"
        self.slow_motion="240 fps"
        self.foto_em_video="Tem"
        self.video_camera_frontal="Full HD, 60fps"
        self.opcoes_da_camera_frontal="HDR"
        self.video_all=f"Resolução da Gravação: {self.resolucao_da_gravacao}\nAuto Focagem de Vídeo: {self.auto_focagem_de_video}\nFPS da gravação: {self.fps_da_gravacao}\nEstabilização de Vídeo: {self.estabilizacao_de_video}\nSlow Motion: {self.slow_motion}\nFoto em Vídeo: {self.foto_em_video}\nVídeo Camera Frontal: {self.video_camera_frontal}\nOpções da Câmera Frontal: {self.opcoes_da_camera_frontal}"

        # Print das Especificações
        print(f"\nDADOS GERAIS\n{self.dd_gr}\n")
        print(f"\nDADOS TÉCNICOS\n{self.dd_tec}\n")
        print(f"\nBATERIA\n{self.bateria_all}\n")
        print(f"\nTELA\n{self.tela_all}\n")
        print(f"\nCÂMERA\n{self.camera_all}\n")
        print(f"\nVÍDEO\n{self.video_all}\n")
