#-*- coding:utf8 -*-

import urllib.request
from movie.movie import Movie
from bs4 import BeautifulSoup

class Spider:
    url = 'http://pianyuan.net/'
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
                    #description
                    movie.src = Spider.url+ col.a['href']
                    movie.desc = col.text.strip()
                elif colno == 1:
                    movie.size = col.string
                elif colno == 2:
                    movie.update_time = col.string
            
            movies.append(movie)
        return movies
        
if __name__ == '__main__':
    s = Spider()
    movies = s.crawl()
    for m in movies:
        print(movie.src, m.update_time, m.size)