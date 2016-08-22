from random import randint
import os
import time
from Classes.Solicitacao import Solicitacao
from Classes.Controlador import Controlador
from Util.Common import Common


c = Controlador()
c.iniciar_lista_elevador()
c.ligar_elevadores()
s = Solicitacao(randint(0, Common.numAndares), randint(0, Common.numAndares))
c.add_solicitacao_a_fila(s)
count = 0
while 1:
    count += 1
    if count % randint(1, Common.tempoMaxNovaSolicitacao) == 0:
        s = Solicitacao(randint(0, Common.numAndares), randint(0, Common.numAndares))
        c.add_solicitacao_a_fila(s)
        pass
    os.system('cls')
    c = Controlador()
    print(c)
    c.atender_solicitacao()
    time.sleep(1)
