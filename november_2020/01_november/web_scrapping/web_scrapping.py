import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import re

r = requests.get("https://www.peakbagger.com/list.aspx?lid=5651")
c= r.content
soup= BeautifulSoup(c, "html.parser")
mytable= soup.find_all("table", {"class":"gray"})
print(len(mytable))
# Lets go ahead and scrape first table with HTML code gdp[0]
table1 = mytable[0]
# the head will form our column names
body = table1.find_all("tr")
# Head values (Column names) are the first items of the body list
head = body[0] # 0th item is the header row
body_rows = body[1:] # All other items becomes the rest of the rows
print(len(body_rows))
headings = []
for item in head.find_all("th"): # loop through all th elements
    # convert the th elements to text and strip "\n"
    item = (item.text).rstrip("\n")
    # append the clean column name to headings
    headings.append(item)
print(headings)
#
table_to_get_link= soup.find("table", {"class":"gray"})
link_of_peak= table_to_get_link.findAll("a")
del link_of_peak[0:7]
del link_of_peak[1::2]

links= []
for link in link_of_peak:
    links.append(link.get("href"))
    

for index in range(len(links)-1):
    
    lat_long_url= requests.get(f"https://www.peakbagger.com/{links[index]}")
    lat_long_c= lat_long_url.content
    soup= BeautifulSoup(lat_long_c, "html.parser")
    lat_long_mytable= soup.find_all("table", {"class":"gray"})
    table2 = lat_long_mytable[0]
    # the head will form our column names
    body = table2.find_all("td")
    try:
        lat_long_full_string= body[7].contents

        print(lat_long_full_string)
        lat_string= (lat_long_full_string[1])
        long_string= (lat_long_full_string[2]).replace(" (Dec Deg)","")
    except:
        pass
print(lat_string, long_string)
##df_link = pd.DataFrame(links,columns=['url'])
##print(df_link.head())
# Next is now to loop though the rest of the rows

#print(body_rows[0])
all_rows = [] # will be a list for list for all rows
for row_num in range(len(body_rows)): # A row at a time
    row = [] # this will old entries for one row
    for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        # row_item.text removes the tags from the entries
        # the following regex is to remove \xa0 and \n and comma from row_item.text
        # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        #append aa to row - note one row entry is being appended
        row.append(aa)
    # append one row to all_rows
    all_rows.append(row)
# We can now use the data on all_rowsa and headings to make a table
# all_rows becomes our data and headings the column names
del all_rows[0]
df = pd.DataFrame(data=all_rows,columns=headings)

df.drop(df.iloc[:, 4:], inplace = True, axis = 1)
df["url"]= links
print(df.columns)
df.to_excel("mountain.xlsx")
