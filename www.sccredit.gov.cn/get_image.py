#coding=utf-8
#2015/04/24
#author@alingse

from __future__ import print_function

import requests
import argparse
import time
import os

query_url = 'http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=cmm'
yzm_url = 'http://www.sccredit.gov.cn/getYzm.do'

session = requests.Session()

headers = {
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6", 
    "Accept-Encoding": "gzip, deflate, sdch", 
    "Host": "www.sccredit.gov.cn", 
    "Accept": "image/webp,image/*,*/*;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36", 
    "Connection": "keep-alive",  
    "Pragma": "no-cache", 
    "Cache-Control": "no-cache", 
    "Referer": "http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=cmm"
}


def pre_visit(session):
    try:
        r = session.get(query_url, headers=headers, timeout=2)
        print(r.cookies)
    except Exception as e:
        pass
        print(e)


def get_imgcontent(pre=False):
    try:
        if pre:
            pre_visit(session)
        r = session.get(yzm_url, headers=headers, timeout=2)
        content =  r.content
        return content
    except Exception as e:
        pass
        print(e)


def main(savepath,count,pre=True,content_type='jpg'):
    start = 10*count
    end = start + count + 1
    for i in range(start,end):

        content = get_imgcontent(pre=pre)
        
        if content == None:
            time.sleep(3)
            pre = True
            pre_visit(session)
        else:
            pre = False
            f = open('{}/{}.{}'.format(savepath,i,content_type),'wb')
            f.write(content)
            f.close()
            print(i)
            time.sleep(0.7)

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('savepath',nargs ='?',default = './raw_image',help='raw img save path')
    parser.add_argument('-c','--count',type=int,default=900)
    parser.add_argument('-t','--type',help='image type',default='jpg')
    parser.add_argument('--test',default=None,help='if use --test give savepath for test image') 
    args = parser.parse_args()
    if args.test:
        content = get_imgcontent(pre=True)
        f = open(args.test,'wb')
        f.write(content)
        f.close()
        exit()

    savepath = args.savepath
    savepath = os.path.abspath(savepath)
    count = args.count

    main(savepath,count)
