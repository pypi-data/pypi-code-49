import datetime
import re
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib import parse, request
import idna
from OpenSSL import SSL
G={
	"expire":10,
	"isSend":False,
	"isPrint":False,
	"isCert":False,
	"isUrl":False,
	"smtpServer":None,
	"smtpPort":None,
	"account":None,
	"password":None,
	"receivers":[]
}
r = re.compile(r'((?:https|http)://[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+/?)')
def test(func):
	def wrapper(urllist):
		msg = []
		for url in urllist:
			result = func(url)
			if result == "":
				continue
			else:
				msg.append(result)
		return msg
	return wrapper

def getUrl(filename):
	try:
		urllist = []
		hander = open(filename, 'r', encoding = 'utf-8')
		for url in hander.readlines():
			url = url.strip().split('#')[0]
			if url == "":
				continue
			if r.search(url):
				urllist.append(url)
	except FileNotFoundError:
		print("{0} not found!".format(filename))
		exit(-1)
	except UnicodeDecodeError:
		print("{0} decode error".format(filename))
		exit(-1)
	return urllist

@test
def verifyAddress(url):
	try:
		code = request.urlopen(url, timeout = 5).getcode()
		if code > 400:
			result = ""
		else:
			result = (url, code)
	except Exception as e:
		result = (url,code,e)
	return result

def _getCert(url):
	meta_url = parse.urlparse(url)
	sock_info = (meta_url.hostname, meta_url.port or 443)
	try:
		sock = socket.socket()
		sock.connect(sock_info)
		cxt = SSL.Context(SSL.SSLv23_METHOD)
		cxt.check_hostname = False
		cxt.verify_mode = SSL.VERIFY_NONE
		sock_ssl = SSL.Connection(cxt, sock)
		sock_ssl.set_tlsext_host_name(idna.encode(sock_info[0]))
		sock_ssl.set_connect_state()
		sock_ssl.do_handshake()
		cert = sock_ssl.get_peer_certificate()
		sock_ssl.close()
		sock.close()
	except Exception as e:
		cert = e
	return cert
@test
def verifyCert(url):
	cert = _getCert(url)
	if isinstance(cert,Exception):
		result = (url,-1,cert)
	else:
		certTime = datetime.datetime.strptime(str(cert.get_notAfter()[: -1], encoding = 'utf-8'), '%Y%m%d%H%M%S') + datetime.timedelta(hours = 8)
		TimeRemained = certTime - datetime.datetime.now()
		if TimeRemained.days > G['expire']:
			result = ""
		else:
			result = (url, TimeRemained.days)
	return result


def setMailConfig(args):
	if len(args) < 3:
		print("lost mail config")
		exit(-1)
	else:
		try:
			hand = open(args[2],"r",encoding="utf-8")
			for i in hand.readlines():
				i = i.strip().split('#')[0]
				if i == "":
					continue
				elif i.startswith("server:"):
					i = i.split(":")
					G['smtpSever']=i[1]
					G['smtpPort']=i[2]
					G['account']=i[3]
					G['password']=i[4]
				else:
					G['receivers'].append(i)
			G['isSend'] = True
			print("mail config loaded")
		except Exception as c:
			print(c)
			exit(-1)

def send(content,subject):
	try:
		con = smtplib.SMTP_SSL(G['smtpSever'], G['smtpPort'], None, None, None, 3)
		con.login(G['account'],G['password'])
		text = MIMEText(content)
		shell = MIMEMultipart()
		shell['Subject'] = subject
		shell['From'] = G['account']
		shell['to'] = G['password']
		shell.attach(text)
		con.sendmail(G['account'],G['receivers'], shell.as_string())
		con.send
	except Exception as e:
		print(e)
def makeRecords(record,head):
	records = head+":\n"
	for i in record:
		tmp = ""
		for x in i:
			tmp += str(x)+"    "
		records += tmp+"\n"
	return records

def setStat(args):
	global G
	if len(args) < 3:
		printHelpExit()
	else:
		args = args[1:]
	switch = args[0]
	G['urlfile'] = args[1]
	isCert = re.search(r'c\d+', switch)
	isUrl = re.search(r'u', switch)
	isSend = re.search(r'e',switch)
	isPrint = re.search(r'p',switch)
	if not isCert and not isUrl:
		printHelpExit()
	if isSend:
		setMailConfig(args)
	if isCert:
		G['isCert']=True
		G['expire']=int(isCert.group()[1:])
	if isUrl:
		G['isUrl']=True
	if isPrint:
		G['isPrint'] = True
def printHelpExit():
	print("""
Format:
	python -m rzqtest switch urlfile [emailconfig]

Switch:
	c[number] check certified
	u check address
	p print result to screen
	e send email use with emailconifg

emailconfig format:
	server:domain:port:account:password
	# receivers
	a@xx.xx
	b@xx.xx
""")
	exit(-1)