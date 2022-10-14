
class Nikola:
    def __init__(self, name, age) -> None:
        if (name != "Николай"):
            self.name = f"Я не {name},а Николай."
        else:
            self.name = name
        self.age = age


Nikolay = Nikola("Николай", 25)
Maksim = Nikola("Максим", 19)

print(Nikolay.name)
print(Maksim.name)
