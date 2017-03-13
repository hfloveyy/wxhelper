# -*- coding: utf-8 -*-


ORDERS = ['发通知','还有谁','结束']

class Si:
    def __init__(self,content):
        print 'i am Si！'
        self.content = content
    def handleMsg(self):
        order = self.content[2:12].strip()
        if order in ORDERS:
            self.handleOrder(order)

    def handleOrder(self,order):
        if order in '发通知':
            print 'i 发通知'
        elif order in '还有谁':
            print '还有谁'
        elif order in '结束':
            print '结束'