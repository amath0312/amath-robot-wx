#!/usr/bin/env python3
#-*-coding:utf8-*-

from movie.spider import Spider as Movie
from wxpy import *

def start_robot():
    bot = Bot()

    master = bot.friends().search('槑')[0]
    # group = bot.groups().search('程序员及家属')[0]

    @bot.register()
    def reply_my_friend(msg):
        if msg.member == master and msg.text == ':movie':
            message_text = ''
            movies = Movie().news()
            for m in movies:
                message_text += str(m)
                message_text += '\r\n'*2
            return message_text
    bot.start()

def test_spider():
    movies = Movie().news()
    for m in movies:
        print(m)
        print('='*20)
    
if __name__ == '__main__':
    # test_spider()
    start_robot()