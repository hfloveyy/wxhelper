import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def text_reply(msg):
    from_user_name = msg['FromUserName']
    to_user_name = msg['ToUserName']
    print 'from :' + from_user_name
    print 'to :' + to_user_name
    print msg['Text']

@itchat.msg_register([TEXT,SHARING],isGroupChat=True)
def group_reply_text(msg):
    from_user_name = msg['FromUserName']
    to_user_name = msg['ToUserName']
    actual_nick_name = msg['ActualNickName']
    print 'nickname :' + actual_nick_name
    print 'from :' + from_user_name
    print 'to :' + to_user_name

    print msg['Content']


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()