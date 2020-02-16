import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Error(Exception):
	pass
	
class Mail:
	"""
	Base Class for the module. You can send emails with attachments
	
	Parameters
	------------------
	mail: :class: `str`
		The actual mail you are going to send using :class: `Mail`
	password: :class: `str`
		The given mail account password
		
	Attributes
	---------------
	send
		Actually sends the mail
	"""
	def __init__(self, mail, password):
		self.mail = mail
		self.password = password
		
	async def send(self, reciever, body, subject=None, bcc=None, attachment_name=None, attachment_bytes=None):
		"""
		Sends the email
		
		Parameters
		-----------------
		reciever: :class: `str`
			The recievers mail address
		body: :class: `str`
			The body of the mail
		subject: :class: `str`
			The subject of the mail
		bcc: :class: `str`
			The bcc of the mail
		attachment_name: :class: `str`
			The name of the attachment
		attachment_bytes: :class: `str`
			The bytes of the attachment
		"""
		sender_mail = self.mail
		password = self.password
		
		msg = MIMIEMultipart()
		msg["From"] = sender_mail
		msg["To"] = reciever
		msg["Subject"] = subject if not subject else "No Subject given"
		msg["Bcc"] = bcc
		
		msg.attach(MIMEText(body, "html"))
		
		if attachment_bytes is not None and attachment_name is not None:
			part = MIMEBase("application","octet-stream")
			part.set_payload(attachment_bytes)
			
			encoders.encode_base24(part)
			
			part.add_header(
				"Content-Disposition",
				f"attachment, filename= {attachment_name}"
			)
			
			message.attach(part)
			
		txt = message.as_string()
		
		ctx = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as server:
			server.login(sender_mail, password)
			server.sendmail(sender_mail, reciever, text)