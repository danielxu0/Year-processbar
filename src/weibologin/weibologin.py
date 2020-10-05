from weibo import Client

# 需要修改
APP_KEY=''
APP_SECRET=''
APP_URL=''
WEIBO_USER=''
WEIBO_PW=''

# 获取client对象
def getClient():
    c = Client(APP_KEY,APP_SECRET,APP_URL,username=WEIBO_USER,password=WEIBO_PW)
    return c

if __name__ == '__main__':
    c=getClient()
    # 使用statuses/share接口发文，必须包含 安全域名（自己没有可以用别人的网站，PS：www.baidu.com 亲测不可用）
    text='测试：每天自动发一条推文!!!\n' + 'http://www.mob.com'
    c.post('statuses/share', status=text)

