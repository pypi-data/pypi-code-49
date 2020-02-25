#!/usr/bin/env python2

import sys, re, os, libxml2
from collections import namedtuple

XML = namedtuple('XML', ['doc','ctx','nsp'])

def getContextFromStringWithNS(xml, argsNS=None, urls=None):

	def handler(ectx, error):
		None #sys.stderr.write('error=%s'%error)

	libxml2.registerErrorHandler(handler,'')

	doc = libxml2.parseDoc(xml)
	ctx = doc.xpathNewContext()
	nsp = {}

	for ns in [
		doc.getRootElement().ns(),
		doc.getRootElement().nsDefs(),
	]:
		if ns:
			nsp[ns.name] = ns.content
			if urls:
				sys.stderr.write('xmlns:%s=%s\n'%(ns.name, ns.content))

	if argsNS:
		pn = re.compile('^([^=]*)=["\']([^\'"]*)["\']$')
		for ns in argsNS:
			mn = pn.match(ns)
			if mn:
				nsp[mn.group(1)] = mn.group(2)

	for prefix, namespace in nsp.iteritems():
		ctx.xpathRegisterNs(prefix,namespace)

	return (doc,ctx,nsp)

def getContextFromString(xml, argsNS=None, urls=None):
	(doc,ctx,nsp) = getContextFromStringWithNS(xml, argsNS, urls)
	return (doc,ctx,nsp)

def getContextFromFile(fn, argsNS=None, urls=None):
	fp = open(fn)
	xml = fp.read()
	fp.close()
	return getContextFromString(xml, argsNS, urls)

def getContextFromStream(input, argsNS=None, urls=None):
	xml = input.read()
	return getContextFromString(xml, argsNS, urls)

def getElements(context,xpath,parent=None):
	if parent:
		context.setContextNode(parent)
	return context.xpathEval(xpath)

def getElement(context,xpath,parent=None):
	elements = getElements(context,xpath,parent)
	if len(elements) > 0:
		return elements[0]
	return None

def getElementText(context,xpath,parent=None):
	element = getElement(context,xpath,parent)
	if element:
		return element.content
	return None

def setElementText(context,xpath,value,parent=None):
	element = getElement(context,xpath,parent)
	if element:
		element.setContent(value)
	return

def insertElement(document, name, before, parent=None, ns=None):
	if not parent:
		parent = document.getRootElement()
	#print(parent.ns(), type(parent.ns()))
	element = document.newDocNode(ns or parent.ns(), name, None)
	before.addPrevSibling(element)
	return element

def appendElement(document, name, after, parent=None, ns=None):
	if not parent:
		parent = document.getRootElement()
	#print(parent.ns(), type(parent.ns()))
	element = document.newDocNode(ns or parent.ns(), name, None)
	after.addNextSibling(element)
	return element

def addElement(document, name, parent=None, ns=None):
	if not parent:
		parent = document.getRootElement()
	#print(parent.ns(), type(parent.ns()))
	element = document.newDocNode(ns or parent.ns(), name, None)
	parent.addChild(element)
	return element

def addElementText(document, name, value, parent=None, ns=None):
	if not parent:
		parent = document.getRootElement()
	element = document.newDocNode(ns or parent.ns(),name,value)
	parent.addChild(element)
	return element

def addElementCDATA(document,name,value,parent=None):
	element = addElement(document,name,parent=parent)
	cdata = document.newCDataBlock(value,len(value))
	element.addChild(cdata)
	return element

def hasAttribute(element,attname):
	return element.hasProp(attname)

def getAttribute(element,attname):
	return element.prop(attname)

def setAttribute(element,attname,value):
	try:
		element.setProp(attname,value)
	except:
		element.newProp(attname,value)
	return

def delAttribute(element,attname):
	for property in element.properties:
		#sys.stderr.write('%s\n'%property)
		if property.type == 'attribute' and property.name == attname:
			property.unlinkNode()
			property.freeNode()
			break
	return
