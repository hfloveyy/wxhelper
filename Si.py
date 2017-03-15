# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import itchat

ORDERS = ['发通知','还有谁','结束']
MEMBERS = ['我','你','他']
class Si:
    def __init__(self):
        print 'i am Si！'
        self.content = None
        self.fun = None
        self.msglist = []
        self.allready = []
        self.notyet = []
        self.msgdict = {'msg': self.msglist}
        self.flag = False
        self.reply = None
    def handleMsg(self,content,from_user_name):
        self.content = content.encode('utf-8')
        self.fun = from_user_name
        order = self.content[2:12].strip()
        if self.flag:
            self.msglist.append(self.content)
            if self.content in MEMBERS:
                self.allready.append(self.content)
        if order in ORDERS:

            self.handleOrder(order)

        if not self.notyet and set(self.allready)==set(MEMBERS):
            itchat.send('%s' % self.reply, self.fun)
            self.end()
            itchat.send('全部签到,结束通知', self.fun)

    def handleOrder(self,order):
        if order in '发通知':
            print 'i 发通知'
            self.flag = True
            self.msglist.append(self.content[12:])
            itchat.send(self.content[12:], self.fun)
        elif order in '还有谁':
            print '还有谁'
            self.notyet = list(set(MEMBERS)-set(self.allready))

            itchat.send('%s' % self.reply, self.fun)
        elif order in '结束':
            if self.msglist:
                print '结束'
                itchat.send('%s' % self.reply, self.fun)
                itchat.send('结束通知', self.fun)
                self.end()
            else:itchat.send('nothing to notice', self.fun)

    def end(self):
        self.flag = False
        self.msglist = []
        self.allready = []
        self.notyet = []
        self.msgdict = {}


