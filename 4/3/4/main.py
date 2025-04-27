from Baterista import Baterista
from Saxofonista import Saxofonista
from Musico import Musico
from Orquestra import Orquestra

baterista=Baterista()
saxofonista1=Saxofonista()
saxofonista2=Saxofonista()
saxofonista3=Saxofonista()
saxofonista4=Saxofonista()
musico1=Musico()
musico2=Musico()
orquestra=Orquestra()

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
