import requests
import json

search_title = 'शेरबहादुर देउवा'
try:
    with open(f"{search_title}.json") as f:
        data = json.load(f)
except:
    data = {"page": 1, "articles": []}

for page in range(data['page'], 4):
    url = f"https://bg.annapurnapost.com/api/search?title={search_title}&page={page}"
    response = requests.get(url)
    articles = response.json()['data']['items']
    data['articles'].extend(articles)
    data['page'] += 1
    with open(f"{search_title}.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)