#multiple inheritance
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(self.name)
        print(self.species)

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="Dog")
        self.breed=breed
    def show_details(self):
        animal.show_details(self)
        print(self.breed)
        
class mainclass(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed="xyz")
        self.color=color
        
    def show_details(self):
        dog.show_details(self)
        print(self.color)
        
obj=mainclass("Tommy","black")
obj.show_details()