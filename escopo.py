# aqui come o escopo global
nome = "Global"


def funcao():
    # aqui começa o escopo local
    nome = "Local"

    def funcao_interna():
        # aqui começaao escopo local da função interna
        nome = "Interna"
        print("Escopo local da funcão interna:", locals())
        print("*" * 30)
        print(nome)
        return nome        
        # aqui termina o escopop local da função interna
    
    print("Escopo local da funcão:", locals())

    print("=" * 30)
    funcao_interna()
    print(nome)

    return nome
    # aqui termina o escopo logal

print("Escopo global do programa", globals())
print("-" * 30)

funcao()
print(nome)


# aqui termina o escopo gobal
    