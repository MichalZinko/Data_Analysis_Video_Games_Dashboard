#importing libraries
from bs4 import BeautifulSoup
import requests
import csv

# loop that creates dictionary of csv file
# open csv file
with open('Video_games_missing_years.csv','r') as csv_file:
    content = csv.reader(csv_file)
    games_dictionary = {}
    #list_of_games_names = []
    #list_of_platforms = []
    for line in content:
        if line[0] != 'Name':
            if line[1] != 'Platform':
                games_dictionary[line[0].strip()] = line[1].strip() 
                #list_of_games_names.append(line[0].strip())
                #list_of_platforms.append(line[1].strip())

#for loop that creates urls from dictionary file
# getting games names 
for game_name in games_dictionary:
    game_platform = games_dictionary[game_name]
    url_game_name = game_name.replace(' ', '-').replace(':', '').replace('ii', '').lower()
    url = f'https://www.ign.com/games/{url_game_name}'
   
