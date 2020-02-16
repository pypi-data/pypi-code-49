#coding:utf8
#author:puluterYu(based On cgitb)
import _thread
import inspect
import keyword
import linecache
import os
import pydoc
import sys
import tempfile
import time
import tokenize
import traceback

codeText = ""
__UNDEF__ = []                          # a special sentinel object

def lookup(name, frame, locals):
    """Find the value for a given name in the given environment."""
    if name in locals:
        return 'local', locals[name]
    if name in frame.f_globals:
        return 'global', frame.f_globals[name]
    if '__builtins__' in frame.f_globals:
        builtins = frame.f_globals['__builtins__']
        if type(builtins) is type({}):
            if name in builtins:
                return 'builtin', builtins[name]
        else:
            if hasattr(builtins, name):
                return 'builtin', getattr(builtins, name)
    return None, __UNDEF__

def scanvars(reader, frame, locals):
    """Scan one logical line of Python and look up values of variables used."""
    vars, lasttoken, parent, prefix, value = [], None, None, '', __UNDEF__
    for ttype, token, start, end, line in tokenize.generate_tokens(reader):
        if ttype == tokenize.NEWLINE: break
        if ttype == tokenize.NAME and token not in keyword.kwlist:
            if lasttoken == '.':
                if parent is not __UNDEF__:
                    value = getattr(parent, token, __UNDEF__)
                    vars.append((prefix + token, prefix, value))
            else:
                where, value = lookup(token, frame, locals)
                vars.append((token, where, value))
        elif token == '.':
            prefix += lasttoken + '.'
            parent = value
        else:
            parent, prefix = None, ''
        lasttoken = token
    return vars

def text(einfo, context=5):
    global codeText
    """Return a plain text document describing a given traceback."""
    etype, evalue, etb = einfo
    if isinstance(etype, type):
        etype = etype.__name__
    pyver = 'Python ' + sys.version.split()[0] + ': ' + sys.executable
    date = time.ctime(time.time())
    head = "[=====Basic Part=====]\n%s\n%s\n%s" % (str(etype), pyver, date) 
    codeText = inspect.getinnerframes(etb, 10000)
    frames = []
    records = inspect.getinnerframes(etb, context)
    for frame, file, lnum, func, lines, index in records:
        file = file and os.path.abspath(file) or '?'
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        call = ''
        if func != '?':
            call = 'in ' + func + \
                inspect.formatargvalues(args, varargs, varkw, locals,
                    formatvalue=lambda value: '=' + pydoc.text.repr(value))

        highlight = {}
        def reader(lnum=[lnum]):
            highlight[lnum[0]] = 1
            try: return linecache.getline(file, lnum[0])
            finally: lnum[0] += 1
        vars = scanvars(reader, frame, locals)
        rows = []
        rows.append("[====================]\n\n\n[=====Data Part=====]")
        done, dump = {}, []
        for name, where, value in vars:
            if name in done: continue
            done[name] = 1
            if value is not __UNDEF__:
                if where == 'global': name = 'global ' + name
                elif where != 'local': name = where + name.split('.')[-1]
                dump.append('%s = %s' % (name, pydoc.text.repr(value)))
            else:
                dump.append(name + ' undefined')

        rows.append('\n'.join(dump))
        rows.append('[===================]\n\n\n[=====Raw Error=====]')
        frames.append('\n%s\n' % '\n'.join(rows))

    exception = ['%s: %s' % (str(etype), str(evalue))]

    return head + ''.join(frames) + ''.join(exception) + '''

    The above is a description of an error in a Python program.  Here is
    the original traceback:

    %s
    ''' % ''.join(traceback.format_exception(etype, evalue, etb))+"\n[===================]"

class Hook:
    
    """A hook to replace sys.excepthook that shows tracebacks in HTML."""

    def __init__(self, display=1, logdir=None, context=5, file=None,
                 format="html"):
        self.display = display          # send tracebacks to browser if true
        self.logdir = logdir            # log tracebacks to files if not None
        self.context = context          # number of source code lines per frame
        self.file = file or sys.stdout  # place to send the output
        self.format = format

    def __call__(self, etype, evalue, etb):
        self.handle((etype, evalue, etb))

    def handle(self, info=None):
        global codeText
        info = info or sys.exc_info()

        formatter = text
        plain = False
        try:
            doc = formatter(info, self.context)
        except:                         # just in case something goes wrong
            doc = ''.join(traceback.format_exception(*info))
            plain = True

        if self.display:
            if plain:
                doc = pydoc.html.escape(doc)
                self.file.write('<pre>' + doc + '</pre>\n')
        else:
            self.file.write('<p>A problem occurred in a Python script.\n')

        if self.logdir is not None:
            suffix = ['.txt', '.html'][self.format=="html"]
            (fd, path) = tempfile.mkstemp(suffix=suffix,prefix="pkmq-", dir=self.logdir)

            try:
                with os.fdopen(fd, 'w') as file:
                    file.write(doc)
                msg = '%s contains the description of this error.' % path
            except:
                msg = 'Tried to save traceback to %s, but failed.' % path

            if self.format == 'html':
                self.file.write('<p>%s</p>\n' % msg)
            codes = codeText[0].code_context
            for l in range(len(codes)):
                codes[l] = '%5d ' % (l+1) + codes[l].rstrip() + "\n"
            res = "[Author: PuluterYu]\n\n\n[=====Raw Code Part=====]\n"+"".join(codes) + "[=======================]\n\n\n\n" + doc
            with open("./yuLog.txt","w") as f:
                f.write(res)
            
        try:
            self.file.write('发生异常，代码及报错已保存到./yuLog.txt\n请双击打开文件，并复制全部内容，粘贴到qq群内寻求帮助')
        except: pass

handler = Hook().handle
def enable(display=1, logdir=None, context=5, format="html"):
    """Install an exception handler that formats tracebacks as HTML.

    The optional argument 'display' can be set to 0 to suppress sending the
    traceback to the browser, and 'logdir' can be set to a directory to cause
    tracebacks to be written to files there."""
    sys.excepthook = Hook(display=display, logdir=logdir,
                          context=context, format=format)

if not os.path.exists("./logs"): os.mkdir("logs")
enable(logdir="./logs/",format='text')