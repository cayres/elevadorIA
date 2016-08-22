class Solicitacao(object):
    """Summary
    Classe que representa solicitações
    Attributes:
        andarFinal (Int): Description
        andarInicial (Int): Description
        mudouElevador (bool): Description
    """

    def __init__(self, andarInicial, andarFinal):
        self.andarInicial = andarInicial
        self.andarFinal = andarFinal

    def __str__(self):
        return "[" + str(self.andarInicial) + ", " + str(self.andarFinal) + " ]"

    def __repr__(self):
        return str(self)
