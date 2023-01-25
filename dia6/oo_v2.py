# components - 0.0


class Person:
    """Represents a person."""
    company_name = "Dunder Mifflin"
    work_address = "Rua Stanton, Pensilvania"
    balance = 0

    def add_points(person, value):
        if person.role == "Manager":
            value *= 2
        person.balance += value



jim = Person()
jim.name = "Jim Halpert"
jim.role = "Salesman"
jim.add_points(100)

print(id(jim))
print(jim.company_name)
print(jim.name)
print(jim.balance)

dwight = Person()
dwight.name = "Dwight Schrute"
dwight.role = "Manager"
dwight.add_points(100)
print(id(dwight))
print(dwight.company_name)
print(dwight.name)
print(dwight.balance)

pam = Person()
pam.name = "Pam Besly"
pam.role = "Receptionist"
pam.add_points(100)
print(id(pam))
print(pam.company_name)
print(pam.name)
print(pam.balance)
