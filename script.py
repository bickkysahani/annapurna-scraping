import requests
import json


def annapurna_scrape(search_term):
    page_number = 1
    listItems = []
    url = f"https://bg.annapurnapost.com/api/search?title={search_term}&page={page_number}"
    # response = requests.get(url)
    response = requests.get(url)
    res = json.loads(response.text)
    # print(res)
    # with open('response.json', 'w') as f:
    #     json.dump(res, f, indent=4, ensure_ascii=False,
    #                separators=(',', ': '))
    total_articles = res['data']['total']
    totalPage = res['data']['totalPage']
    print("total articles :",total_articles)
    print("total pages :",totalPage)
    for i in range(1, totalPage+1):
        if page_number<=totalPage:
            print("current page : ",page_number)
            url = f"https://bg.annapurnapost.com/api/search?title={search_term}&page={page_number}"
            try:
                response = requests.get(url)
                res = json.loads(response.text)
                print("total articles in current page : ",res['data']['count'])
                print("articles count :", len(res['data']['items']))
                # print(type(res))
                with open('response.json', 'w') as f:
                    listItems.extend(res['data']['items'])
                    json.dump(listItems, f, indent=4, ensure_ascii=False,
                            separators=(',', ': '))

                # json.dump(res, f, indent=4, ensure_ascii=False,
                #             sort_keys=True, separators=(',', ': '))
                
            except Exception as e:
                print(e)
                print("error in page :",page_number)

            page_number += 1
        else:
            print('No more pages')
            break
        
    with open('response.json', 'r') as f:
        #read the json file
        data = json.load(f)
        print("Total articles saved :",len(data))

term = 'शेरबहादुर देउवा'
annapurna_scrape(term)

