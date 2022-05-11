import requests
import json


def annapurna_scrape(search_term):
    page_number = 1
    listItems = []
    articles_count = 0
    while True:
        print("current page : ",page_number)
        try: 
            with open('response3.json', 'r') as f:
                listItems = json.load(f)
                for item in listItems:
                 #print(item)
                 for k,v in item.items():
                     if k == 'page_number':
                         #print(k)
                         if item[k] == page_number:
                            print("page number ", page_number , "data already exists")
                            #print(page_number)
                            page_number += 1
                            print("current page : ",page_number)
                            break
                    
                     else:
                        pass
                    
        except:
            print("No file found")
            print("Creating new file")
        
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
        articles_count += res['data']['count']
        print("total articles : ",res['data']['total'])
        print("articles count in current page:", res['data']['count'])
        # print(type(res))
     
        #listItems.append({'page_number': page_number, 'data': res['data']['items']})
        dataItems = {'page_number': page_number, 'data': res['data']['items']}
        listItems.append(dataItems)

        with open('response3.json', 'w') as f:
            json.dump(listItems, f, indent=4, ensure_ascii=False,
                             separators=(',', ': '))
       
        print("Total articles saved :", articles_count)   
        print("----------------------------")
        

        page_number += 1

        if page_number > totalPage:
            print("No more pages")
            break
        
  
       

term = 'शेरबहादुर देउवा'
annapurna_scrape(term)
