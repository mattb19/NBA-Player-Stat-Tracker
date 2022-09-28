from Player import Player

class PostAvg(Player):
    def __init__(self, firstName, lastName, age, number, GP, min, fgPercent, threePtPercent, FTPercent, REB, AST, BLK, STL, PF, TO, PTS):
        self.GP = GP
        self.min = min
        self.fgPercent = fgPercent
        self.threePtPercent = threePtPercent
        self.FTPercent = FTPercent
        self.REB = REB
        self.AST = AST
        self.BLK = BLK
        self.STL = STL
        self.PF = PF
        self.TO = TO
        self.PTS = PTS
        Player.__init__(self, firstName, lastName, age, number)
    
    def getGP(self):
        return self.GP

    def getMin(self):
        return self.min

    def getFgPercent(self):
        return self.fgPercent

    def getThreePtPercent(self):
        return self.threePtPercent
    
    def getFtPercent(self):
        return self.FTPercent

    def getREB(self):
        return self.REB

    def getAST(self):
        return self.AST

    def getBLK(self):
        return self.BLK

    def getSTL(self):
        return self.STL

    def getPF(self):
        return self.PF

    def getTO(self):
        return self.TO
    
    def getPTS(self):
        return self.PTS

