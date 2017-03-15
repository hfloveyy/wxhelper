# -*- coding: utf-8 -*-

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
    def handleMsg(self,content,from_user_name):
        self.content = content
        self.fun = from_user_name
        order = self.content[2:6].strip().encode('utf-8')
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
        elif order in '还有谁':
            print '还有谁'
            
        elif order in '结束':
            print '结束'
            self.flag = False
            self.msglist = []
            self.msgdict = {}

    def print_dict(self):
        print self.msgdict
        reply = ''
        for s in self.msglist:
            reply = reply + ' ' + s
        itchat.send(reply,self.fun)