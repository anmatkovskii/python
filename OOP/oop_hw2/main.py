class Soda:
    def __init__(self, addition_par=" "):
        self.addition = addition_par

    def show_my_drink(self):
        if self.addition != " ":
            print(f"Газування та {self.addition}")
        else:
            print("Звичайне газування")


class Nikola:
    def __init__(self, age_par, name_par):
        self.name = name_par
        self.age = age_par
        self.default_name = "Nikola"

    def __repr__(self):
        if self.name == "Nikola":
            return f'Name: {self.name}, Age: {self.age}'
        else:
            self.name = f"I am not {self.name}, I am {self.default_name}"
            return self.name


lemonade = Soda()
lemonade.show_my_drink()
mykola = Nikola("20", "Nikola")
maksym = Nikola("22", "Maksym")
print(mykola)
print(maksym)
