people = [
    {
        "name": "Jim Halpert",
        "balance": 500,
        "role": "Salesman"
    },
    {
        "name": "Dwight Schrute",
        "balance": 100,
        "role": "Manager"
    }
]

def add_points(person, value):
    data = person.copy()
    if data["role"] == "Maneger":
        value *= 2
    data["balance"] += value
    return data

result = map(lambda person: add_points(person, 100), people)

print(list(result))
