from .Solicitacao import Solicitacao
from Util.Common import Common
import time
import math


class Elevador(object):
    """Summary

    Attributes:
        andarAtual (int): Description
        peso (int): Description
        solicitacoes (list): Description
        statusPorta (str): Description
    """

    def __init__(self):
        self.andarAtual = 0
        self.solicitacoes = []
        self.statusPorta = ' >< '

    def __str__(self):
        return "{ AndarAtual: " + str(self.andarAtual) + ", " + self.statusPorta + ", Solicitações: " + str(self.solicitacoes) + " }"

    def __repr__(self):
        return str(self)

    def esta_parado(self):
        """Summary

        Returns:
            Bool
        """
        return len(self.solicitacoes) == 0

    def esta_subindo(self):
        """Summary

        Returns:
            Bool
        """
        return not self.esta_parado() and self.andarAtual < self.solicitacoes[0].andarInicial

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
        if len(self.solicitacoes) == 0:
            self.solicitacoes.append(solicitacao)
            return
        if len(self.solicitacoes) == 1:
            if solicitacao.andarFinal < self.solicitacoes[0].andarInicial:
                self.solicitacoes = [solicitacao] + self.solicitacoes
                return
            else:
                self.solicitacoes = self.solicitacoes + [solicitacao]
                return
        for i, s in enumerate(self.solicitacoes):
            if solicitacao.andarFinal < s.andarInicial:
                self.solicitacoes = self.solicitacoes[
                    i:] + [solicitacao] + self.solicitacoes[:i]

    def realizar_parada(self):
        for i, s in enumerate(self.solicitacoes):
            if s.andarInicial == self.andarAtual:
                s.andarInicial = -1
                return "<  >"
            if s.andarInicial == -1 and s.andarFinal == self.andarAtual:
                self.solicitacoes.remove(s)
                return "<  >"
            else:
                if s.andarInicial > self.andarAtual:
                    self.andarAtual += 1
                    return " >< "
                else:
                    if self.andarAtual == 0:
                        return " >< "
                    self.andarAtual -= 1
                    return " >< "

    def mover(self):
        """Summary
        Incrementa/Decrementa o andarAtual em direção ao andarFinal
        """
        while 1:
            numParada = sum(1 for s in self.solicitacoes if s.andarInicial ==
                            self.andarAtual or s.andarFinal == self.andarAtual)
            if numParada > 0:
                self.statusPorta = self.realizar_parada()
                continue
            if self.esta_parado():
                continue
            elif self.solicitacoes[0].andarInicial != -1:
                if self.solicitacoes[0].andarInicial > self.andarAtual:
                    self.andarAtual += 1
                    self.statusPorta = " >< "
                else:
                    self.andarAtual -= 1
                    self.statusPorta = " >< "
            else:
                if self.solicitacoes[0].andarFinal > self.andarAtual:
                    self.andarAtual += 1
                    self.statusPorta = " >< "
                else:
                    self.andarAtual -= 1
                    self.statusPorta = " >< "
            time.sleep(Common.tempoDeslocamentoPorAndar)

    def calcular_custo_parada(self, solicitacao: Solicitacao) -> int:
        """Summary
        Calcula o custo que o elevador terá para atender a solicitação.
                Custo = NAP + NP
                NAP -> número de andares à percorrer
                                NP -> número de paradas do percurso
        Args:
            solicitacao (Solicitacoes): Description

        Returns:
            int: Description
        """
        NAP = 0
        NP = 0

        if not self.pode_atender_solicitacao(solicitacao):
            return -1

        NAP = math.fabs(solicitacao.andarFinal - solicitacao.andarInicial) + \
            math.fabs(solicitacao.andarInicial - self.andarAtual)
        if self.esta_subindo():
            NP += sum(1 for s in self.solicitacoes if self.andarAtual <=
                      s.andarInicial and s.andarInicial <= solicitacao.andarFinal)
            NP += sum(1 for s in self.solicitacoes if self.andarAtual <=
                      s.andarFinal and s.andarFinal <= solicitacao.andarFinal)
        if self.esta_descendo():
            NP += sum(1 for s in self.solicitacoes if self.andarAtual >=
                      s.andarInicial and s.andarInicial >= solicitacao.andarFinal)
            NP += sum(1 for s in self.solicitacoes if self.andarAtual >=
                      s.andarFinal and s.andarFinal >= solicitacao.andarFinal)

        return NAP + NP

    def pode_atender_solicitacao(self, solicitacao: Solicitacao) -> bool:
        """Summary
        Verifica se o elevador é capaz de atender a solicitação naquele momento.
        Args:
            solicitacao (Solicitacao): Description

        Returns:
            bool: Description
        """
        if self.esta_subindo() and solicitacao.andarInicial > solicitacao.andarFinal:
            return False
        elif self.esta_descendo() and solicitacao.andarInicial < solicitacao.andarFinal:
            return False
        elif self.esta_subindo() and self.andarAtual > solicitacao.andarInicial:
            return False
        elif self.esta_descendo() and self.andarAtual < solicitacao.andarInicial:
            return False
        return True
