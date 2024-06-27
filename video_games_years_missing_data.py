#importing libraries
from bs4 import BeautifulSoup
import requests
import csv

# loop that creates dictionary of csv file
# open csv file
with open('Video_games_missing_years_test.csv','r') as csv_file:
    content = csv.reader(csv_file)
    games_dictionary = {}
    list_of_games_names = []
    list_of_platforms = []
    for line in content:
        if line[0] != 'Name':
            if line[1] != 'Platform':
                games_dictionary[line[0].strip()] = line[1].strip() 
                list_of_games_names.append(line[0].strip())
                list_of_platforms.append(line[1].strip())
#for loop that creates urls from dictionary file

# getting games names 
count_done = 0
count = 0
for game_name in list_of_games_names:
    game_platform = games_dictionary[game_name]
    url_game_name = game_name.lower().replace(' ', '-').replace(':', '').replace('.', '').replace('ii', '').replace("'", '').replace('!', '').replace('fifa-soccer', 'fifa')
    url = f'https://rawg.io/games/{url_game_name}'
    print(f'\n{url}')
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    infos = soup.find_all('div', class_ = "game__meta-text", itemprop="datePublished")
    for info in infos: 
        if info == None:
            print('N/A')
        else:
            date_release = info.text
            lenght_of_date = len(date_release)
            year = date_release[lenght_of_date-4::]
            print(year)
            count_done += 1
        count += 1
print(count_done, count)