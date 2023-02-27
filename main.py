class Animal:
    def mananca(self):
        #->None:
        print("Animal")

class Pisica(Animal):
    def mananca(self):
        print("Pisica")

x=Animal()
x.mananca()
y=Pisica()
y.mananca()




#totul e public in py, ca sa fie safe punem underscore
#self=ca this-ul, se recomanda folosirea lui self
#tipe hint