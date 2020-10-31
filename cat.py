import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

mail_host = "smtp.163.com" # SMTP服务器,这里使用163邮箱
mail_sender = "gdr18668165741@163.com" # 发件人邮箱
mail_license = os.getenv("MAILKEY") # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
mail_receivers = ["1031212913@qq.com"] # 收件人邮箱，可以为多个收件人

def send_mail(title, msg):
    mm = MIMEMultipart('related')
    subject_content = title # 邮件主题
    mm["From"] = "gdr<gdr18668165741@163.com>" # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["To"] = "receiver_1_name<1031212913@qq.com>" # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["Subject"] = Header(subject_content, 'utf-8') # 设置邮件主题

    message_text = MIMEText(msg, "plain", "utf-8") # 构造邮件正文,参数1：正文内容，参数2：文本格式，参数3：编码方式
    mm.attach(message_text)# 向MIMEMultipart对象中添加文本对象

    stp = smtplib.SMTP()
    stp.connect(mail_host, 25) # 设置发件人邮箱的域名和端口，端口地址为25
    stp.set_debuglevel(1)
    stp.login(mail_sender, mail_license) # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.sendmail(mail_sender, mail_receivers, mm.as_string()) # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    print("邮件发送成功")
    stp.quit() # 关闭SMTP对象


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s]))) # sudo gem install terminal-notifier



from wxpy import *
bot = Bot() # 初始化机器人，扫码登陆
my_group = bot.groups().search("小蒋猫猫")[0] # 搜索名称含有 "小蒋猫猫" 的猫车群

@bot.register([my_group], TEXT)
def auto_reply(msg):
    print(msg)
    if '豪车' in msg.text or '神车' in msg.text:
        notify('豪车来了!','',msg.text) # 给 mac 发通知
        send_mail('豪车来了!', msg.text) # 发邮件通知
embed()

