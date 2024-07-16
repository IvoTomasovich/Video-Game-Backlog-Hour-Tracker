import requests
import pandas as pd
from bs4 import BeautifulSoup


headers =  { # used to all us to scrape site
    'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'
}


proceed = True

data = []  # stores the info we want to put in excel sheet

currentnum = 0  # used to loop through all 4 different times for the games

totalplaytimeMain = 0
totalplaytimeMainandSides = 0
totalplaytimeCompletionist = 0
totalplaytimeAllStyles = 0

while(proceed):
       CurrentGameName = input("Name of Current Game: ")

       currentpage = input("Please Provide the number at the end of the URL link so I can parse the data: ")

       url = "https://howlongtobeat.com/game/" + str(currentpage)  # currentpage number is the number at the end of each link


       response = requests.get(url, headers=headers)  # asks to get data from the site

       soup = BeautifulSoup(response.content, 'html.parser')  # used to set how we want to go through the site


       if soup.title.text == '404 Not Found': # if error, exit the loop
          proceed = False
       else:
          all_games = soup.find_all("li", class_="GameStats_short__tSJ6I time_100") # this is the specific chunk of data from each page we want
          DictOfGames = {'Game Name': CurrentGameName} # dict to store data
          for game in all_games: # loop through all 4 times
               # each loop has 5 components
               # 1) actually finding the hour string and only taking the numerical characters
               # 2) in case we hace any fraction strings, convert them to decimals
               # 3) convert the game time from string to float
               # 4) add 1 to current # so we can move on to next case, making this value 0 if we're on the last run
              if currentnum == 0:
                   gameinfo = game.find("h5").text.split(" ", 1)[0]
                   correctedgameinfo = gameinfo.replace('½', '.5').replace('¼', '.25').replace('¾', '.75')
                   DictOfGames['Main Story'] = float(correctedgameinfo)
                   totalplaytimeMain += float(correctedgameinfo)
                   currentnum += 1
              elif currentnum == 1:
                   gameinfo = game.find("h5").text.split(" ", 1)[0]
                   correctedgameinfo = gameinfo.replace('½', '.5').replace('¼', '.25').replace('¾', '.75')
                   DictOfGames['Main + Sides'] = float(correctedgameinfo)
                   totalplaytimeMainandSides += float(correctedgameinfo)
                   currentnum += 1
              elif currentnum == 2:
                   gameinfo = game.find("h5").text.split(" ", 1)[0]
                   correctedgameinfo = gameinfo.replace('½', '.5').replace('¼', '.25').replace('¾', '.75')
                   DictOfGames['Completionist'] = float(correctedgameinfo)
                   totalplaytimeCompletionist += float(correctedgameinfo)
                   currentnum += 1
              elif currentnum == 3:
                   gameinfo = game.find("h5").text.split(" ", 1)[0]
                   correctedgameinfo = gameinfo.replace('½', '.5').replace('¼', '.25').replace('¾', '.75')
                   DictOfGames['All Styles'] = float(correctedgameinfo)
                   totalplaytimeAllStyles += float(correctedgameinfo)
                   currentnum = 0
          data.append(DictOfGames) # add all this data at the end of the data array
          Continue = input(f'Continue? Type Y or N: ') # used if the user wants to continue
          if Continue == "Y":
            proceed = True
          elif Continue == "N": # if they don't want to, add the total times for all 4 characters
            proceed = False
            DictOfGames['Total Time Main'] = totalplaytimeMain
            DictOfGames['Total Time Main + Sides'] = totalplaytimeMainandSides
            DictOfGames['Total Time Completionist'] = totalplaytimeCompletionist
            DictOfGames['Total Time All Styles'] = totalplaytimeAllStyles
          else:
            Continue = input(f'Continue? Type Y or N: ')

# looks at the data and then sends it all to an excel file
df = pd.DataFrame(data)
df.to_excel("BackLog.xlsx", index=False)

