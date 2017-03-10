# -*- coding: utf-8 -*-
import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def text_reply(msg):
    print '*' * 10
    print msg
    print '*' * 10
    from_user_name = msg['FromUserName']
    to_user_name = msg['ToUserName']
    print msg['']
    print 'from :' + from_user_name
    print 'to :' + to_user_name
    print msg['Text']


@itchat.msg_register([TEXT,SHARING],isGroupChat=True)
def group_reply_text(msg):
    print '*' * 10
    print msg
    print '*' * 10
    from_user_name = msg['FromUserName']
    chat_room = itchat.search_chatrooms(userName=from_user_name)
    print chat_room['NickName'] if chat_room else ''
    to_user_name = msg['ToUserName']
    print 'from :' + from_user_name
    print 'to :' + to_user_name

    print msg['Content']



if __name__ == "__main__":
    print 'start'
    itchat.auto_login(hotReload=True)
    print 'playing'
    itchat.run()
    print 'end'

