import Elevador
import Solicitacao


class Controlador:

    listaElevador = []
    filaSolicitacao = []

    def iniciar_lista_elevador(cls, numElevadores: int):
        for x in range(0, numElevadores + 1):
            cls.listaElevador.append(Elevador())

    def add_solicitacao_a_fila(cls, solicitacao: Solicitacao):
        cls.listaSolicitacao.append(solicitacao)

    def atender_solicitacao(cls, solic: Solicitacao = None):
        """Summary

        Args:
            solic (Solicitacao, optional): Se solic não for passado
            o controlador pega o primeiro da fila de solicitações
        """
        if solic is None:
            solic = cls.filaSolicitacao.pop(0)
        listaCusto = []
        for i, elv in enumerate(cls.listaElevador):
            listaCusto.append([elv.calcular_custo_parada(solic), i])
        else:
            result = filter(lambda x: x[1] != -1, listaCusto)
            if len(result) == 0:
                cls.filaSolicitacao.append(solic)
            else:
                listaCusto.sort(key=lambda x: x[1])
                melhorCusto = listaCusto.pop(0)
                cls.listaElevador[melhorCusto[2]].solicitar_parada(solic)
