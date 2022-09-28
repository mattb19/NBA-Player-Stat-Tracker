class Player:
    def __init__(self, firstName, lastName, age=0, number=0, team="", pos=""):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.number = number
        self.team = team
        self.pos = pos
    
    def __str__(self):
        return self.firstName+" "+self.lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName 
    
    def getAge(self):
        return str(self.age)
    
    def getNumber(self):
        return str(self.number)
    
    def getTeam(self):
        return str(self.team)
    
    def getPos(self):
        return str(self.pos)


