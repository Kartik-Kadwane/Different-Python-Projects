import smtplib

to=input("Enter the Email of recipent:\n")
content=input("Enter the content for mail:\n")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','pass12345')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()

sendEmail(to,content)
