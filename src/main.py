import weibologin.weibologin as wl
import processbar.processbar as pb
import urllib.parse as up

URL='http://www.mob.com'

if __name__ == '__main__':
    c=wl.getClient()
    text=pb.GetText() # 获取年度余额文字和图形
    print(text)
    text=text+URL
    #text=up.quote(text,safe='/',encoding=None,errors=None)+URL
    #print(text)
    ret=c.post('statuses/share',status=text) # 发布微博
    print(ret['text'])
