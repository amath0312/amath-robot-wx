#-*- coding:utf8 -*-

import urllib.request
from movie.movie import Movie
from bs4 import BeautifulSoup

class Spider:
    url = 'http://pianyuan.net'
    def __init__(self):
        pass

    def crawl(self):
        response = urllib.request.urlopen(Spider.url)
        html = response.read().decode('utf8')
        soup = BeautifulSoup(html,"html.parser")
        movie_table = soup.find_all("table",class_='data',limit=1)[0].tbody
        movies = []
        for lineno, row in enumerate(movie_table.find_all('tr')):
            if lineno == 0:
                #skip first line
                continue
            if lineno >10:
                break
            movie = Movie()
            for colno,col in enumerate(row.find_all('td')):
                if colno == 0:
                    # description
                    movie.src = Spider.url+ col.a['href']
                    movie.desc = col.text.strip()
                    self.fill_details(movie)
                elif colno == 1:
                    movie.size = col.string
                elif colno == 2:
                    movie.update_time = col.string
            
            movies.append(movie)
        return movies
        
    def fill_details(self,movie):
        detail_page = movie.src
        response = urllib.request.urlopen(detail_page)
        html = response.read().decode('utf8')
        soup = BeautifulSoup(html,"html.parser")
        
        name = soup.find_all('div',class_='col-sm-12 col-md-12 col-lg-12 text-left nopd')[0].h1.contents[0].strip()
        movie.name = name

        detail_ul = soup.find_all('ul',class_='detail')[0]
        detail_li = detail_ul.find_all('li',class_='clearfix')
        for li in detail_li:
            if li.strong:
                key = li.strong.text
                value = li.div.text.strip()
                if '地区' in key:
                    movie.area = value
                elif '类型' in key:
                    movie.style = value
                elif '导演' in key:
                    for director in li.div.find_all('a'):
                        movie.directors.append(director.text)
                elif '主演' in key:
                    for actor in li.div.find_all('a'):
                        movie.actors.append(actor.text)
                elif '编剧' in key:
                    for scenarist in li.div.find_all('a'):
                        movie.scenarists.append(scenarist.text)
        

if __name__ == '__main__':
    s = Spider()
    movies = s.crawl()
    for m in movies:
        print(movie.src, m.update_time, m.size)