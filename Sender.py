import smtplib


emailId = input('Enter your email id : ')
passwd = input('Enter your password : ')

server = smtplib.SMTP_SSL("smtp.gmail.com",465) # establishing the server
try:
    server.login(emailId, passwd)
except:
    print('login failed')

senderId = input("Enter the Client Email Id : ")
msg = input("Enter the Message to be sent : ")
server.sendmail(emailId,senderId,msg)

server.quit()
print('sent')

'''
 If you get Bad Authentication Error, go to gmail > privacy and enable less secured apps permission

'''