import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
        'Accept': "*/*",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'keep-alive',
        'Origin': 'https://maoyan.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Cookie': 'uuid_n_v=v1; uuid=2BD4FD20B93711EAB7FDDF490BC946C0B5FBF19577FF42A8A1138D6A9C3F37F9; _csrf=84e72b01db0937cd96c0ea1bd7b09b66a6968d6f795a96719527d2a343ec5f77; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593345719; _lxsdk_cuid=172face3c536a-09d4b4fa6287c7-f7d123e-1fa400-172face3c54c8; _lxsdk=2BD4FD20B93711EAB7FDDF490BC946C0B5FBF19577FF42A8A1138D6A9C3F37F9; mojo-uuid=3efc0172bdfa87241f3d3ecd2c2daac7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593351879; __mta=142569997.1593345719580.1593351851224.1593351879227.4; _lxsdk_s=172fb47fd26-2f6-287-814%7C%7C1'
         }

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
print(response.status_code)
bs_info = bs(response.text, 'html.parser')

movies_list = []

for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'})[:10]:

    for item in tags.find_all('div',attrs={'class':'movie-hover-info'}):

        movies_name = item.find('span',attrs={'class':'name'}).text
        content = item.find_all('span',attrs={'class':'hover-tag'})
        movie_type = content[0].next_sibling.strip()
        release_time = content[2].next_sibling.strip()

        movies_list.append([movies_name,movie_type,release_time])

movies = pd.DataFrame(data=movies_list,columns=['电影名称','电影类型','上映时间'])

print(movies)

movies.to_csv('./movielist.csv', encoding='utf8', index=False, header=False)