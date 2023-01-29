from typing import Union


def soma(a: Union[int, str], b: Union[int, str]):
    return a + b

soma(1, 2)
soma("Bruno", "Bruno")


# Carrinho de compras
from decimal import Decimal


produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5
cliente_especial = True


def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade

if cliente_especial:
    valor = Decimal(4.3)

total = calcula_total(valor, quantidade)


print("Tipo:", type(total))
print(f"O total é R${total:.2f}")
