from bs4 import BeautifulSoup
import requests
import pandas as pd

dwarf_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
d_page = requests.get(dwarf_url)

d_soup = BeautifulSoup(d_page.text , "html.parser")

d_table = d_soup.find_all("table")

temp_list = []

table_rows = d_table[7].find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstip()for i in td]
    temp_list.append(row)

star_name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns= [ 'Star' , "Distance" , 'Mass' , 'Radius'])
print(df2)

df2.to_csv('brown_dwarfs.csv')
