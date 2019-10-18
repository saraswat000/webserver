import requests
import json
url = 'https://api.github.com/repos/releax/automate/commits?page=1&amp;per_page=2&amp;callback=voidcommits&amp;sha=master'
r = requests.get(url=url)

data = r.text.replace('/**/voidcommits(','')
data = data[:len(data)-1] 
print(json.dumps(data))