# components - 0.0


class Person:
    """Represents a person."""
    company_name = "Dunder Mifflin"
    work_address = "Rua Stanton, Pensilvania"
    balance = 0 # Aributo de classe imutável

    # nunca defina um valor mutavel como atributo de classe
    prefered_colors = [] # classe mútavel

    def __init__(self, name, role="Undefined", prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # Injecao de dependencia - 1 arg metodo = a propria instancia
    def add_points(self, value):
        if self.role == "Manager":
            value *= 2
        self.balance += value


jim = Person("Jim Halpert", role="Salesman", prefered_colors=["Blue"])
jim.add_points(500)
jim.work_address = 'Home'
print(jim.name, jim.balance, jim.prefered_colors, jim.work_address, jim.role)

pam = Person("Pam Besly", "Receptionist", ["Purple", "Yello"])
pam.add_points(100)
print(pam.name, pam.balance, pam.prefered_colors, pam.work_address, pam.role)

print(Person.prefered_colors)
