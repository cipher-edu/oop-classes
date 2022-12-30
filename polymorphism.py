class Lang:
    def salom(self):
        raise NotImplementedError('sss')
class French(Lang):
    def salom(self):
        print("bonjuor")

class China(Lang):
    def salom(self):
        print("salomcha")

def intro(lang):
    lang.salom()

oybek = French()
amir = China()

intro(oybek)
intro(amir)