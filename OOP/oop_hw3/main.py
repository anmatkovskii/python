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

    def buy_product(self, product_price):
        a = product_price.split(".")
        self.gryvni -= int(a[0])
        self.kopijky -= int(a[1])
        if self.kopijky < 0:
            self.gryvni -= 1
            self.kopijky += 100
        return print(f'Bought! Your current balance: {self.gryvni},{self.kopijky}UAH')


x = Money("5000", "0")
print(x)
x.buy_product("425.15")