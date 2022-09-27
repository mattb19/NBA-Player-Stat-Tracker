class Player:
    def __init__(self, firstName, lastName, season):
        self.firstName = firstName
        self.lastName = lastName
        self.season = season
    
    def __str__(self):
        return self.firstName+" "+self.lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName 
    
    def getSeason(self):
        return self.season
