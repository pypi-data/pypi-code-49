from .params import *
from graphviz import Digraph as DotGraph
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def showGraph(dot, show=True, file_name='textgraph.gv'):
  dot.render(file_name, view=show)

def gshow(g, attr=None, file_name='temp.gv', show=1):
  dot = DotGraph()
  for e in g.edges():
    f, t = e
    if not attr : w= ''
    else : w = g[f][t][attr]
    dot.edge(str(f), str(t), label=str(w))
  dot.render(file_name, view=show>1)

def pshow(t, file_name="temp",cloud_size=24,show=1):
  file_name=file_name[:-4]
  def t2s(x) :
    if isinstance(x,tuple) :
      return " ".join(x)
    return x
  sum, kws = t.extract_content(5, cloud_size)
  #for x in t.by_rank:ppp(x)
  d=dict()
  s=set()
  for kw in kws:
    if isinstance(kw,tuple) :
      kw0=tuple(map(lambda x: x.lower(),kw))
      d[t2s(kw)]=t.pr[kw0]
      s.add(kw0)
    else :
      lkw=kw.lower()
      d[kw]=t.pr[lkw]
      s.add(lkw)
  #ppp("CLOUD",d)
  show_ranks(d,file_name=file_name+"_cloud.pdf",show=show)
  #ppp('SUBGRAPH',s)
  if t.g.number_of_edges()<80:
    topg=t.g
  else :
     topg=t.g.subgraph(s)
  #ppp('TOPG', topg.number_of_edges())
  gshow(topg,file_name=file_name+".gv",show=show)

def show_ranks(rank_dict,file_name="cloud.pdf",show=1) :
  cloud=WordCloud(width=800,height=400)
  cloud.fit_words(rank_dict)
  f=plt.figure()
  plt.imshow(cloud, interpolation='bilinear')
  plt.axis("off")
  if show>1 : plt.show()
  f.savefig(file_name,bbox_inches='tight')
  plt.close('all')
