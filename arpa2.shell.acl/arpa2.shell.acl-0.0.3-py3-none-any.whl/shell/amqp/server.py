#!/usr/bin/env python
#
# arpa2api.d -- Receive requests to ARPA2 shells over AMQP.
#
#TODO#JSON# Integrate this into the arpa2.shell.py module.
#
# This is an AMQP 1.0 server that receives shell command
# requests, finds the shells to run them in, and sends
# back the result.
#
# The shells do not provide exit codes (other than the
# shutdown of the shell) but instead provide output on
# stdout and stderr.  This is sent back to the requester,
# if a reply_to address is presented along with the
# shell request.  Future versions of the command might
# receive stdin from the message, though that will
# mostly be empty.
#
# The idea is to have the same handler classes run under
# arpa2.shell in an interactive mode and in here using a
# batch-processing mode.  The interactive shell can be
# used by administrators to correct for problems.
#
# From: Rick van Rein <rick@openfortress.nl>


import sys
import time
import re

import pkg_resources

from arpa2.shell import cmdshell

import json
import gssapi
from gssapi.raw.misc import GSSError


from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


# The name of the entry group of shells
#
entrypoint_group = 'arpa2.shell.cmdshell.subclasses'


# Regular expressions to parse stdout_ information
#
rex_hdr = '^([A-Za-z0-9-]+): ([^\n]*)$'
rex_out = '^(' + rex_hdr + ')*\n(.*)$'

re_hdr = re.compile (rex_hdr)
re_out = re.compile (rex_out)


