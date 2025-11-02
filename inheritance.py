# inheritance.py
# this is the parent class
class PartyAnimal:
    def __init__(self, name):
        self.name = name
        self.x = 0

    def party(self):
        self.x += 1
        print(self.name, "party count:", self.x)
# this is the child class inheriting everything from the parent
class FootballFan(PartyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
# touchdown method adds 6 points then calls .party
    def touchdown(self):
        self.points += 6
        print(self.name, "scored! points =", self.points)
        self.party()

if __name__ == "__main__":
    s = PartyAnimal("Caprice")
    s.party()

    j = FootballFan("Art")
    j.party()
    j.touchdown()
