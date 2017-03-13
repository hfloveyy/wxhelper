# -*- coding: utf-8 -*-
import Si
content = 'S 发通知 通知内容：时间地点开会 各单位 收到回复 '
content2 = 'S 还有谁 '
content3 = 'S 结束'
NAME = 'S'


if __name__ == "__main__":
    print 'main'
    print content[:2]
    if NAME in content[:2]:
        s = Si.Si(content)
        s.handleMsg()