from Player import *

from ftplib import FTP
from Player import *

class RegAvg(Player):
    def __init__(self, fg, fgPercent, threePt, threePtPercent, FT, FTPercent, OR, DR, REB, AST, BLK, STL, PF, TO, PTS):
        self.fg = fg
        self.fgPercent = fgPercent
        self.threePt = threePt
        self.threePtPercent = threePtPercent
        self.FT = FT
        self.FTPercent = FTPercent
        self.OR = OR
        self.DR = DR
        self.REB = REB
        self.AST = AST
        self.BLK = BLK
        self.STL = STL
        self.PF = PF
        self.TO = TO
        self.PTS = PTS

    def getFg(self):
        return self.fg

    def getFgPercent(self):
        return self.fgPercent

    def getThreePt(self):
        return self.threePt

    def getThreePtPercent(self):
        return self.threePtPercent

    def getFt(self):
        return self.FT
    
    def getFtPercent(self):
        return self.FTPercent

    def getOR(self):
        return self.OR

    def getDR(self):
        return self.DR

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