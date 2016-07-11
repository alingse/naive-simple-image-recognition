#coding=utf-8
#author@shibin
#2015.09.22

import requests
import time
import sys
import os

img_url="http://www.k369.com/em/Foreground/Image.aspx"
def down_k369(url):
    try:
        resp=requests.get(url,timeout=1)
        return resp.content
    except:
        pass
def main(download_dir,pic_ct,pic_type='.gif'):    
    i_start=int('10'+str(pic_ct))
    while pic_ct>0:
        img_data=down_k369(img_url)
        if img_data==None:
            continue
        if img_data=="":
            continue
        fpath=download_dir+str(i_start)+pic_type
        f=open(fpath,'wb')
        f.write(img_data)
        f.close()
        i_start-=1
        pic_ct-=1





if __name__ == '__main__':
    download_dir=sys.argv[1]
    pic_ct=400
    try:
        pic_ct=int(sys.argv[2])
    except:
        pass
    main(download_dir,pic_ct)