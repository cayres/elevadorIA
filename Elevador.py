import Solicitacao


class Elevador(object):
    """Summary

    Attributes:
        andarAtual (int): Description
        andarFinal (int): Description
        peso (int): Description
        solicitacoes (list): Description
        statusPorta (str): Description
    """

    def __init__(self):
        self.andarAtual = 0
        self.andarFinal = 0
        self.solicitacoes = []
        self.peso = 0
        self.statusPorta = 'F'

    def add_passageiro(self):
        self.peso += 70

    def remover_passageiro(self):
        self.peso -= 70

    def esta_ocupado(self):
        """Summary

        Returns:
            Bool
        """
        return self.peso > 0

    def esta_parado(self):
        """Summary

        Returns:
            Bool
        """
        return self.andarAtual == self.andarFinal

    def esta_subindo(self):
        """Summary

        Returns:
            Bool
        """
        return self.andarAtual < self.andarFinal

    def esta_descendo(self):
        """Summary

        Returns:
            Bool
        """
        return not(self.esta_subindo() or self.esta_parado())

    def solicitar_parada(self, solicitacao: Solicitacao):
        """Summary
        Atribui a solicitação
        Args:
            solicitacao (Solicitacoes): Description

        Returns:
            TYPE: Description
        """
        self.solicitacoes.append(solicitacao)

        if self.esta_parado():
            self.andarFinal = solicitacao.andarFinal
        elif self.esta_subindo() and solicitacao.andarFinal > self.andarFinal:
            self.andarFinal = solicitacao.andarFinal
        elif self.esta_descendo() and solicitacao.andarFinal < self.andarFinal:
            self.andarFinal = solicitacao.andarFinal

    def mover(self):
        """Summary
        Incrementa/Decrementa o andarAtual em direção ao andarFinal
        """
        if self.esta_parado():
            return
        if self.esta_subindo():
            self.andarAtual += self.andarAtual
        else:
            self.andarAtual -= self.andarAtual

    def calcular_custo_parada(self, solicitacao: Solicitacao) -> int:
        """Summary
        Calcula o custo que o elevador terá para atender a solicitação.
                Custo = NAP + (NP * NSP)
                NAP -> número de andares à percorrer
                                NP -> número de paradas do percurso
                                NSP -> número de solicitações de parada para o andar
        Args:
            solicitacao (Solicitacoes): Description

        Returns:
            int: Description
        """
        if self.esta_subindo() and self.andarAtual > solicitacao.andarInicial or self.esta_descendo() and self.andarAtual < solicitacao.andarInicial:
            return -1
        
