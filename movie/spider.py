#-*-coding:utf8-*-

import movie.pianyuan


class Spider():
    def __init__(self):
        pass
    
    def news(self):
        new_movies = []
        new_movies.extend( movie.pianyuan.spider.Spider().crawl() )
        return new_movies

