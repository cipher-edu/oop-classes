class Inson(object):

    def __init__(self, name, id):

        self.name = name
        self.id = id

class Ishchi(Inson):

    def __init__(self, name, id, maosh, ishkuni):

        self.maosh = maosh
        self.ishkuni = ishkuni
        
        Inson.__init__(self, name, id)
    
    def display1(self):
        print("meining ismim {}".format(self.name))
        print("mening id {}".format(self.id))
        print("maoshim {}".format(self.maosh))
        print("ish kunim {}".format(self.ishkuni))

natija = Ishchi("Oybek", 1541515, 8000000, 6)

natija.display1()
