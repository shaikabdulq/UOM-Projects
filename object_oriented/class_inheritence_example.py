# Extends the class_object_example.py script by adding a 'FootballFan' 
# class that inherits from 'PartyAnimal' class. It includes additional 
# functionality specific to a football fan, such as a method that
# keeps track of points (i.e. touchdown()).


class PartyAnimal():
    x = 0
    name = ''
    def __init__(self,y):
        self.name = y
        print(self.name,'is constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,self.x)

class FootballFan(PartyAnimal):
    point = 0
    def touchdown(self):
        self.point = self.point + 7
        self.party()
        print(self.name,'points',self.point )

a = PartyAnimal('Anil')
a.party()
a.party()

b = FootballFan('Bhuvan')
b.party()
b.touchdown()
b.party()
