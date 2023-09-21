from easygui import *
from main import *


money = Money(money=20000, penni=75, valuta='UAH')
coffe = Product(name='coffe',money=20, penni=25, valuta='UAH')
latte = Product(name='latte',money=2, penni=1, valuta='EUR')
a = Product(name='a',money=100, penni=25, valuta='UAH')
b = Product(name='b',money=50, penni=25, valuta='EUR')

# print(money)
# print(money.sell(coffe))
# print(money)
# print(coffe.shop())
print(money.sell(b))
print(money.sell(a))