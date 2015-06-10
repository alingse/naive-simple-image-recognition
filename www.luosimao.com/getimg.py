#coding=utf-8
#2015/04/24
#author@shibin

#import urllib2
#import urllib

import requests
import time

Imgurl='http://luosimao.com/captcha/?'
IMGPATH='./test_data/'

def get_imgdata():
    try:
        url=Imgurl+str(int(time.time())-400)+'000'
        print url
        resp=requests.get(url)
        return resp.content
    except:
        return None
#get_imgdata()
def main():
    for i in range(1000,2000):
        imgdata=get_imgdata()
        if imgdata==None:
            time.sleep(3)
            continue
        f=open(IMGPATH+str(i)+'.png','wb')
        f.write(imgdata)
        f.close()
        print i
        time.sleep(0.5)

if __name__ == '__main__':
    main()
