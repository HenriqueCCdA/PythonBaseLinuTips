class Dog:
    def make_sound(self):
        return "woof woof"

class Cat:
    def make_sound(self):
        return "moew moew"



def print_sound(obj):
    if not hasattr(obj, "make_sound"):
        raise ValueError(f"{obj} is not Soundable")
    print(obj.make_sound())


rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)

print_sound(13)
