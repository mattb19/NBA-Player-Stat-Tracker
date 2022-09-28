from Player import *
from PostAvg import *
from CareerAvg import *
from RegAvg import *

class PlayerList:
    def __init__(self):
        self.playerList = []
    
    def setPlayerList(self, listOfPlayers):
        self.playerList = [i for i in listOfPlayers]
    
    def getPlayerList(self):
        playerList = []
        for i in self.playerList:
            player = {
                'team':'',
                'player':str(i),
                'age':str(i.getAge()),
                'number':i.getNumber(),
                'gp':i.getGP(),
                'min':str(i.getMin()),
                'fgpercent':i.getFgPercent(),
                'threeptpercent':i.getThreePtPercent(),
                'ftpercent':i.getFtPercent(),
                'reb':i.getREB(),
                'ast':i.getAST(),
                'blk':i.getBLK(),
                'stl':i.getSTL(),
                'pf':i.getPF(),
                'to':i.getTO(),
                'pts':i.getPTS()
            }
            playerList.append(player)
        return playerList
