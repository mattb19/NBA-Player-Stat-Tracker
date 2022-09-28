import requests
from bs4 import BeautifulSoup
from RegAvg import RegAvg
from CareerAvg import CareerAvg
from PostAvg import PostAvg

class WebScraper:
    def __init__(self, isGay=True):
        self.isGay = isGay

    def getTeam(self, name):
        
        #List of team roster URLs to check for player name
        URLs = ["http://www.espn.com/nba/teams/roster?team=Bos",
                "http://www.espn.com/nba/teams/roster?team=BKN",
                "http://www.espn.com/nba/teams/roster?team=NY",
                "http://www.espn.com/nba/teams/roster?team=Phi",
                "http://www.espn.com/nba/teams/roster?team=Tor",
                "http://www.espn.com/nba/teams/roster?team=Chi",
                "http://www.espn.com/nba/teams/roster?team=Cle",
                "http://www.espn.com/nba/teams/roster?team=Det",
                "http://www.espn.com/nba/teams/roster?team=Ind",
                "http://www.espn.com/nba/teams/roster?team=Mil",
                "http://www.espn.com/nba/teams/roster?team=Atl",
                "http://www.espn.com/nba/teams/roster?team=Cha",
                "http://www.espn.com/nba/teams/roster?team=Mia",
                "http://www.espn.com/nba/teams/roster?team=Orl",
                "http://www.espn.com/nba/teams/roster?team=WSH",
                "http://www.espn.com/nba/teams/roster?team=GS",
                "http://www.espn.com/nba/teams/roster?team=LAC",
                "http://www.espn.com/nba/teams/roster?team=LAL",
                "http://www.espn.com/nba/teams/roster?team=PHX",
                "http://www.espn.com/nba/teams/roster?team=Sac",
                "http://www.espn.com/nba/teams/roster?team=Dal",
                "http://www.espn.com/nba/teams/roster?team=Hou",
                "http://www.espn.com/nba/teams/roster?team=Mem",
                "http://www.espn.com/nba/teams/roster?team=NO",
                "http://www.espn.com/nba/teams/roster?team=SA",
                "http://www.espn.com/nba/teams/roster?team=Den",
                "http://www.espn.com/nba/teams/roster?team=Min",
                "http://www.espn.com/nba/teams/roster?team=Okc",
                "http://www.espn.com/nba/teams/roster?team=Por",
                "http://www.espn.com/nba/teams/roster?team=UTAH"]
        
        #If player's name is found, return the URL with individual data
        for URL in URLs:
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            player = soup.find('a', string = name)
            if player != None:
                playerurl = player.get('href')
                return playerurl


    def list2Dic(self, lst):
        
        #Converts raw data into dictionary
        dict = {"gp" : float(lst[0]), "min" : float(lst[1]), "fgpercent" : float(lst[2]), "threeptpercent" : float(lst[3]),
                "ftpercent" : float(lst[4]), "reb" : float(lst[5]), "ast" : float(lst[6]), "blk" : float(lst[7]),
                "stl" : float(lst[8]), "pf" : float(lst[9]),"to" : float(lst[10]), "pts" : float(lst[11])}
        return dict


    def retreiveData(self, URL):
        regseason = []
        postseason = []
        career = []
        player = ""

        #Gets player's individual data
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        sumStat = soup.find("table", class_ = "Table Table--align-right")
        data = sumStat.find_all("td", class_ = "Table__TD")
        bio = soup.find_all("ul", class_ = "PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap")

        #Checks to see what data is provided
        if len(data) > 24:
            for element in range(12):
                regseason.append(data[element].text)
            for element in range(12,24):
                postseason.append(data[element].text)
            for element in range(24,36):
                career.append(data[element].text)
            for element in range(len(bio)):
                player = bio[element].text
            Team = ''
            Number = '#'
            Pos = ''
            for i in player:
                if i != '#':
                    Team += i.lower()
                else:
                    break
            lst = [i for i in player if i.isdigit() == True]
            for i in lst:
                Number += i
            count = 0
            for i in player:
                if i == '#':
                    count += 1
                if count == 1 and i.isdigit() == False and i != "#":
                    Pos += i
            Team = Team.replace(' ', '')
            lst = [Team, Number, Pos]
            return [lst, regseason, career, postseason]
        if len(data) <= 24:
            for element in range(12):
                regseason.append(data[element].text)
            for element in range(12,24):
                career.append(data[element].text)
            for element in range(len(bio)):
                player = bio[element].text
            Team = ''
            Number = '#'
            Pos = ''
            for i in player:
                if i != '#':
                    Team += i.lower()
                else:
                    break
            lst = [i for i in player if i.isdigit() == True and i != "#"]
            for i in lst:
                Number += i
            count = 0
            for i in player:
                if i == '#':
                    count += 1
                if count == 1 and i.isdigit() == False:
                    Pos += i
            Team = Team.replace(' ', '')
            lst = [Team, Number, Pos]
            return [lst, regseason, career]
        if len(data) == 0:
            return None

    def getData(self, name):
        #Use this function to retrieve player data in format Team # Name, reg season stats, postseason(if provided) stats, career stats
        something = self.retreiveData(self.getTeam(name))
        FN = ""
        LN = ""
        count = 0
        for i in name:
            if i != ' ' and count == 0:
                FN += i
            elif i == ' ':
                count += 1
            elif count == 1:
                LN += i
        if len(something) == 3:
            PlayerReg = RegAvg(FN, LN, 0, something[0][1], something[0][0], something[0][2], something[1][0], something[1][1], 
            something[1][2], something[1][3], something[1][4], something[1][5], something[1][6], something[1][7], something[1][8], 
            something[1][9], something[1][10], something[1][11])
            PlayerCareer = CareerAvg(FN, LN, 0, something[0][1], something[0][0], something[0][2], something[2][0], something[2][1], 
            something[2][2], something[2][3], something[2][4], something[2][5], something[2][6], something[2][7], something[2][8], 
            something[2][9], something[2][10], something[2][11])
            return [PlayerReg, PlayerCareer]
        elif something == None:
            return "Player has no data"
        else:
            PlayerReg    =    RegAvg(FN, LN, 0, something[0][1], something[0][0], something[0][2], something[1][0], something[1][1], 
            something[1][2], something[1][3], something[1][4], something[1][5], something[1][6], something[1][7], something[1][8], 
            something[1][9], something[1][10], something[1][11])
            PlayerCareer = CareerAvg(FN, LN, 0, something[0][1], something[0][0], something[0][2], something[2][0], something[2][1], 
            something[2][2], something[2][3], something[2][4], something[2][5], something[2][6], something[2][7], something[2][8], 
            something[2][9], something[2][10], something[2][11])
            PlayerPost = PostAvg(FN, LN, 0, something[0][1], something[0][0], something[0][2], something[3][0], something[3][1], 
            something[3][2], something[3][3], something[3][4], something[3][5], something[3][6], something[3][7], something[3][8], 
            something[3][9], something[3][10], something[3][11])
            return [PlayerReg, PlayerCareer, PlayerPost]

