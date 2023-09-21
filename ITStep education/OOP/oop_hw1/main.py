class Cars:
    def __init__(self, model_par, age_par, producer_par, capacity_par, color_par, price_par):
        self.model = model_par
        self.age = age_par
        self.producer = producer_par
        self.capacity = capacity_par
        self.color = color_par
        self.price = price_par

    def __str__(self):
        return f'{self.model}, {self.age}, {self.producer}, {self.capacity}, {self.color}, {self.price}'

    def change_model(self, new_model):
        self.model = new_model
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_producer):
        self.producer = new_producer
        return "Saved"

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        return "Saved"

    def change_color(self, new_color):
        self.color = new_color
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"


class Books:
    def __init__(self, name_par, age_par, publisher_par, genre_par, author_par, price_par):
        self.name = name_par
        self.age = age_par
        self.publisher = publisher_par
        self.genre = genre_par
        self.author = author_par
        self.price = price_par

    def __str__(self):
        return f'{self.name}, {self.age}, {self.publisher}, {self.genre}, {self.author}, {self.price}'

    def change_name(self, new_name):
        self.name = new_name
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_publisher):
        self.publisher = new_publisher
        return "Saved"

    def change_genre(self, new_genre):
        self.genre = new_genre
        return "Saved"

    def change_author(self, new_author):
        self.author = new_author
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"


class Stadium:
    def __init__(self, name_par, opened_par, country_par, city_par, seats_par):
        self.name = name_par
        self.opened = opened_par
        self.country = country_par
        self.city = city_par
        self.seats = seats_par

    def __str__(self):
        return f'{self.name}, {self.opened}, {self.country}, {self.city}, {self.seats}'

    def change_name(self, new_name):
        self.name = new_name
        return "Saved"

    def change_age(self, new_opened):
        self.opened = new_opened
        return "Saved"

    def change_producer(self, new_country):
        self.country = new_country
        return "Saved"

    def change_genre(self, new_city):
        self.city = new_city
        return "Saved"

    def change_author(self, new_seats):
        self.seats = new_seats
        return "Saved"


car1 = Cars("BMW 920", "2020", "Germany", "5.5", "red", "50000")
book1 = Books("Метро 2033", "2020", "Навчальна книга - Богдан", "Фантастика", "Дмитро Ґлуховський", "449.00")
stadium = Stadium("Old Trafford", "1910", "England", "Manchester", "74310")
print(car1)
print(book1)
print(stadium)