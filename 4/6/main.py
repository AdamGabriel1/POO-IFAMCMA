from TreinadorJedi import TreinadorJedi
from IniciadosJedi import IniciadoJedi
from SessaoJedi import SessaoJedi

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

print(sessaojedi.getIniciado())

print(sessaojedi.getMediaAnoNascimento())

print(sessaojedi.getDescricao())