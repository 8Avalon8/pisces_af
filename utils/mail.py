# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def SendEmail(content,title = u"Pisces自动测试异常报告"):
    # 第三方 SMTP 服务
    subject = title
    mailto_list=['receiver@mail.com']           #Receiver(List)  
    mail_host="smtp.163.com"            #smtp server address  
    mail_user="username"                           #Username
    mail_pass="password"                             #password  
    mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com  
    me="PiscesAutotest"+"<"+mail_user+"@"+mail_postfix+">"  
    #content = 
    #print content
    msg = MIMEText(content,'plain','utf-8')  
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(me, 'utf-8')  
    msg['To'] = ";".join(mailto_list)                #将收件人列表以‘；’分隔  
    try:  
        #print msg
        server = smtplib.SMTP()  
        server.connect(mail_host)                            #连接服务器  
        server.login(mail_user,mail_pass)               #登录操作  
        server.sendmail(me, mailto_list, msg.as_string())  
        server.close()  
        print u"邮件发送成功"
        return True  
    except Exception, e:  
        print u"Error: 无法发送邮件"
        print str(e)  
        return False
if __name__ == '__main__':
    info = str(1) + "/" + str(3) + " passed"
    ##########Temp Usage, Should use Result Class to print
    mail = u"================================================================\r\n"
    mail += info+"\r\n"
    mail += u"Fail Tasks:\r\n"
    mail += "[Task1,Task2]" + "\r\n"
    mail += u"Tasksuits执行完毕\r\n"
    mail += u"================================================================\r\n"
    SendEmail(mail)