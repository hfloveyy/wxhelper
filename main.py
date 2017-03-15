# -*- coding: utf-8 -*-
import itchat
from itchat.content import *
from Si import Si


CHATROOM_NAME = u'测试群'
MYNAME = u'S'

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
    chat_room = itchat.search_chatrooms(userName=from_user_name)
    #获取群名称
    chat_room_name =  chat_room['NickName'] if chat_room else 'wrong'
    print chat_room_name
    if CHATROOM_NAME in chat_room_name:
        s.handleMsg(msg['Content'],from_user_name)
        s.print_dict()
    print msg['Content']



if __name__ == "__main__":
    print 'start'
    s = Si()
    itchat.auto_login(hotReload=True)
    print 'playing'
    itchat.run()
    print 'end'

