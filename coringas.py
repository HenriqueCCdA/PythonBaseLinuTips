def funcao(*args, timeout=10, **kwargs):
    print(args)
    for item in args:
        print(item)

    print(kwargs)
    print(f"{timeout=}")

funcao("Bruno", 1, True, [], timeout=90, nome="Joao", cidade="Viana", data="hoje")