from Player import Player

class PostAvg(Player):
    def __init__(self, firstName, lastName, age, number, team, pos, GP, minu, fgPercent, threePtPercent, FTPercent, REB, AST, BLK, STL, PF, TO, PTS):
        self.GP = GP
        self.min = minu
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
        Player.__init__(self, firstName, lastName, age, number, team, pos)

    def getGP(self):
        return str(self.GP)

    def getMin(self):
        return str(self.min)

    def getFgPercent(self):
        return str(self.fgPercent)+'%'

    def getThreePtPercent(self):
        return str(self.threePtPercent)+'%'

    def getFtPercent(self):
        return str(self.FTPercent)+'%'

    def getREB(self):
        return str(self.REB)

    def getAST(self):
        return str(self.AST)

    def getBLK(self):
        return str(self.BLK)

    def getSTL(self):
        return str(self.STL)

    def getPF(self):
        return str(self.PF)

    def getTO(self):
        return str(self.TO)

    def getPTS(self):
        return str(self.PTS)