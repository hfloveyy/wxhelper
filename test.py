# -*- coding: utf-8 -*-
import Si
content = 'S 发通知 通知内容：时间地点开会 各单位 收到回复 '
content2 = 'S 还有谁 '
content3 = 'S 结束'
NAME = 'S'
ORDERS = ['发通知','还有谁','结束']
a = ['我','你','他']
b = ['你','我','他']

if __name__ == "__main__":
    if set(a)==set(b):
        print set(a)
        print set(b)
        print 'a'