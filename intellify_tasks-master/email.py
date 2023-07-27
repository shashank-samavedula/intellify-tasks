import smtplib

sender = 'holmes@gmail.com'
receivers = ['poirot@yahoo.com','marple@gmail.com']
message = "This is the message"

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print("Successfully sent email")
