#importing libraries
from bs4 import BeautifulSoup
import requests
import csv

# loop that creates dictionary of csv file
# open csv file
with open('Video_games_missing_years.csv','r') as csv_file:
    content = csv.reader(csv_file)
    list_of_games_names = []
    for line in content:
        if line[0] != 'Name':
            if line[1] != 'Platform':
                list_of_games_names.append(line[0].strip())
#for loop that creates urls from dictionary file

# getting games names 
count_done = 0
count = 0
for game_name in list_of_games_names:
    game_platform = games_dictionary[game_name]
    url_game_name = game_name.lower().replace(' ', '-').replace(':', '').replace('.', '').replace("'", '').replace('!', '').replace('/', '').replace('fifa-soccer', 'fifa')
    url = f'https://rawg.io/games/{url_game_name}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    info = soup.find('div', class_ = "game__meta-text", itemprop="datePublished")
    if info == None:
        print(game_name, 'N/A')
    else:
        count_done += 1
        date_release = info.text
        lenght_of_date = len(date_release)
        year = date_release[lenght_of_date-4::]
    count += 1
print(count_done/count * 100%)