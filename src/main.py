import weibologin.weibologin as wl
import processbar.processbar as pb
import urllib.parse as up

URL='http://www.mob.com'

if __name__ == '__main__':
    c=wl.getClient()
    text=pb.GetText()
    print(text)
    text=text+URL
    #text=up.quote(text,safe='/',encoding=None,errors=None)+URL
    #print(text)
    ret=c.post('statuses/share',status=text)
    print(ret['text'])
