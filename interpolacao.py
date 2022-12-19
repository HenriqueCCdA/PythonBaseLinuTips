email_tmpl = """
    Olá, %(nome)s
     
    Tem interesse em comprar %(produto)s?
     
    Este o produto é ótimo para resolver
    %(texto)s
     
    Clique agora em %(link)s
     
    Apenas %(quantidade)d disponiveis!
    
    Preço promocional %(preco).2f
    """


clientes = ['Maria', 'João', 'Bruno']

for cliente in clientes:
    print(email_tmpl % {'nome': cliente, 'produto': 'caneta', 'texto': 'Escrever muito bem', 'link': 'https://', 'quantidade': 1, 'preco': 50.5})
 
