# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/24 11:25'
from random import Random
# 导入Django自带的邮件模块
from users.models import EmailVerifyRecord
# 导入Django自带的邮件模块
from django.core.mail import send_mail
# 导入setting中发送邮件的配置
from DataMingingPaper.settings import EMAIL_FROM

'''
生成随机字符串
'''
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    str_set = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    random = Random()
    for i in range(random_length):
        index = random.randint(0, len(str_set)-1)
        str += str_set[index]
    return str

'''
发送注册邮件
'''
def send_register_email(email, send_type='register'):
    # 1.发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 2.定义邮件内容并发送
    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = 'Django在线文献数据挖掘系统网站，注册激活链接.'
        email_body = '请点击下面的链接激活你的账号: http://www.dataminging.com/active/{0}'.format(code)
        # 使用Django内置函数完成邮件发送。四个参数：1.subject,2.message,3.from_email,4.recipient_list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = 'Django在线文献数据挖掘系统网站，密码重置链接.'
        email_body = '请点击下面的链接重置你的密码: http://www.dataminging.com/reset/{0}'.format(code)
        # 使用Django内置函数完成邮件发送。四个参数：1.subject,2.message,3.from_email,4.recipient_list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass