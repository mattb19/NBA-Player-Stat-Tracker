import requests
from bs4 import BeautifulSoup
def getTeam(name):
    
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


def list2Dic(lst):
    
    #Converts raw data into dictionary
    dict = {"gp" : float(lst[0]), "min" : float(lst[1]), "fgpercent" : float(lst[2]), "threeptpercent" : float(lst[3]),
            "ftpercent" : float(lst[4]), "reb" : float(lst[5]), "ast" : float(lst[6]), "blk" : float(lst[7]),
            "stl" : float(lst[8]), "pf" : float(lst[9]),"to" : float(lst[10]), "pts" : float(lst[11])}
    return dict


def retreiveData(URL):
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
        return player, list2Dic(regseason), list2Dic(postseason), list2Dic(career)
    if len(data) <= 24:
        for element in range(12):
            regseason.append(data[element].text)
        for element in range(12,24):
            career.append(data[element].text)
        for element in range(len(bio)):
            player = bio[element].text
        return player, list2Dic(regseason), list2Dic(career)
    if len(data) == 0:
        return 'Player has no data'


#Use this function to retrieve player data in format Team # Name, reg season stats, postseason(if provided) stats, career stats
print(retreiveData(getTeam("Malcolm Brogdon")))
