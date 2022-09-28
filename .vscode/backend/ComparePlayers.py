from Player import *
from PostAvg import *
from CareerAvg import *
from RegAvg import *

class Comparison:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def getComparison(self):
        return [
            {
                'team':self.player1.getTeam(),
                'player':str(self.player1),
                'age':str(self.player1.getAge()),
                'number':self.player1.getNumber(),
                'gp':self.player1.getGP(),
                'min':str(self.player1.getMin()),
                'fgpercent':self.player1.getFgPercent(),
                'threeptpercent':self.player1.getThreePtPercent(),
                'ftpercent':self.player1.getFtPercent(),
                'reb':self.player1.getREB(),
                'ast':self.player1.getAST(),
                'blk':self.player1.getBLK(),
                'stl':self.player1.getSTL(),
                'pf':self.player1.getPF(),
                'to':self.player1.getTO(),
                'pts':self.player1.getPTS()
            },
            {
                'team':self.player2.getTeam(),
                'player':str(self.player2),
                'age':str(self.player2.getAge()),
                'number':self.player2.getNumber(),
                'gp':self.player2.getGP(),
                'min':str(self.player2.getMin()),
                'fgpercent':self.player2.getFgPercent(),
                'threeptpercent':self.player2.getThreePtPercent(),
                'ftpercent':self.player2.getFtPercent(),
                'reb':self.player2.getREB(),
                'ast':self.player2.getAST(),
                'blk':self.player2.getBLK(),
                'stl':self.player2.getSTL(),
                'pf':self.player2.getPF(),
                'to':self.player2.getTO(),
                'pts':self.player2.getPTS()
            }
        ]