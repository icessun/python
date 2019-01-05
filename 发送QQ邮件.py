# -*- coding:utf-8 -*-
__author__ = 'icessun'
__date__ = '2019/1/4 21:03'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.header import Header

sender_from = '604421385@qq.com' # 发件人邮箱
sender_to='icessun@qq.com' # 收件人邮箱
email_server = 'smtp.qq.com'
email_port=25
sender_Auth='xxxxxx'
sender_subject = 'python test'


def send_email(email_subject:str,email_content:str=None)->int:
    try:
        message = MIMEMultipart('mixed')
        message['Subject'] = Header(email_subject,'utf-8')
        message['From'] = formataddr(['test',sender_from])
        message['To'] = formataddr(['接收者',sender_to])

        # 文本发送
        text = MIMEText(email_content,'plain','utf-8')
        message.attach(text)

        # 图片发送
        send_image_file = open(r'E:\test\2.jpg','rb').read()
        image = MIMEImage(send_image_file)
        image.add_header('Content-ID','<image>')
        image['Content-Disposition'] = 'attachment;filename="test.jpg"'
        message.attach(image)

        # HTML文件发送
        content_html = """<html>
        <body>  
            <p> 
               Here is the <a href="http://www.baidu.com">link</a> you wanted.
            </p> 
          </body>  
        </html>  """
        text_html = MIMEText(content_html,'html','utf-8')
        message.attach(text_html)

        # 附件发送
        send_file = open(r'F:\password.txt').read()
        text_att = MIMEText(send_file,'base64','utf-8')
        text_att['Content-Type'] = 'application/octet-stream'
        text_att.add_header('Content-Disposition','attachment',filename='aaaa.txt')
        message.attach(text_att)

        smtp=smtplib.SMTP(email_server,email_port)
        smtp.login(sender_from,sender_Auth)
        smtp.sendmail(sender_from,sender_to,message.as_string())
        smtp.quit()
        return 0
    except:
        return -1




print(send_email('test','python发送邮件'))