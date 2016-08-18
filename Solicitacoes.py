class Solicitacao(object):
    """Summary
    Classe que representa solicitações
    Attributes:
        andarFinal (Int): Description
        andarInicial (Int): Description
        mudouElevador (bool): Description
    """

    def __init__(self, andarInicial, andarFinal, io):
        self.andarInicial = andarInicial
        self.andarFinal = andarFinal
