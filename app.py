#!/usr/bin/env python3
#-*-coding:utf8-*-

from movie.spider import Spider as Movie
from wxpy import *
if __name__ == '__main__':
    masters=['8281467162@chatroom']
    bot = Bot()

    group = bot.groups().search('家属深圳三缺一')[0]
    print(group)
    @bot.register()
    def reply_my_friend(msg):
        if msg.sender.wxid in masters and msg.text == ':movie':
            message_text = ''
            movies = Movie().news()
            for m in movies:
                message_text += str(m)
                message_text += '\r\n'*2
            return message_text
    bot.start()
    # movies = Movie().news()
    # for m in movies:
    #     print(m)
    #     print('='*20)