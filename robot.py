#coding=utf-8

import itchat

#处理文本消息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

#登录
itchat.auto_login()
itchat.run()
