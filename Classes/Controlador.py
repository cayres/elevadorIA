from .Elevador import Elevador
from .Solicitacao import Solicitacao
from Util.Common import Common
import datetime
import threading


class Controlador:

    listaElevador = []
    filaSolicitacao = []
    numAndares = Common.numAndares

    def __str__(self):
        current_time = datetime.datetime.now()
        result = "Elevadores Inteligentes " + \
            current_time.strftime("%d/%m/%Y %H:%M:%S") + "\n"
        for i in range(Common.numAndares, -1, -1):
            result += " | "
            for j in range(0, Common.numElevadores):
                if Controlador.listaElevador[j].andarAtual == i:
                    result += Controlador.listaElevador[j].statusPorta
                    continue
                result += " == "
            result += " | \n"
        result += "Fila de solicitações: " + \
            str(Controlador.filaSolicitacao)
        for i, el in enumerate(Controlador.listaElevador):
            result += "\nElevador" + str(i + 1).zfill(2) + ": " + str(el)
        return result.strip()

    def iniciar_lista_elevador(cls):
        for x in range(0, Common.numElevadores):
            Controlador.listaElevador.append(Elevador())

    def ligar_elevadores(cls):
        for el in Controlador.listaElevador:
            t = threading.Thread(target=el.mover)
            t.start()

    def add_solicitacao_a_fila(cls, solicitacao: Solicitacao):
        Controlador.filaSolicitacao.append(solicitacao)

    def atender_solicitacao(cls):
        """Summary

        Args:
            solic (Solicitacao, optional): Se solic não for passado
            o controlador pega o primeiro da fila de solicitações
        """
        if len(Controlador.filaSolicitacao) == 0:
            return
        solic = Controlador.filaSolicitacao.pop(0)
        listaCusto = []
        for i, elv in enumerate(Controlador.listaElevador):
            custo = elv.calcular_custo_parada(solic)
            if custo != -1:
                listaCusto.append([elv.calcular_custo_parada(solic), i])
        else:

            # count = 0
            # count += sum(1 for s in result)
            if len(listaCusto) == 0:
                Controlador.filaSolicitacao.append(solic)
            else:
                listaCusto.sort(key=lambda x: x[0])
                melhorCusto = listaCusto.pop(0)
                Controlador.listaElevador[
                    melhorCusto[1]].solicitar_parada(solic)