class ARPA2ShellDaemon (MessagingHandler):

	"""The ARPA2ShellDaemon awaits incoming ARPA2
	   shell requests, and sends them into backend
	   processes that run those shells.  Results are
	   sent back if a reply_to address is provided
	   in the shell request batch message.
	   
	   Messages are protected with GSSAPI/Kerberos5,
	   and the exchange is initiated as GSSAPI is.
	   After initial setup, any number of messages
	   may follow.

	   Although messages can be processed one at a
	   time, the GSSAPI contexts require some more
	   maintenance.  The correlation_id in a message
	   (defaulting to the initiating message's id)
	   is used to keep messages related.

	   TODO: Expire contexts when credentials do.
	"""


	# Create a new instance of the ARPA2ShellDaemon.
	#
	def __init__ (self, broker, address):
		super (ARPA2ShellDaemon,self).__init__ ()
		self.shell = { }
		self.broker  = broker
		self.address = address
		self.name = gssapi.Name (
			#TODO#FIXED#
			'amqp/testsrv.qpid.arpa2@ARPA2.NET')
		self.side = 'accept' # initiate, accept, both
		self.cred = None
		self.gctx = { }

	def _have_gssapi_ctx_corlid (self, msg):
		assert (self.name is not None)
		corlid = msg.correlation_id or msg.id
		assert (corlid is not None)
		if self.cred is None:
			self.gctx = { }
			self.cred = gssapi.Credentials (
				name = self.name,
				mechs = set ([gssapi.MechType.kerberos]),
				usage = self.side)
			#DEBUG# print 'server has self.cred setup as', self.cred.inquire ()
		#DEBUG# print 'checking for match with corlid', corlid
		if corlid in self.gctx:
			ctx = self.gctx [corlid]
		else:
			ctx = gssapi.SecurityContext (
				creds = self.cred,
				usage = 'accept')
			self.gctx [corlid] = ctx
			#DEBUG# print 'new security context for server:', ctx
		assert (ctx is not None)
		ctx.__DEFER_STEP_ERRORS__ = False
		return (ctx,corlid)

	# Consume a GSSAPI token and update the context accordingly.
	# Once GSSAPI is complete, trigger on_link_opened_securely()
	#
	def on_message_gssapi (self, event, ctx_corlid):
		(ctx,corlid) = ctx_corlid
		assert (not ctx.complete)
		gsstoken = event.message.body
		#DEBUG# print 'received gssapi token size:', len (gsstoken)
		gsstoken = ctx.step (gsstoken)
		if gsstoken is not None or not ctx.complete:
			#DEBUG# print 'sending gssapi token size:', len (gsstoken), 'namely', gsstoken.encode ('hex')
			msg = Message (
				body=gsstoken,
				address=event.message.reply_to,
				reply_to=self.recver.remote_source.address,
				correlation_id=corlid)
			self.sender.send (msg)
			#DEBUG# print 'sent with corlid', corlid
		#DEBUG# print 'done receiving and processing gssapi token'


	# Load the shell as a plugin module to this daemon.
	# Shells must hold an cmdshell.Cmd instance named Cmd.
	# The processes are retained for future re-use.
	#
	#TODO# We may want to be able to reset shells.
	#
	def get_shell (self, modname):
		if modname [:5] != 'arpa2':
			raise Exception ('Not a command shell name: ' + modname)
		if modname in self.shell:
			return self.shell [modname]
		exc = 'Shell not available: ' +  modname
		for ep in pkg_resources.iter_entry_points (
					group=entrypoint_group,
					name=modname):
			#DEBUG# print ('GOT EP=%r :: %r' % (ep, type (ep)))
			cmd_cls = ep.load ()
			#DEBUG# print ('GOT CMD_CLS=%r :: %r' % (cmd_cls, type (cmd_cls)))
			if issubclass (cmd_cls, cmdshell.Cmd):
				cmd = cmd_cls ()
				self.shell [modname] = cmd
				return cmd
			exc = 'Not an ARPA2 shell: ' + modname
		raise Exception (exc)


	# Prefix lines with the given prompt and return the text.
	#
	def _prefix_lines (self, prompt, text):
		if text [-1:] == '\n':
			text = text [:-1]
		if text != '':
			text = prompt + text.replace ('\n', '\n' + prompt)
		return text


	# Parse special forms in the standard output.
	# This may be # be expanded to accommodate our requirements.
	# Currently: <hdrname>: <value>\n...\n\n<body...>
	#
	def _parse_stdout (self, jout):
		if 'stderr_' in jout:
			return
		try:
			out = jout ['stdout_']
			if '\n\n' in out:
				(hd,bd) = out.split ('\n\n', 1)
			else:
				if out [-1:] == '\n':
					out = out [:-1]
				(hd,bd) = (out,'')
			print ('Header lines: """%r"""' % hd.split ('\n'))
			headers = [ re_hdr.match (ln).groups () for ln in hd.split ('\n') ]
			# Success, so fill "headers_" and "body_" keys
			jout ['headers_'] = headers
			jout ['body_'] = bd
		except Exception as e:
			return


	# Run a command in a given shell and collect the results.
	# The command may span multiple lines, adding to stdin.
	# Update the command value with several new JSON keys.
	#
	def run_command (self, shellname, command, name, life):
		#DEBUG# print 'running shell', shellname, 'for', command
		try:
			shell = self.get_shell (shellname)
			shell.gss_name = name
			shell.gss_life = life + time.time ()
			jout = shell.onecmd_json (command)
			self._parse_stdout (jout)
			return jout
		except Exception as e:
			return { 'stderr_':
				'Exception in run_command: %s\n' % e }
		finally:
			shell.gss_name = None
			shell.gss_life = None


	# Split a message into shell commands that are run
	# in their respective shells.  Return the collective
	# reply to the batch job in the message.
	#
	def run_message (self, message, ctx):
		shellnames = set ()
		name = ctx.initiator_name
		life = ctx.lifetime
		reply = []
		for jin in message:
			jout = jin.copy ()
			jin_do = jin ['do_']
			if type (jin_do) != type ([]):
				jin_do = jin_do.split ()
			shell = jin_do [0]
			jout ['do_'] = jin_do [1:]
			shellnames.add (shell)
			if life > 0:
				try:
					jout = self.run_command (shell, jout, name, life)
				except Exception as e:
					jout ['stderr_'] = 'Exception in run_message: %s\n' % str (e)
			else:
				jout ['stderr_'] = 'Access denied: Credentials expired\n'
			reply.append (jout)
		for shellname in shellnames:
			#DEBUG# print ('resetting shell', shellname)
			self.get_shell (shellname).reset ()
		#DEBUG# print 'message run complete'
		return reply


	# Setup the current Container for incoming and reply traffic
	#
	def on_start (self, event):
		#DEBUG# print 'starting'
		ctr = event.container
		cnx = ctr.connect (self.broker)
		self.recver = ctr.create_receiver (cnx, self.address)
		self.sender = ctr.create_sender   (cnx, None        )
		#DEBUG# print 'started'


	def _decrypted_message (self, body, ctx_corlid):
		(ctx,corlid) = ctx_corlid
		body2 = json.loads (str (ctx.decrypt (body), 'utf-8'))
		return body2

	def _encrypted_message (self, body, ctx_corlid, **kwargs):
		(ctx,corlid) = ctx_corlid
		try:
			body2 = ctx.encrypt (bytes (json.dumps (body), 'utf-8'))
		except GSSError as ge:
			body2 = json.dumps ('GSSAPI Error: ' + str (ge))
		return Message (body=body2, **kwargs)

	# Receive an AMQP message.  Run its batch of commands,
	# collect the reply and pass it back if so desired.
	#
	def on_message (self, event):
		msg = event.message
		#DEBUG# print 'message received size:', len (msg.body), 'namely', msg.body.encode ('hex')
		(ctx,corlid) = self._have_gssapi_ctx_corlid (msg)
		try:
			if not ctx.complete:
				#DEBUG# print 'handling message as gssapi'
				self.on_message_gssapi (event, (ctx,corlid))
				#DEBUG# print 'handled  message as gssapi'
				return
		except GSSError as ge:
			#DEBUG# print 'ran into a problem:', str (ge)
			return #TODO# Not ideal, but can we send a reply?
		#DEBUG# print 'treating as plain message'
		if msg.body is None:
			#DEBUG# print 'body is none'
			return
		#DEBUG# print 'treating as non-empty plain message'
		try:
			body2 = self._decrypted_message (msg.body, (ctx,corlid))
			#DEBUG# print 'decrypted to', body2
			ans = self.run_message (body2,ctx)
			#DEBUG# print ('Succeeded to run, ans = %r\n' % ans)
		except GSSError as ge:
			#DEBUG# print ('responding with gssapi error %r\n' % ge)
			ans = [ { 'stderr_': 'GSS-API Error: %s\n' % str (e) } ]
		except Exception as e:
			#DEBUG# print ('responding with exception %r\n' % e)
			ans = [ { 'stderr_': 'Exception in on_message: %s\n' % str (e) } ]
		#DEBUG# print ('answer will be\n', ans)
		if msg.reply_to is not None:
			#DEBUG# print 'composing reply'
			rto = self._encrypted_message (ans, (ctx,corlid),
				address=msg.reply_to,
				reply_to=self.recver.remote_source.address,
				correlation_id=corlid)
			self.sender.send (rto)
			#DEBUG# print 'sent reply size:', len (rto.body), 'namely:', rto.body.encode ('hex')
		else:
			#DEBUG# print 'no reply requested by client'
			pass


# The main program creates on ARPA2ShellDaemon and runs it indefinately.
#
def main ():
	handler = ARPA2ShellDaemon ('amqp://localhost:5672', '/internetwide/arpa2.net/reservoir')
	contain = Container (handler)
	contain.run ()

if __name__ == '__main__':
	main ()
