contador = 0

def func():
    global contador
    contador += 1

    subcontador = 0

    def funcao_interna():
        nonlocal subcontador
        subcontador += 1

    funcao_interna()
    print(subcontador)

func()
func()

print(contador)
