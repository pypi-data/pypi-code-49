#!/usr/bin/env python2

# PYTHON_ARGCOMPLETE_OK

import sys, re, os, libxml2, argparse, argcomplete

from Perdy.Colours import Colours
from Perdy.eddo import *
from Perdy.pretty import *
from GoldenChild.xpath import *

parser = argparse.ArgumentParser()

parser.add_argument('-?',             action='help',       help='show this help')
parser.add_argument('-v','--verbose', action='store_true', help='show detailed output')
parser.add_argument('-s','--show',    action='store_true', help='show changes')
parser.add_argument('-c','--cdata',   action='store_true', help='text as cdata')
parser.add_argument('-t','--text',    action='store',      help='set value as text value')
parser.add_argument('-T','--tfile',   action='store',      help='set value as text value taken from tfile')
parser.add_argument('-a','--attr',    action='store',      help='set value as attribute value')
parser.add_argument('-x','--xpath',   action='store',      help='xpath to apply to the file')
parser.add_argument('-n','--ns',      action='store',      help='added to context ', nargs='*', metavar='prefix=\"url\"')
parser.add_argument('file',           action='store',      help='file to parse', nargs='*')

argcomplete.autocomplete(parser)
args = parser.parse_args()

if args.verbose:
    prettyPrint(('args',vars(args)), colour=True, output=sys.stderr)

def main():

    pn = re.compile('^([^=]*)=["\']([^\'"]*)["\']$')
    ns = {}
    if args.ns:
        for nsp in args.ns:
            m = pn.match(nsp)
            if m:
                ns[m.group(1)]=m.group(2)
        if args.verbose:
            prettyPrint(('ns',ns), colour=True, output=sys.stderr)
            
    if args.attr and args.xpath:
        pa = re.compile('^(.*)/@([^@]*)$')
        m = pa.match(args.xpath)
        if m:
            xpath=m.group(1)
            attr = m.group(2)
            if args.verbose:
                sys.stderr.write('attr name=%s\n'%attr)
        else:
            sys.stderr.write('can\'t match attr from xpath=%s'%args.xpath)
    else:
        xpath = args.xpath

    for f in args.file:
        if args.show:
            sys.stderr.write('%s\n'%f)
        b='%s.bak'%f
        try:
            os.remove(b)
        except:
            None
        os.rename(f,b)
        
        (doc,ctx,nsp)=getContextFromFile(b)
        for p in ns.keys():
            ctx.xpathRegisterNs(p,ns[p])

        if args.tfile:
            with open(args.tfile) as tf:
                text = ''.join(tf.readlines())
                tf.close()
        elif args.text:
            text = args.text
        else:
            text = None
            
        res = ctx.xpathEval(xpath)
        for r in res:
            if text:
                if args.show:
                    sys.stderr.write('%s- %s%s\n'%(colours['Red'],r.content,colours['Off']))
                    sys.stderr.write('%s+ %s%s\n'%(colours['Green'],text,colours['Off']))
                if args.cdata:
                    r.setContent(None)
                    cdata = doc.newCDataBlock(text,len(text))
                    r.addChild(cdata)
                else:
                    r.setContent(text)
            if args.attr:
                if args.show:
                    sys.stderr.write('%s- %s%s\n'%(colours['Red'],r.prop(attr),colours['Off']))
                    sys.stderr.write('%s+ %s%s\n'%(colours['Green'],args.attr,colours['Off']))
                r.setProp(attr,args.attr)
                
        output = open(f,'w')
        output.write('%s'%doc)
        output.close()
    return

if __name__ == '__main__' : main()
