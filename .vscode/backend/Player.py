class Player:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def __str__(self):
        return self.firstName+" "+self.lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName 
