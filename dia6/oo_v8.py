from abc import ABC


class Conta(ABC):

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0


class ContaCorrente(Conta):
    _id_interno = 456789

    @property
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = ContaCorrente("Bruno")
print(dir(conta))
print(conta.cliente)
print(conta.saldo)

conta.saldo = 100
print(conta.saldo)

conta.saldo = -50
print(conta.saldo)

del conta.saldo
print(conta.saldo)
