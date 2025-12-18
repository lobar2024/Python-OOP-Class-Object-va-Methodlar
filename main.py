#   OOP - Object-Oriented Programming
#1-misol
class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f'{product} mahsuloti  qoshildi')

    # Obyektni chop etish(yani print)
    def __str__(self):
        return f'Dokon {self.name} \nLocation: {self.location} \nProducts: {self.products}'

#obyekt yaratish
m1 = Store('Supermarket', 'Pitnak shahar Al-Xorazmiy 13')
print(m1)

print()

#mahsulot qowiw
m1.add_product('Kofe')
print(m1)

print()

m1.add_product('Sut')
m1.add_product('Ananas')
print()
print(m1)

#2-misol
class Mashina:
    rang = 'qizil'
    model = 'toyota'
    yil = 2020

    def yur(self):
        print(f'{self.model} mashinasi yurmoqda')

mashina1 = Mashina()
print(mashina1.rang)
mashina1.yur()

#3-misol
class Hayvon:
    def shovqin_qil(self):
        print('Hayvon shovqin qilmoqda')

class It(Hayvon):
    def shovqin_qil(self):
        print('It: Vov-vov')

it1 = It()
it1.shovqin_qil()

class Mushuk(Hayvon):
    def shovqin_qil(self):
        print('Mushuk: Miyav-Miyav')

hayvonlar = [It(), Mushuk()]

for i in hayvonlar:
    i.shovqin_qil()
