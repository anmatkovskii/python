# Task 1

class Device:
    def __init__(self, price, energy_consumption, weight):
        self.price = price
        self.energy_consumption = energy_consumption
        self.weight = weight

    def __repr__(self):
        return f'{self.price}$, {self.energy_consumption}VT, {self.weight}Kg'

    def new_price(self, new_price):
        self.price = new_price
        return "Done"

    def new_energy(self, new_energy):
        self.energy_consumption = new_energy
        return "Done"

    def new_weight(self, new_weight):
        self.weight = new_weight
        return "Done"


class CoffeeMachine(Device):
    def __init__(self, price, energy_consumption, weight, interface, color):
        super().__init__(price, energy_consumption, weight)
        self.interface = interface
        self.color = color

    def __repr__(self):
        return f'{self.price}$, {self.energy_consumption}VT, {self.weight}Kg, Interface: {self.interface},' \
               f' Color: {self.color}'

    def new_interface(self, new_interface):
        self.interface = new_interface
        return "Done"

    def new_color(self, new_color):
        self.color = new_color
        return "Done"


class Blender(Device):
    def __init__(self, price, energy_consumption, weight, speed, color):
        super().__init__(price, energy_consumption, weight)
        self.speed = speed
        self.color = color

    def __repr__(self):
        return f'{self.price}$, {self.energy_consumption}VT, {self.weight}Kg, Speed: {self.speed},' \
               f' Color: {self.color}'

    def new_speed(self, new_speed):
        self.speed = new_speed
        return "Done"

    def new_color(self, new_color):
        self.color = new_color
        return "Done"


class MeatGrinder(Device):
    def __init__(self, price, energy_consumption, weight, grinding_speed, color):
        super().__init__(price, energy_consumption, weight)
        self.grinding_speed = grinding_speed
        self.color = color

    def __repr__(self):
        return f'{self.price}$, {self.energy_consumption}VT, {self.weight}Kg, grinding_speed: {self.grinding_speed},' \
               f' Color: {self.color}'

    def new_grinding_speed(self, new_grinding_speed):
        self.grinding_speed = new_grinding_speed
        return "Done"

    def new_color(self, new_color):
        self.color = new_color
        return "Done"


# Task 3


class Money:
    def __init__(self, gryvni, kopijky):
        self.gryvni = int(gryvni)
        self.kopijky = int(kopijky)
        while True:
            if self.kopijky >= 100:
                self.gryvni += 1
                self.kopijky -= 100
            else:
                break

    def __repr__(self):
        return f'Your balance: {self.gryvni},{self.kopijky}UAH'

    def new_grn(self, new_grn):
        self.gryvni = new_grn
        return "Done"

    def new_kop(self, new_kop):
        self.kopijky = new_kop
        return "Done"


class Product(Money):
    def __init__(self, gryvni, kopijky):
        super().__init__(gryvni, kopijky)

    def __repr__(self):
        return f'Product price: {self.gryvni},{self.kopijky}UAH'

    def new_grn(self, new_grn):
        self.gryvni = new_grn
        return print(f'New product price: {self.gryvni},{self.kopijky}UAH')

    def new_kop(self, new_kop):
        self.kopijky = new_kop
        return print(f'New product price: {self.gryvni},{self.kopijky}UAH')


