class Auto:
    def __init__(self, name, color, price):
        self.name=name
        self.color=color
        self.price=price
    
    def car_detailes(self):
        print("avto nomi ", self.name)
        print("avto rangi", self.color)
        print("avto narxi", self.price)

    def tezlik(self):
        print("telizgi 250 km/h")

    def mark(self):
        print("mark")
class Car(Auto):
    def car_detailes(self):
        print("avto nomi ", self.name)
        print("avto rangi", self.color)
        print("avto narxi", self.price)
    def tezlik(self):
        print("telizgi 250 km/h")

    def mark(self):
        print("mark")

a = Auto("truck", "qoro", 25000000)
b = Car("damas", "oq", 8600000)

a.tezlik()
b.car_detailes()