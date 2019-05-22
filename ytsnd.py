from bs4 import BeautifulSoup
import requests
import os

# Search is "This is a search"
# https://www.youtube.com/results?search_query=this+is+a+search

youtuberl = 'https://www.youtube.com/results?search_query='
base = "https://www.youtube.com"
search_param = input("Song Name: ")
search_param = search_param.replace(" ", "+")

geturl = youtuberl + search_param
print(geturl)
response = requests.get(geturl)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

links = soup.find_all('a')

stufflist = []

def isvideo(x):
    if 'watch' in x.get('href'):
        return True
    else:
        return False


for link in soup.find_all('a'):
    if 'watch' in link.get('href') and link.has_attr('title'):
        stufflist.append(link)



def printoptions():
    print("Here are your options \n")
    x = 0
    for link in stufflist:
        print(str(x) + " " + link.get('title'))
        x+= 1
    return input("Enter selection \n")




def mainloop():
    while True:
        x = printoptions()
        while len(x) != 1 and len(x) != 2:
            x = printoptions()
        break
    return base + stufflist[int(x)].get('href')


printoptions()

final = "py -m youtube_dl -x --audio-format \"mp3\" " + mainloop()
print(final)

os.system(final)
