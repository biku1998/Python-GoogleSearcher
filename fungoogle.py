# importing lib needed.
import requests , sys , webbrowser , bs4

# getting the request
res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))

print(sys.argv)
# raise a status

res.raise_for_status()

# making soup 
soup = bs4.BeautifulSoup(res.text,"html.parser")

linkElements = soup.select('.r a')

linksToOpen = min(5,len(linkElements))

for i in range(linksToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))

