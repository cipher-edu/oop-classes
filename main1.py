class Auto:

    def __init__(self, nomi, color, price):
        self.nomi =nomi
        self.color = color
        self.price = price

    def car_detailes(self):
        print("mashina nomi ", self.nomi) 
        print("mashina rangi " , self.color)
        print("mashina narxi ", self.price)

    def tezlik(self):
        print("max tezligi 250")

    def  mark(self):
        print("3 avlod mashina")
class Car(Auto):
    def tezlik(self):
        print("max  tezligi 100")
    def mark(self):
        print("1-avlod mashina")
a = Auto("truck", "qora", 25000000)
b = Car("damas", "oq", 86000000)

a.car_detailes()
a.tezlik()
a.mark()
