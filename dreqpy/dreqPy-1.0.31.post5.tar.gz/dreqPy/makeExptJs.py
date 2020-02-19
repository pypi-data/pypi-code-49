import collections, os, sys
nt__charmeEnable = collections.namedtuple( 'charme', ['id','site'] )

try:
  import dreq
  import vrev
  import misc_utils
  import rvgExtraTable
  import volsum
  import table_utils
except:
  import dreqPy.volsum as volsum
  import dreqPy.dreq as dreq
  import dreqPy.vrev as vrev
  import dreqPy.misc_utils as misc_utils
  import dreqPy.table_utils as table_utils
  import dreqPy.rvgExtraTable as rvgExtraTable

python2 = True
if sys.version_info[0] == 3:
  python2 = False
  def cmp(x,y):
    if x == y:
      return 0
    elif x > y:
      return 1
    else:
      return -1

setMlab = misc_utils.setMlab

#priority	long name	units 	comment 	questions & notes	output variable name 	standard name	unconfirmed or proposed standard name	unformatted units	cell_methods	valid min	valid max	mean absolute min	mean absolute max	positive	type	CMOR dimensions	CMOR variable name	realm	frequency	cell_measures	flag_values	flag_meanings

strkeys = [u'procNote', u'uid', u'odims', u'flag_meanings', u'prov', u'title', u'tmid', u'label', u'cell_methods', u'coords', u'cell_measures', u'spid', u'flag_values', u'description']

ntstr = collections.namedtuple( 'ntstr', strkeys )

class cmpd(object):
  def __init__(self,k):
    self.k = k
  def cmp(self,x,y):
    return cmp( x.__dict__[self.k], y.__dict__[self.k] )

class cmpd2(object):
  def __init__(self,k1,k2):
    self.k1 = k1
    self.k2 = k2
  def cmp(self,x,y):
    if x.__dict__[self.k1] == y.__dict__[self.k1]:
      return cmp( x.__dict__[self.k2], y.__dict__[self.k2] )
    else:
      return cmp( x.__dict__[self.k1], y.__dict__[self.k1] )

class cmpdn(object):
  def __init__(self,kl):
    self.kl = kl
  def cmp(self,x,y):
    for k in self.kl:
      if x.__dict__[k] != y.__dict__[k]:
        return cmp( x.__dict__[k], y.__dict__[k] )
    
    return cmp( 0,0 )

import re

class makePurl(object):
  def __init__(self):
    c1 = re.compile( '^[a-zA-Z][a-zA-Z0-9]*$' )
    mv = dq.coll['var'].items
    oo = open( 'htmlRewrite.txt', 'w' )
    for v in mv:
      if c1.match( v.label ):
         oo.write( 'RewriteRule ^%s$ http://clipc-services.ceda.ac.uk/dreq/u/%s.html\n' % (v.label,v.uid) )
      else:
         print ('Match failed: %s' % v.label )
    oo.close()
      

hdr = """
function f000(value) { return (value + "").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;") };

function formatter00(row, cell, value, columnDef, dataContext) {
        var vv = value.split(" ");
        return '<b><a href="/dreq/u/' + vv[1] + '.html">' + (vv[0] + " ").replace(/&/g,"&amp;") + '</a></b>, ';
    };
function formatter01(row, cell, value, columnDef, dataContext) { return '<i>' + f000(value) + '</i> ' };
function formatter02(row, cell, value, columnDef, dataContext) { return '[' + f000(value) + '] ' };
function formatter03(row, cell, value, columnDef, dataContext) { if (value != "'unset'"  ) { return '(' + f000(value) + ') ' } else {return ''} };
function formatter04(row, cell, value, columnDef, dataContext) { return '{' + f000(value) + '} ' };
function formatter05(row, cell, value, columnDef, dataContext) { return '&lt;' + f000(value) + '&gt; ' };

var getData  = {
cols: function() {
  var columns = [ {id:0, name:'Experiment', field:0, width: 100, formatter:formatter00 },
              {id:1, name:'Title', field:1, width: 210, formatter:formatter01 },
              {id:2, name:'MIP', field:2, width: 180, formatter:formatter02},
              {id:3, name:'Ntot', field:3, width: 180, formatter:formatter03} ];
 return columns;
},

data: function() {
var data = [];
"""
ftr = """return data;
}
};
"""
##rtmpl = 'data[%(n)s] = { "id":%(n)s, 0:"%(var)s",  1:"%(sn)s", 2:"%(ln)s", 3:"%(u)s", 4:"%(uid)s" };'
##rtmpl = 'data[%%(n)s] = { "id":%%(n)s, 0:"%(expt)s",  1:"%(ln)s", 2:"%(mip)s", 3:"%(ntot)s" };'
rtmpl = '0:"%(expt)s",  1:"%(ln)s", 2:"%(mip)s", 3:"%(ntot)s"'
rtmpl2 = 'data[%(n)s] = { "id":%(n)s, %(load)s };'

class makeJs(object):
  def __init__(self,dq):
    rl = {}
    for v in dq.coll['experiment'].items:
        expt = '%s %s' % (v.label,v.uid)
        ln = v.title
        uid = v.uid
        mip = v.mip
        ntot = v.ntot
        d = locals()
        for k in ['ln','mip']:
    
          if  d[k].find( '"' ) != -1:
            print ( "WARNING ... quote in %s .. %s [%s]" % (k,expt,d[k]) )
            d[k] =  d[k].replace( '"', "'" )
            print ( d[k] )
        
        rr = rtmpl % d
        rl[v.label] = rr
    oo = open( 'data3ex.js', 'w' )
    oo.write( hdr )
    n = 0
    for k in sorted( rl.keys() ):
      oo.write( ( rtmpl2 % {'n':n, 'load':rl[k] } ) + '\n' )
      n += 1
    oo.write( ftr )
    oo.close()

if __name__ == "__main__":
  try:
    import scope
  except:
    import dreqPy.scope as scope

  assert os.path.isdir( 'html' ), 'Before running this script you need to create "html", "html/index" and "html/u" sub-directories, or edit the call to dq.makeHtml'
  assert os.path.isdir( 'html/u' ), 'Before running this script you need to create "html", "html/index" and "html/u" sub-directories, or edit the call to dq.makeHtml, and refernces to "u" in style lines below'
  assert os.path.isdir( 'html/index' ), 'Before running this script you need to create "html", "html/index" and "html/u" sub-directories, or edit the call to dq.makeHtml, and refernces to "u" in style lines below'
  assert os.path.isdir( 'tables' ), 'Before running this script you need to create a "tables" sub-directory, or edit the table_utils.makeTab class'

  dq = dreq.loadDreq( manifest='docs/dreqManifest.txt' )
##
## add special styles to dq object "itemStyle" dictionary.
##
  mj = makeJs( dq )
