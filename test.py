# -*- coding: utf-8 -*-
import Si
content = 'S 发通知 通知内容：时间地点开会 各单位 收到回复 '
content2 = 'S 还有谁 '
content3 = 'S 结束'
NAME = 'S'
ORDERS = ['发通知','还有谁','结束']

if __name__ == "__main__":
    s = Si.Si()
    print 'main'
    print content[:2]
    print content[2:12]
    order = content[2:6].strip()
    print order
    print type(order)
    if order in ORDERS:
        s.handleOrder(order)