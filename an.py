import requests
import json


def annapurna_scrape(search_term):
    page_number = 1
    listItems = []
    while True:
        print("current page : ",page_number)
        url = f"https://bg.annapurnapost.com/api/search?title={search_term}&page={page_number}"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if response.status_code == 200:
            res = json.loads(response.text)
        else:
            #raise SystemExit(f"Error: {response.status_code}")
            print("error in page number : ",page_number)
            page_number += 1
            continue
        #res = json.loads(response.text)

        total_articles = res['data']['total']
        print("total articles : ",res['data']['total'])
        print("articles count in current page:", res['data']['count'])
        # print(type(res))
        with open('response2.json', 'w') as f:
            listItems.extend(res['data']['items'])
            json.dump(listItems, f, indent=4, ensure_ascii=False,
                            separators=(',', ': '))
    
        print("Total articles saved :",len(listItems))   

        if len(listItems) == total_articles:
            print("No more pages")
            break

        page_number += 1
  
        

term = 'शेरबहादुर देउवा'
annapurna_scrape(term)

