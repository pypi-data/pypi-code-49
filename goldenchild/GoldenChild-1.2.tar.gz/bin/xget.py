#!/usr/bin/env python2

# PYTHON_ARGCOMPLETE_OK

# http://mikekneller.com/kb/python/libxml2python/part1

import sys, re, os,  argparse, argcomplete

from io import StringIO

from GoldenChild.xpath import *
from Perdy.parser import *
from Perdy.pretty import *
from Perdy.eddo import *

def argue():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-?',			 action='help',	   help='show this help')
	parser.add_argument('-v','--verbose', action='store_true', help='show detailed output')
	parser.add_argument('-b','--bare',	action='store_true', help='show bare output with root element')
	parser.add_argument('-u','--urls',	action='store_true', help='show namespace urls')
	parser.add_argument('-c','--colour',  action='store_true', help='show colour output')
	parser.add_argument('-t','--text',	action='store_true', help='print result as text')
	parser.add_argument('-s','--single',  action='store_true', help='display result as a single value')
	parser.add_argument('-d','--delete',  action='store_true', help='delete nodes by xpath')
	parser.add_argument('-i','--inline',  action='store_true', help='when deleting do it to the original file')
	parser.add_argument('-p','--pretty',  action='store_true', help='display horizontal bar between files')
	parser.add_argument('-z','--horizon', action='store_true', help='display horizontal bar between files')
	parser.add_argument('-f','--fname',   action='store_true', help='show file name')
	parser.add_argument('-o','--output',  action='store',	  help='output to file')
	parser.add_argument('-e','--element', action='store',	  help='use this element as the document root', default='results')
	parser.add_argument('-n','--ns',	  action='store',	  help='added to context ', nargs='*', metavar='prefix=\"url\"')
	parser.add_argument('-x','--xpath',   action='store',	  help='xpath to apply to the file')
	parser.add_argument('file',		   action='store',	  help='file to parse', nargs='*')

	argcomplete.autocomplete(parser)
	args = parser.parse_args()

	if args.verbose:
		sys.stderr.write('args : ')
		prettyPrint(vars(args), colour=True, output=sys.stderr)

	return args
		
def element(xml,rdoc,rctx,nsp):
	(doc,ctx,_nsp) = getContextFromString(xml, urls=args.urls)
	element = doc.getRootElement().copyNode(True)
	for ns in nsp.keys():
		ctx.xpathRegisterNs(ns,nsp[ns])
		#element.setProp('xmlns:%s'%ns,'%s'%nsp[ns])
		rdoc.getRootElement().setProp('xmlns:%s'%ns,'%s'%nsp[ns])
	rdoc.getRootElement().addChild(element)
	return

def process(xml,output=sys.stdout,rdoc=None,rctx=None):
	if True: #try
		(doc,ctx,nsp)=getContextFromStringWithNS(xml, args.ns, urls=args.urls)
		
		if args.verbose:
			sys.stderr.write('nsp : ')
			#print(nsp)
			prettyPrint(nsp,colour=True,output=sys.stderr)

		res = ctx.xpathEval(args.xpath)
		if args.delete:
			for r in res:
				r.unlinkNode()
				r.freeNode()
			output.write('%s\n'%doc)
		elif args.single:
			if args.pretty:
				sp = StringIO.StringIO('%s'%res)
				doParse(sp,output,colour=args.colour)
				sp.close()
			else:
				output.write('%s\n'%res)
		else:
			if len(res) == 0:
				None
				#output.write('\n')
			else:
				for r in res:
					if args.text:
						output.write('%s\n'%r.content)
					elif not args.bare and rdoc and rctx:
						element('%s'%r,rdoc,rctx,nsp)
					else:
						if args.pretty:
							sp = StringIO.StringIO('%s'%r)
							doParse(sp,output,colour=args.colour)
							sp.close()
						else:
							output.write('%s\n'%r)

	if False: #except:
		sys.stderr.write('<!-- exception when parsing -->\n')
		if args.verbose:
			sys.stderr.write('exc_info : ')
			prettyPrint(sys.exc_info(), output=sys.stderr)

	return

def main():
	global args

	args = argue()
	if args.horizon:
		horizon = buildHorizon()
	else:
		horizon = None

	if args.output:
		output = open(args.output,'w')
		sys.stderr.write('%s\n'%args.output)
	else:
		output=sys.stdout

	(rdoc,rctx) = (None,None)
	if not args.bare:
		(rdoc,rctx,nsp) = getContextFromString('<%s/>'%args.element, urls=args.urls)

	if args.file and len(args.file) > 0:
		for file in args.file:
			if horizon:
				sys.stderr.write('%s\n'%horizon)
			if args.fname:
				if args.text or args.single:
					sys.stderr.write('%s: '%file)
				else:
					sys.stderr.write('%s\n'%file)

			fp = open(file)
			xml=fp.read()
			fp.close()

			if args.inline: output = open(file,'w')
			process(xml,output,rdoc,rctx)
			if args.inline:
				print file
				output.close()
			
	else:
		xml = sys.stdin.read()
		process(xml,output,rdoc,rctx)

	if not args.delete and not args.bare and not args.text and not args.single:
		if args.pretty:
			sp = StringIO.StringIO('%s'%rdoc)
			doParse(sp,output,colour=args.colour)
			sp.close()
		else:
			output.write('%s'%rdoc)
		
	if args.output:
		output.close()

	return

if __name__ == '__main__' : main()
