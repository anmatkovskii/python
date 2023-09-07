import os.path
from easygui import *


class Money:
    def __init__(self,money,penni,valuta):
        self.money = money
        self.penni = penni
        self.valuta = valuta
        self.curs = {'UAH': {'UAH':1, 'USD':42, 'EUR':41}, 'USD': {'UAH':0.025, 'USD':1, 'EUR':0.025},
                     'EUR': {'UAH':0.024, 'USD':0.98, 'EUR':1}}
        self.discount = 0

    def __repr__(self):
        return f' {self.money}.{self.penni} {self.valuta}'

    def sell(self,product):

        if self.discount >= 0 and self.discount < 500:
            product_money = product.money * self.curs.get(self.valuta).get(product.valuta)
            product_penni = product.penni * self.curs.get(self.valuta).get(product.valuta)
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money
                self.discount += product_money
                return f'{product} {int(self.money)} {int(self.penni)} {self.valuta}'
            else:
                return f'You don t have money'

        if self.discount > 500 and self.discount < 1000:
            product_money = product.money * self.curs.get(self.valuta).get(product.valuta) - product.money * self.curs.get(self.valuta).get(product.valuta) * 0.05
            product_penni = product.penni * self.curs.get(self.valuta).get(product.valuta) - product.penni * self.curs.get(self.valuta).get(product.valuta) * 0.05
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money

                self.discount += product_money
                return f'{product} {int(self.money)} {int(self.penni)} {self.valuta}'
            else:
                return f'You don t have money'

        if self.discount > 1000:
            product_money = product.money * self.curs.get(self.valuta).get(product.valuta) - product.money * self.curs.get(self.valuta).get(product.valuta) * 0.1
            product_penni = product.penni * self.curs.get(self.valuta).get(product.valuta) - product.penni * self.curs.get(self.valuta).get(product.valuta) * 0.1
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money
                self.discount += product_money
                return f'{product} {int(self.money)} {int(self.penni)} {self.valuta} '
            else:
                return f'You don t have money'

class Product (Money):
    def __init__(self,money,penni,valuta,name):
        super().__init__(money,penni,valuta)
        self.name = name
        self.path = os.path.join('data_file', 'file.txt')
        file = open(self.path, 'a')
        file.write(f'Name:{self.name} price:{self.money}.{self.penni} {self.valuta}\n')
        file.close()

    def __repr__(self):
        return f'{self.money} {self.penni} {self.valuta}'

    def shop(self):
        file = open(self.path, 'r')
        file1 = file.readlines()
        file.close()
        return ''.join(file1)

# money = Money(money=20000, penni=75, valuta='UAH')
# coffe = Product(name='coffe',money=20, penni=25, valuta='UAH')
# latte = Product(name='latte',money=2, penni=1, valuta='EUR')
# a = Product(name='a',money=100, penni=25, valuta='UAH')
# b = Product(name='b',money=50, penni=25, valuta='EUR')

# print(money)
# print(money.sell(coffe))
# print(money)
# print(coffe.shop())
# print(money.sell(b))
# print(money.sell(a))