#from .mail_settings import *
#
#def test_import_settings():
#    #from mail_settings import smtp_server
#    print(smtp_server)
#    print("Hola")
#
#test_import_settings()
##print(smtp_server)

def mail_send(mail_from, mail_to, mail_subject, mail_body):
    '''
    # mainly: https://docs.python.org/3.4/library/email-examples.html
    # marginally: http://naelshiab.com/tutorial-send-email-python/
    '''

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    #from mail_settings import smtp_server
    #from mail_settings import smtp_port
    #from mail_settings import smtp_username
    #from mail_settings import smtp_password
    smtp_server = 'smtp.heanet.ie'
    smtp_port = 587
    smtp_username = 'torque_app'
    smtp_password = 'Fai4ohai!ph4wah9'

    #mail1 = 'daniel.lete@heanet.ie'
    #mail2 = 'daniel.lete@gmail.com'
    #toaddrs  = mail1 + ", " + mail2

    msg = MIMEMultipart()
    msg['From'] = mail_from
    #msg['To'] = mail_to
    msg['Subject'] = mail_subject
    body = mail_body
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        #server.set_debuglevel(True) # show communication with the server
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.quit()
        result = "PASS, mail sent to " + mail_to
    except Exception as err:
        result = "FAIL, " + str(err)
        pass

    return result


#m_to = 'daniel.lete@heanet.ie'
#m_from = 'noreply@white.heanet.ie'
#m_subject = "AA rainy day of October"
#m_body = 'It was morning and everything was wet. Few people where in the street.'
#m = mail_send(m_from, m_to, m_subject, m_body)
#print(m)
