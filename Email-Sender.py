from email.message import EmailMessage 
import ssl
import smtplib

sender = "kanwaradnanrajput@gmail.com"
password = "###########"
receiver = "45218@gcslahore.edu.pk"
subject = "subject"
body = """ This is the body """
em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,roll,em.as_string())

