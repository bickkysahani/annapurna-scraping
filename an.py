import requests
import json


def annapurna_scrape(search_term):
    page_number = 1
    #listItems = []
    # articles_count = 0
    try: 
        with open(f"{search_term}.json", 'r') as f:
            data = json.load(f)
            page_number = data['page']
    except:
        data = {"page": 1, "articles": []}
        
    while True:
        # print("current page : ",page_number)
        url = f"https://bg.annapurnapost.com/api/search?title={search_term}&page={page_number}"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if response.status_code == 200:
            res = json.loads(response.text)
        else:
            raise SystemExit(f"Error: {response.status_code}")
            

        totalPage = res['data']['totalPage']
        total_articles = res['data']['total']
        # articles_count += res['data']['count']
        print("total articles : ",res['data']['total'])
        # print("articles count in current page:", res['data']['count'])
        # print(type(res))
     
        #listItems.append({'page_number': page_number, 'data': res['data']['items']})
        # dataItems = {'page': page_number, 'articles': res['data']['items']}
        # listItems.append(dataItems)
        
        data['articles'].extend(res['data']['items'])
        data['page'] += 1

        with open(f"{search_term}.json", 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False,
                             separators=(',', ': '))
       
        print("Total articles saved :", len(data['articles']))   
        # print("----------------------------")
        

        page_number += 1

        if page_number > totalPage:
            print("No more pages")
            break
        
  
       

term = 'शेरबहादुर'
annapurna_scrape(term)
