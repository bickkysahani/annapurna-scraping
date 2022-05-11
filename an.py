import requests
import json


def annapurna_scrape(search_term):
    page_number = 1
    listItems = []
    while True:
        print("current page : ",page_number)
        url = f"https://bg.annapurnapost.com/api/search?title={search_term}&page={page_number}"
        response = requests.get(url)
        res = json.loads(response.text)
        total_articles = res['data']['total']
        print("total articles : ",res['data']['total'])
        print("articles count in current page:", res['data']['count'])
        # print(type(res))
        with open('response2.json', 'w') as f:
            listItems.extend(res['data']['items'])
            json.dump(listItems, f, indent=4, ensure_ascii=False,
                            separators=(',', ': '))
                
        with open('response2.json', 'r') as f:
            #read the json file
            data = json.load(f)
            print("Total articles saved :",len(data))
            saved_articles = len(data)
            
        if saved_articles == total_articles:
            print("No more pages")
            break

        page_number += 1
  
        

term = 'शेरबहादुर देउवा'
annapurna_scrape(term)

