# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import itchat

ORDERS = ['发通知','还有谁','结束']
MEMBERS = ['哈尔滨监狱','牡丹江监狱','佳木斯监狱','呼兰监狱','黎明监狱','齐齐哈尔监狱','讷河监狱','新康监狱','华山监狱','香兰监狱','大庆监狱',
           '凤凰山监狱','新建监狱','女子监狱','鸡西监狱','东风监狱','双鸭山监狱','北安监狱','七台河监狱','泰来监狱','五大连池监狱','未管所','六三监狱','松滨监狱']
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
            if self.msglist:
                self.notyet = list(set(MEMBERS) - set(self.allready))
                self.notyet = self.notyet if self.notyet else ' '
                self.reply = self.msglist[0]+'\n已签到: ' + ' '.join(self.allready)+\
                             '\n未签到: '+' '.join(self.notyet)

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
            self.reply = self.msglist[0] + '\n已签到: ' + ' '.join(self.allready) + \
                         '\n未签到: ' + ' '.join(self.notyet)
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


