# coding=utf-8
from urllib import request
from urllib import parse
import time, _thread

def get_content(i):
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    #url = 'https://api.douban.com/v2/movie/search?q=%s'% (parse.quote('张艺谋'))
    try:
        d = request.urlopen(url).read()
        data.append(d)
    except Exception as e:
        print(e)
    print(i, time.time() - time_start)
    print('Data:', len(data))

time_start = time.time()
data = []

for i in range(30):
    print('Request movie:', i)
    _thread.start_new_thread(get_content, (i,))

while 1:
    pass
