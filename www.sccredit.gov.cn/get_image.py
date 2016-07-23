#coding=utf-8
#author@alingse



url = 'http://www.sccredit.gov.cn/getYzm.do'

headers = {
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6", 
    "Accept-Encoding": "gzip, deflate, sdch", 
    "Host": "www.sccredit.gov.cn", 
    "Accept": "image/webp,image/*,*/*;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36", 
    "Connection": "keep-alive", 
    "Pragma": "no-cache", 
    "Cache-Control": "no-cache", 
    "Referer": "http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=corp"
}


def get_imgcontent(session):
    try:
        r = session.get(url,headers=headers,timeout=3)
        print(r.headers)
        content = r.content
        return content
    except Exception as e:
        pass
        print(e)


if __name__ == '__main__':
    pass