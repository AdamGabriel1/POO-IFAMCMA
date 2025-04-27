from Baterista import Baterista
from Saxofonista import Saxofonista
from Musico import Musico
from Orquestra import Orquestra

baterista=Baterista()
saxofonista=Saxofonista()
musico=Musico()
orquestra=Orquestra()

baterista.toca_com("Saxofonista")
saxofonista.toca_com("Baterista")

musico.toca_em("Orquestra")
orquestra.toca_em("Musico")
