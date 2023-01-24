contador = 0

def incrementa_contador():
    global contador
    contador += 1


incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)