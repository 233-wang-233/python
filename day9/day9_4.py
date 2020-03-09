import requests
import json
def main():
    resp = requests.get('http://api.tianapi.com/bulletin/index?key=401cea86b3572811a4a64c46797fa4cb')
    data_model=json.loads(resp.text)
    # print(data_model['msg'])

    for news in data_model['newslist']:
        print(news['title'])
if __name__ == '__main__':
    main()