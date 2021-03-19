
import email.message
msg = email.message.EmailMessage()
msg["From"]="bigben83530@gmail.com"
msg["To"]="bigben83530@gmail.com"
msg["Subject"]="你好"
#寄送純文字內容
# msg.set_content("測試看看")
#寄送多樣式的內容
msg.add_alternative("<h3>優惠眷</h3>滿五百送一百",subtype="html")
#連線到SMTP Server.驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋GMAIL SMTP SERVER
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("bigben83530@gmail.com","bigben106022535")
server.send_message(msg)
server.close()







