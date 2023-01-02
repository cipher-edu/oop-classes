class Lang:
    def salom(self):
        print("salomcha")
        raise NotImplementedError("klasda hatolik mavjud")
        

class Franch(Lang):
    # def salom(self):
    #     print("Bonjour")
    pass

class China(Lang):
    def salom(self):
        print("你好")

class En(Lang):
    def salom(self):
        print("hello")

def intro(lang):
    lang.salom()

a = Franch()
b = En()
x = China()

intro(a)
intro(x)