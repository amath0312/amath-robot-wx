class Movie(object):
    def __init__(self):
        self.name = ''
        self.src = ''
        self.update_time=''
        self.score = ''
        self.style = ''
        self.desc = ''
        self.size = ''

    def __str__(self):
        str = '';
        str += '名称：'+self.name+'\r\n'
        str += '链接：'+self.src+'\r\n'
        str += '评分：'+self.score+'\r\n'
        str += '类型：'+self.style+'\r\n'
        str += '更新时间：'+self.update_time+'\r\n'
        str += '大小：'+self.size+'\r\n'
        str += '摘要：'+self.desc

        return str
