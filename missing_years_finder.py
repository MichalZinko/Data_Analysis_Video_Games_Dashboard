#importing libraries
from bs4 import BeautifulSoup
import requests
import csv

# loop that creates list of csv file
# open csv file
with open('Missing_years.csv','r') as csv_file:
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
    url_game_name = game_name.lower().replace(' ', '-').replace(':', '').replace('.', '').replace("'", '').replace('!', '').replace('/', '').replace('fifa-soccer', 'fifa')
    url = f'https://rawg.io/games/{url_game_name}'
#Screping the page
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    info = soup.find('div', class_ = "game__meta-text", itemprop="datePublished")
#checking if data exists and adding, to the csv file N/A if not and year if it exists 
    if info == None:
        game_row_data= [[game_name, 'N/A']]
        file = open('video_games_years.csv', 'a', newline='')
        writer = csv.writer(file)
        writer.writerows(game_row_data)
        file.close()
    else:
        count_done += 1
        date_release = info.text
        lenght_of_date = len(date_release)
        year = date_release[lenght_of_date-4::]
        game_row_data= [[game_name, year]]
        file = open('video_games_years.csv', 'a', newline='')
        writer = csv.writer(file)
        writer.writerows(game_row_data)
        file.close()
#counter of succes rate
    count += 1
    succes_rate = count_done/count * 100
print(f'\n{round(succes_rate,2)}% of data was sucesfully found')
