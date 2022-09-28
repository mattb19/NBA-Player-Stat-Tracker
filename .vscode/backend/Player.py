class Player:
    def __init__(self, firstName, lastName, age, number, team):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.number = number
        self.team = team
    
    def __str__(self):
        return self.firstName+" "+self.lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName 
    
    def getAge(self):
        return str(self.age)
    
    def getNumber(self):
        return '#'+str(self.number)
    
    def getTeam(self):
        return str(self.team)


