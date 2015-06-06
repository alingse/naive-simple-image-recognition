#coding=utf-8
#2015/04/24
#author@shibin

#import urllib2
#import urllib

import requests
import time

Imgurl='http://www.inform.kz/captcha.jsp'

IMGPATH='./test_data/'

def get_imgdata():
    try:
        resp=requests.get(Imgurl)
        return resp.content
    except:
        return None
get_imgdata()
def main():
    for i in range(100,1000):
        imgdata=get_imgdata()
        if imgdata==None:
            time.sleep(3)
            continue
        f=open(IMGPATH+str(i)+'.jpg','w')
        f.write(imgdata)
        f.close()
        print i
        time.sleep(0.7)

if __name__ == '__main__':
    main()
