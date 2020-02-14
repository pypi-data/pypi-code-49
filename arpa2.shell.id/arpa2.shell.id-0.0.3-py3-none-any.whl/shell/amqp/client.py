#!/usr/bin/env python
#
# arpa2api -- AMQP 1.0 remote shell inquiries.
#
# This command runs batches of shell commands on a
# remote machine, sending it over AMQP.  Sets reply_to
# so the responses from the shell can be reported.
#
#TODO# This incarnation is based on stdin/stdout/stderr,
#TODO# future versions may present a connectable daemon.
#
# Each command is formatted in JSON, following the
# shell structure as added for the onecmd_json()
# method in our extended version of cmdparser.
# See PROTOCOL.MD for details.  The batch of commands
# submitted as a whole is simply a JSON array.
#
# From: Rick van Rein <rick@openfortress.nl>


import sys
import uuid

import json
import gssapi

from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


bad = False


class ARPA2ShellClient (MessagingHandler):

	def __init__ (self, broker, queue, batch):
		super (ARPA2ShellClient,self).__init__ ()
		self.broker = broker
		self.queue = queue
		assert (type (batch) == type ([]))
		self.batch = batch
		self.name = gssapi.Name (
			#TODO#FIXED#
			#TODO#ALTERNATIVE# 'arpa2shell/host.name@REALM.NAME'
			'amqp/testsrv.qpid.arpa2@ARPA2.NET'
			)
		self.side = 'initiate' # initiate, accept, both
		self.gctx = None
		self.gsta = 'lazy'
		self.corlid = str (uuid.uuid4 ())

	def _have_gssapi_ctx (self):
		assert (self.name is not None)
		if self.gctx is None:
			self.gctx = gssapi.SecurityContext (
				name = self.name,
				usage = 'initiate')
		assert (self.gctx is not None)
		self.gctx.__DEFER_STEP_ERRORS__ = False
		return self.gctx

	def on_start_gssapi (self, event):
		assert (self.gsta == 'lazy')

	# Start GSSAPI as soon as the first link is open (the sender)
	#
	def on_link_opened_gssapi (self, event):
		#DEBUG# print 'gssapi link opened'
		if self.gsta == 'lazy':
			#DEBUG# print 'gssapi is first (sender)'
			ctx = self._have_gssapi_ctx ()
			#DEBUG# print 'using (new) client context', ctx
			gsstoken = ctx.step ()
			assert (gsstoken is not None)
			#DEBUG# print 'initial token of size:', len (gsstoken), 'namely', gsstoken.encode ('hex'), '::', type (gsstoken)
			msg = Message (
					body=gsstoken,
					id=self.corlid,
					reply_to=self.recver.remote_source.address)
			self.sender.send (msg)
			#DEBUG# print 'sent initial message sized:', len (gsstoken)
			self.gsta = 'boot'

	# Consume a GSSAPI token and update the context accordingly.
	# Once GSSAPI is complete, trigger on_link_opened_securely()
	#
	def on_message_gssapi (self, event):
		#DEBUG# print 'got gssapi reply'
		#DEBUG# try:
		#DEBUG# 	print 'correlation id is', event.message.correlation_id, 'should equal', self.corlid
		#DEBUG# except:
		#DEBUG# 	pass
		assert (self.gsta != 'comm')
		if self.gsta == 'lazy':
			# We are receiving a message before sending one.
			# Only if we are 'accept' or 'both' is this ok.
			raise NotImplementedError ('GSSAPI accept mode')
		elif self.gsta == 'boot':
			ctx = self._have_gssapi_ctx ()
			#DEBUG# print 'using client context', ctx
			gsstoken = event.message.body
			#DEBUG# print 'stepping client with size:', len (gsstoken), 'namely', gsstoken.encode ('hex'), '::', type (gsstoken)
			assert (not ctx.complete)
			gsstoken = ctx.step (gsstoken)
			if gsstoken is not None:
				#DEBUG# print 'produced new token size:', len (gsstoken), 'namely', gsstoken.encode ('hex')
				msg = Message (
					body=gsstoken,
					reply_to=self.recver.remote_source.address,
					correlation_id=self.corlid)
				self.sender.send (msg)
			if ctx.complete:
				self.gsta = 'comm'
				#DEBUG# print 'client opened link securely'
				self.on_link_opened_securely (event)
		elif self.gsta == 'comm':
			raise RuntimeError ('GSSAPI already communicates')
		else:
			raise NotImplementedError ('GSSAPI state ' + self.gsta)

	def _decrypted_message (self, body):
		assert (self.gsta == 'comm')
		ctx = self._have_gssapi_ctx ()
		body2 = json.loads (str (ctx.decrypt (body), 'utf-8'))
		return body2

	def _encrypted_message (self, body, **kwargs):
		assert (self.gsta == 'comm')
		ctx = self._have_gssapi_ctx ()
		body2 = ctx.encrypt (bytes (json.dumps (body), 'utf-8'))
		return Message (body=body2, **kwargs)

	def on_start (self, event):
		#DEBUG# print 'started'
		ctr = event.container
		cnx = ctr.connect (self.broker)
		# The sender triggers the first on_link_opened() event
		self.sender = ctr.create_sender (cnx, self.queue)
		self.recver = ctr.create_receiver (cnx, None, dynamic=True)
		#DEBUG# print 'sender, receiver created'
		self.on_start_gssapi (event)
		#DEBUG# print 'gssapi also started'

	# First pass the link over to GSSAPI; later return to on_link_opened_securely()
	#
	def on_link_opened (self, event):
		#DEBUG# print 'link opened'
		self.on_link_opened_gssapi (event)

	# After GSSAPI has run, it triggers this handler to open the application.
	# Note that the event can only be relied upon for structural data.
	# We will only call this operation once, sorry :-S
	#
	def on_link_opened_securely (self, event):
		#DEBUG# print 'link was opened securely on client (will we be sending twice?)'
		msg = self._encrypted_message (
				self.batch,
				reply_to=self.recver.remote_source.address,
				correlation_id=self.corlid)
		self.batch = None
		self.sender.send (msg)
		#DEBUG# print 'message sent sized:', len (msg.body)

	# Initial messages arrive, for GSSAPI, but in 'comm' mode it is a reply
	#
	def on_message (self, event):
		#DEBUG# print 'message from', self.recver.remote_source.address, 'to ?'
		if self.gsta != 'comm':
			self.on_message_gssapi (event)
			return
		reply0 = event.message.body
		if reply0 is None:
			return
		#DEBUG# print 'message received on client sized:', len (reply0), 'namely', reply0.encode ('hex')
		reply = self._decrypted_message (reply0)
		#TODO#JSON# Return JSON-parsed data in reply instead of just printing it
		global bad
		for jout in reply:
			#DEBUG# print ('Got jout = %r\n' % jout)
			if 'headers_' in jout and 'body_' in jout:
				sys.stdout.write ('## HEADERS:\n%r\n\n' % jout ['headers_'])
				sys.stdout.write ('## BODY:\n%s\n' % jout ['body_'])
			elif 'stdout_' in jout:
				sys.stdout.write (jout ['stdout_'])
			else:
				#DEBUG#
				sys.stdout.write ('## NO OUTPUT\n')
			if 'stderr_' in jout:
				sys.stderr.write (jout ['stderr_'])
				bad = True
		#DEBUG# print 'closing down'
		event.connection.close ()
		event.container.stop ()
		#DEBUG# print 'closed down'



# The main program creates on ARPA2ShellClient and runs it on a JSON
# batch read from stdin.
#
def main ():
	cmdbatch = json.loads (sys.stdin.read ())
	handler = ARPA2ShellClient ('amqp://localhost:5672', '/internetwide/arpa2.net/reservoir', cmdbatch)
	contain = Container (handler)
	contain.run ()
	exit (1 if bad else 0)

if __name__ == '__main__':
	main ()
