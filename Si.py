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

    def handleOrder(self,order):
        if order in '发通知':
            print 'i 发通知'
            self.flag = True
            self.msglist.append(self.content[12:])
            itchat.send(self.content[12:], self.fun)
        elif order in '还有谁':
            print '还有谁'
            self.notyet = list(set(MEMBERS)-set(self.allready))
            if self.msglist:
                self.reply = self.msglist[0]+'\nallreay: ' + ' '.join(self.allready)+\
                             '\nnot yet: '+' '.join(self.notyet)
            self.print_dict()
        elif order in '结束':
            if self.msglist:
                print '结束'
                self.print_dict()
                itchat.send('结束通知', self.fun)
                self.flag = False
                self.msglist = []
                self.allready = []
                self.notyet = []
                self.msgdict = {}
            else:itchat.send('nothing to notice', self.fun)


    def print_dict(self):
        print self.reply
        print type(self.reply)
        itchat.send('%s' % self.reply,self.fun)