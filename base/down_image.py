# coding=utf-8
# author@alingse

from requests import Session

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


def gen_session():
    session = Session()
    url = 'http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=corp'
    try:
        session.get(url, timeout=3)
        return session
    except Exception:
        pass


def get_img(session=None, **kwargs):
    if not session:
        session = gen_session()

    try:
        if 'headers' not in kwargs:
            kwargs['headers'] = headers
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 3

        r = session.get(url, **kwargs)
        return r.content
    except Exception:
        pass
