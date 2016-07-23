#coding=utf-8
#2015/04/24
#author@alingse

from __future__ import print_function

from get_image import get_imgcontent 
from requests import Session
import argparse
import time
import os


def gen_session():
    session = Session()
    url = 'http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=corp'
    try:
        session.get(url,timeout=3)
        return session
    except Exception as e:
        pass
        print(e)


def download(savepath,count,content_type='jpg'):
    start = 10*count
    end = start + count + 1

    i = start
    session = gen_session()
    while i < end:

        content = get_imgcontent(session)
        if content == None:
            time.sleep(3)
            session = gen_session()
            continue
        f = open('{}/{}.{}'.format(savepath,i,content_type),'wb')
        f.write(content)
        f.close()
        print(i)
        i += 1
        time.sleep(0.7)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('savepath',nargs ='?',default = './raw_image',help='raw img save path')
    parser.add_argument('-c','--count',type=int,default=900)
    parser.add_argument('-t','--type',help='image type',default='jpg')
    parser.add_argument('--test',default=None,help='if use --test give savepath for test image') 
    args = parser.parse_args()
    if args.test:
        session = gen_session()
        content = get_imgcontent(session)
        if content != None:
            f = open(args.test,'wb')
            f.write(content)
            f.close()
        exit()

    savepath = os.path.abspath(args.savepath)
    count = args.count
    download(savepath,count)
