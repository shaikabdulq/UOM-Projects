# Defines a 'PartyAnimal' class, includes methods to increment a counter
# each time the attendee parties (i.e. party()) and a destructor that 
# prints a message when an object is destroyed.

class PartyAnimal():
    x = 0
    name = ''
    def __init__(self,y):
        self.name = y
        print(self.name,'is constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,self.x)
    def __del__(self):
        print(self.name,'is destroyed',self.x)
a = PartyAnimal('Anil')
a.party()
a.party()
a=50
b = PartyAnimal('Bhuvan')
b.party()
b.party()
b.party()
b=20