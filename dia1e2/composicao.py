names = [ "Bruno",  "Joao", "Bernardo", "Barbara", "Brian"]


# estilo funcional
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()

# estilo procedural
def starts_with_b(text):
    """Return bool iff text_starts with b"""
    return text[0].lower() == "b"


filtro = filter(starts_with_b, names)
filtro = list(filtro)

for name in filtro:
    print(name)
