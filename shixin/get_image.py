#coding=utf-8
#author@shibin

import datetime
import time

now = lambda : time.strftime('%a %b %d %Y %H:%M:%S GMT 0800 (CST)',time.localtime())


headers = {
 "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6", 
 "Accept-Encoding": "gzip, deflate, sdch", 
 "Host": "shixin.court.gov.cn", 
 "Accept": "image/webp,image/*,*/*;q=0.8", 
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36", 
 "Connection": "keep-alive", 
 "Referer": "http://shixin.court.gov.cn/", 
 "Pragma": "no-cache", 
 "Cache-Control": "no-cache"
}

url = 'http://shixin.court.gov.cn/image.jsp'

def get_imgcontent(session):
    try:
        params = {
            'date':now()
            }
        r = session.get(url, params=params, timeout =2, headers=headers)
        content = r.content
        return content
    except Exception as e:
        pass
        print(e)


if __name__ == '__main__':
    pass