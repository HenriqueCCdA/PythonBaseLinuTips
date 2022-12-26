import sys
import logging


RESERVAS_FILE = "reservas_v2.txt"
QUARTOS_FILE = "quartos_v2.txt"

# Acesso ao banco de dados

# TODO: Usar funções para ler os arquivos

ocupados = {} # acumulador
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": int(dias),
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)

quartos = {} # acumulador
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), # TODO: User Decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)

# Programa princial
print("Reservas no Hotel Pythonico da Linux Tips")
print('-' * 50)
if len(ocupados) == len(quartos):
    print("Hotel está locatado, volte depois")
    sys.exit(0)

nome_cliente = input("Qual é o seu nome: ").strip()
print()
print("Lista de quartos")
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - {head[2]:<9} - {head[3]:<10}")

for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "⛔" if not dados_quarto['disponivel'] else "👍"
    print(f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<6.2f} - {disponivel}")

print("-" * 50)

# reserva

try:
    num_quarto = int(input("Qual o quarto desejada: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro.")
        sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    print(f"Número inválido, digite apenas digitos.")
    sys.exit(0)

try:
    dias = int(input("Quantos dias:").strip())
except ValueError:
    print(f"Número inválido, digite apenas digitos.")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} o valor total estimado será {total:.2f}")

if input("Confirma? [digite y]").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")
        










