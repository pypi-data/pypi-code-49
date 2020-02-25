import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from configparser import ConfigParser
import os


def send_email(ToEmail, subject, body, attachement):
    # cfg = ConfigParser()
    # cfg.read('./config.ini')
    mailServer = 'SMTP.JSAPDC.GLOBAL' # cfg.get('Email', 'Host')
    port = 25   # cfg.get('Email', 'Port')
    msg = MIMEMultipart()

    if body.strip() == "" and attachement != "":
        body = "<pre>"
        with open(attachement) as ath_f:
            body += ath_f.read().replace("\n", "<br>")
        body += "</pre>"
    FromEmail = 'Dev.sitOpenVMS.Test@davitamedicalgroup.com'
    ToEmail = str(ToEmail).split(',')
    msg['From'] = FromEmail
    msg['To'] = ",".join(ToEmail)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    filename = attachement
    if os.path.isfile(attachement):
        fileExt = os.path.splitext(os.path.basename(attachement))[1]
        if fileExt.upper() == ".TMP":
            filename = os.path.splitext(attachement)[0] + ".txt"
            if os.path.isfile(filename):
                os.remove(filename)
            os.rename(attachement, filename)
        with open(filename, "rb") as attachment:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
            msg.attach(p)
        if fileExt.upper() == ".TMP":
            os.rename(filename, os.path.splitext(filename)[0] + ".tmp")
    s = smtplib.SMTP(mailServer, port)
    s.starttls()
    # s.login(fromaddr, cfg.get('Email', 'EmailPassword'))

    text = msg.as_string()
    s.sendmail(FromEmail, ToEmail, text)
    s.quit()



# send_email('Hi', '<b>Test</b>', '/DATA/DEV/kde-spydakula/OpenVMs/PythonScripts/UtilityScripts/copy_files.py')












