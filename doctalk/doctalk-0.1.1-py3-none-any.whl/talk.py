from collections import defaultdict
import subprocess
from pathlib import Path
import math
import networkx as nx
import statistics as stat
from pprint import pprint

from .nlp import *
from .sim import *
from .vis import pshow,gshow

client = NLPclient()

def run_with(fname,query=True) :
  '''
  Activates dialog about document in <fname>.txt with questions
  in <fname>_quests.txt
  Assumes stanford corenlp server listening on port 9000
  with annotators listed in params.py  available.
  '''
  t = Talker(from_file=fname+'.txt')
  show =t.params.show_pics

  t.show_all()
  if query:
    t.query_with(fname+'_quest.txt')
    pshow(t,file_name=fname+"_quest.txt",
          cloud_size=t.params.cloud_size,
          show=t.params.show_pics)

def run_with_pdf(fname,**kwargs) :
  pdf2txt(fname+".pdf")
  run_with(fname, **kwargs)

def chat_about(fname,qs=None) :
  t = Talker(from_file=fname + '.txt')
  show = t.params.show_pics
  t.show_all()
  t.query_with(qs)



def tprint(*args) :
  ''' custom print when trance on'''
  if trace : print(*args)


def tload(infile) :
  ''' load a .txt file'''
  tprint('LOADING:',infile,'\n')
  with open(infile, 'r') as f: text = f.read()
  return digest(text)

def jload(infile) :
  ''' loads .json file, preprocessed from a .txt file'''
  with open(infile, 'r') as f:
    res = json.load(f)
    return res

def jsave(infile,outfile):
  '''preprocesses a .txt file to a .json file'''
  d=tload(infile)
  with open(outfile,'w') as g:
    json.dump(d,g,indent=0)

def exists_file(fname) :
  '''true when a file exists'''
  path = Path(fname)
  return path.is_file()

def load(fname,force=0) :
  '''loads a .txt file or its .json file if it exists'''
  if fname[-4:]==".txt":
    if force:
      db = tload(fname)
    else :
      jfname=fname[:-4]+".json"
      if not exists_file(jfname) :
        jsave(fname,jfname)
      db=jload(jfname)
  else:
    db = jload(fname)
  return db

def get_quests(qs) :
  ''' decodes questions from list or file'''
  if not isinstance(qs,list) :
    qfname=qs
    with open(qfname,'r') as f:
      qs = list(l.strip() for l in f)
  return qs

def digest(text) :
  ''' process text with the NLP toolkit'''
  l2occ = defaultdict(list)
  sent_data=[]
  # calls server here
  for i,xss in enumerate(client.extract(text)) :
    lexs,deps,ies=xss
    sent,lemma,tag,ner=[],[],[],[]
    for j,t in enumerate(lexs):
      w,l,p,n=t
      wi=len(l2occ)
      l2occ[l].append((i,j))
      sent.append(w)
      lemma.append(l)
      tag.append(p)
      ner.append(n)
    d=(tuple(sent),tuple(lemma),tuple(tag),
       tuple(ner),tuple(deps),tuple(ies))
    sent_data.append(d)
  return sent_data,l2occ

SENT,LEMMA,TAG,NER,DEP,IE=0,1,2,3,4,5

def rel_from(d):
  ''' extracts several relations as SVO triplets'''
  def to_lems(ux):
    f,t=ux
    if f>=0:
      for u in range(*ux):
        yield lemma[u],tag[u]
  def lems(xs) : return tuple(x[0] for x in xs)
  rs,svos=set(),set()
  for ts in d[IE] :
    for t in ts :
      sx, vx, ox = t
      lemma = d[LEMMA]
      tag=d[TAG]
      sub = tuple(to_lems(sx))
      rel = tuple(to_lems(vx))
      ob = tuple(to_lems(ox))
      res = (sub, rel, ob)
      s=()
      for l,tl in sub:
        if tl[0]=='N' :
          s=l
      o=()
      for l, tl in ob:
        if tl[0] == 'N':
          o = l
      v=()
      for l, tl in rel:
        if tl[0] == 'V':
          v = l
      rs.add(res)
      svo=s,v,o
      if () in svo or s==o : continue
      svos.add(svo)
      if len(sub)>1 : svos.add((s,'subject_in',lems(sub)))
      if len(ob) > 1 : svos.add((o, 'object_in', lems(ob)))
      if len(rel)>1 : svos.add((v, 'verb_in', lems(rel)))

  return tuple(rs),tuple(svos)

def dep_from(id,d):
  ''' extracts dependenciy relations deom given sentece id'''
  deps=d[DEP]
  lemmas=d[LEMMA]
  tags=d[TAG]
  for dep in deps :
    f, r, t = dep
    if t == -1 : target,ttag=id,'SENT'
    else: target,ttag = lemmas[t],tags[t]
    res = lemmas[f],tags[f],r,target,ttag
    yield res

def deps_from(id,d) :
  ''' extracts all dependency relations as nexted tuples'''
  return tuple(t for t in dep_from(id,d))

def comp_from(id,d) :
  '''turns compound annotations into pairs'''
  for x in dep_from(id,d) :
    f,tf,rel,t,tt=x
    if rel in ('compound', 'amod', 'conj:and') and \
       good_word(f) and good_word(t) and \
       good_tag(tf) and good_tag(tt) :
      yield (f,t)

def comps_from(id,d) :
  ''' returns compounds in sentence id as nested tuples of positions'''
  return tuple(t for t in comp_from(id,d) if t)

def sub_centered(id,dep,all_to_sent=True) :
  '''builds dependency graphs centered on subjects and sentences'''
  f, f_, r, t, t_ = dep
  if r == 'punct' or f == t:
    pass
  elif r in ['nsubj'] and f_[0] == 'N':
    yield (id, f)  # sent to subject
    yield (f, id)  # subject to sent
    yield (t, f)  # pred to subject
  elif r in ['nsubj', 'dobj', 'iobj'] : #or t_[0] == 'V':
    if good_word(t) and good_word(f) :
      yield f, t  # arg to pred
      yield t, id  # pred to sent
  # elif r == 'ROOT': yield (f, t)
  else:
    yield (f, t)
    if all_to_sent:
      yield (f,id)


def pred_mediated(id,dep) :
  '''build dependency graphs mediated by predicates'''
  f, f_, r, t, t_ = dep
  if r == 'punct' or f==t:
    pass
  elif r in ['nsubj', 'dobj', 'iobj'] or t_[0] == 'V':
    yield (id, f)  # sent to predicate
    if good_word(t) and good_word(f) : yield t,f  #  pred to arg
    if good_word(t) : yield id, t  # sent to pred
    yield (f, id)  # arg to sent
  elif r == 'ROOT':
    yield (t, f)
  else:
    yield (f, t)


def get_avg_len(db) :
  ''' returns average length of sentences'''
  sent_data,_=db
  lens=[len(x[LEMMA]) for x in sent_data]
  n=len(lens)
  s=sum(lens)
  return round(s/n)

def rank_sort(pr) :
  ''' sort dict by ranks associatied to its keys'''
  by_rank=[(x,r) for (x,r) in pr.items()]
  by_rank.sort(key=lambda x : x[1],reverse=True)
  return by_rank

def ners_from(d):
  ''' extracts useful named entities'''
  ners=[]
  for j, ner in enumerate(d[NER]):
    lemma = d[LEMMA][j]
    if ner != 'O' and good_word(lemma): ners.append((lemma,ner))
  return tuple(ners)

def materialize(db) :
  '''converts relations from positions to actual lemmas'''
  sent_data,l2occ= db
  for i,d in enumerate(sent_data) :
      rels,svos = rel_from(d)
      deps=deps_from(i,d)
      comps=comps_from(i,d) # or directly from deps
      ners=ners_from(d)
      yield tuple(d[SENT]),tuple(d[LEMMA]),tuple(d[TAG]),\
            ners,rels,svos,deps,comps

def wn_from(l2occ) :
  '''extracts likely WordNet relations between lemmas'''
  for w in l2occ :
    if not good_word(w) : continue
    for s,v,o in wn_svo(2,10,w,'n') :
      if l2occ.get(o) :
        yield (s,v,o)
    for s, v, o in wn_svo(2, 10, w, 'v'):
      if l2occ.get(o):
        yield (s, v, o)
    for s, v, o in wn_svo(2, 10, w, 'a'):
      if l2occ.get(o):
        yield (s, v, o)

def v2rel(v) :
  '''rewrites "be" lemma to is'''
  if v=='be' : return 'is'
  return v

def e2rel(e) :
  '''turns NER tags into common words'''
  if e=='MISC' : return 'entity'
  return e.lower()

def answer_quest(q,talker) :
  '''
  given question q, interacts with talker and returns
  its best answers
  '''
  max_answers = talker.params.max_answers
  db = talker.db
  sent_data, l2occ = db
  matches = defaultdict(set)
  nears = defaultdict(set)
  answerer = Talker(from_text=q)
  q_sent_data, q_l2occ = answerer.db
  unknowns = []
  for j, q_lemma in enumerate(q_sent_data[0][LEMMA]):
    q_tag = q_sent_data[0][TAG][j]
    if q_tag[0] not in "NVJ": continue  # ppp(q_lemma,q_tag)
    if not good_word(q_lemma) or q_lemma in ".?": continue

    ys = l2occ.get(q_lemma)

    if not ys:
      unknowns.append(q_lemma)
    else:
      for sent, _pos in ys:
        matches[sent].add(q_lemma)
    if talker.params.expand_query > 0:
      related = wn_all(talker.params.expand_query, 3, q_lemma, wn_tag(q_tag))
      for r_lemma in related:
        if not good_word(q_lemma): continue
        zs = l2occ.get(r_lemma)
        if not zs: continue
        for r_sent, _r_pos in zs:
          nears[r_sent].add((r_lemma, q_lemma))
        if zs and not ys:
          if q_lemma in unknowns: unknowns.pop()
        tprint('EXPANDED:', q_lemma, '-->', r_lemma)
  tprint('')
  if unknowns: tprint("UNKNOWNS:", unknowns, '\n')

  best = []
  if talker.params.pers:
    d = {x: r for x, r in answerer.pr.items() if good_word(x)}
    talker.pr = nx.pagerank(talker.g, personalization=d)

  for (id, shared) in matches.items():
    sent = sent_data[id][SENT]
    r = answer_rank(id, shared, sent, talker, expanded=0)
    # ppp(id,r,shared)
    best.append((r, id, shared, sent))
    # ppp('MATCH', id,shared, r)

  for (id, shared_source) in nears.items():
    shared = {x for x, _ in shared_source}
    sent = sent_data[id][SENT]
    r = answer_rank(id, shared, sent, talker, expanded=1)
    best.append((r, id, shared, sent))
    # ppp('EXPAND', id,shared, r)

  best.sort(reverse=True)

  answers = []
  #ppp(max_answers)
  for i, b in enumerate(best):
    if i >= max_answers: break
    #ppp(i,b)
    rank, id, shared, sent = b
    answers.append((id, sent, round(rank, 4), shared))
  if not talker.params.answers_by_rank: answers.sort()
  return answers, answerer


def sigmoid(x): return 1 / (1 + math.exp(-x))

def answer_rank(id,shared,sent,talker,expanded=0) :
  '''ranks answer sentence id using several parameters'''

  lshared = len(shared)
  if not lshared : return 0

  sent_count=len(talker.db[0])
  word_count=len(talker.db[1])

  lsent = len(sent)
  lavg=talker.avg_len
  srank=talker.pr.get(id)


  nrank=normalize_sent(srank,lsent,lavg)

  if nrank==0 : return 0

  def get_occ_count(x): return len(talker.db[1].get(x))

  unusual = sigmoid(1 - stat.harmonic_mean(
    get_occ_count(x) for x in shared) / sent_count)

  important=math.exp(nrank)

  # #r=stat.harmonic_mean((lshared,important,unusual))
  r=lshared*important*unusual

  if expanded : r=r/2

  #ppp('RANKS:',10000*srank,'-->',10000*nrank,lsent,lavg)
  #ppp('HOW  :', id, lshared, unusual, important, shared,'--->',r)

  #r=math.tanh(r)
  return r

def query_with(talker,qs_or_fname)     :
  ''' queries talker with questions from file or list'''
  if isinstance(qs_or_fname,str) :
    qs = get_quests(qs_or_fname) # file name
  else :
    qs=qs_or_fname # list of questions or None
  if qs:
    for q in qs :
      if not q :break
      interact(q,talker)
  else:
    while True:
      q=input('> ')
      if not q : break
      interact(q,talker)

def interact(q,talker):
  ''' prints/says query and answers'''
  tprint('----- QUERY ----\n')
  print("QUESTION: ",end='')
  talker.say(q)
  print('')
  ### answer is computed here ###
  answers,_=answer_quest(q, talker)
  show_answers(talker,answers)
  talker.distill(q)

def show_answers(talker,answers) :
  ''' prints out/says answers'''
  print('ANSWERS:')
  for info, sent, rank, shared in answers:
    print(info,end=': ')
    talker.say(nice(sent))
    tprint('  ', shared, rank)
  print('')
  tprint('------END-------', '\n')

class Talker :
  '''
  class aggregating summary, keyphrase, relation extraction
  as well as query answering in the form of extracted sentences
  based on given file or text
  '''
  def __init__(self,from_file=None,from_text=None,params=talk_params()):
    '''creates data container from file or text document'''
    self.params=params
    self.show_pics=params.show_pics
    self.sum_count = params.sum_count
    self.key_count = params.key_count
    self.from_file=from_file
    if from_file:
       self.db=load(from_file,self.params.force)
       self.from_file=from_file
    elif from_text :
       self.db=digest(from_text)
    else :
      assert from_file or from_text

    self.avg_len = get_avg_len(self.db)

    self.svos=self.to_svos()

    self.g,self.pr=self.to_graph()
    #self.get_sum_and_words(sk,wk)
    self.summary, self.keywords = \
      self.extract_content(self.sum_count, self.key_count)

  def answer_quest(self,q):
    '''answers question q'''
    return answer_quest(q,self)

  def query_with(self,qs):
    '''answers list of questions'''
    query_with(self,qs)

  def get_tagged(self,w):
    '''adds tags to given lemma w'''
    l2occ=self.db[1]
    sent_data=self.db[0]
    occs=l2occ.get(w)
    if not occs : return None

    tags=set()
    words=set()
    for i,j in occs:
      word = sent_data[i][SENT][j]
      tag=sent_data[i][TAG][j]
      words.add(word)
      tags.add(tag)
    return words,tags

  def get_occs(self,lemma):
    return self.db[1].get(lemma)

  def to_ids(self,nodes) :
    ids=set()
    for w in nodes :
      occs=self.get_occs(w)
      if not occs : continue
      for occ in self.get_occs(w) :
        ids.add(occ[0])
    #return {occ[0] for w in nodes for occ in self.get_occs(w)}
    return ids


  def adjust_sent_ranks(self,pr):
    npr = dict()
    for x, r in pr.items():
      if isinstance(x, int):
        ws = self.db[0][x][SENT]
        r = normalize_sent(r, len(ws), self.avg_len)
      npr[x] = r
    return npr

  def get_sentence(self,i):
    ''' returns sentence i as list of words'''
    return  self.db[0][i][SENT]

  def get_lemma(self,i):
    ''' returns lemmas of sentence i as list of words'''
    return  self.db[0][i][LEMMA]

  def get_tag(self,i):
    ''' gets the POS tags of sentence i'''
    return  self.db[0][i][TAG]

  def get_ner(self,i):
    ''' gets the named entity annotations of sentence i'''
    ner=  self.db[0][i][NER]
    if ner=='O' : return None
    return ner

  def extract_content(self,sk,wk):
    '''extracts summaries and keywords'''
    def nice_word(x,good_tags='N') :
      ws_ts=self.get_tagged(x)
      if not ws_ts : return None
      ws, tags = ws_ts
      ncount = 0
      for tag in tags:
        if tag[0] in good_tags:
          ncount += 1
      if ncount > len(tags) // 2:
        cx = x.capitalize()
        if cx in ws: x = cx
        return x
      else:
        return None
    sents,words=list(),set()

    '''
    npr=dict()
    for x,r in self.pr.items() :
      if isinstance(x,int) :
        ws = self.db[0][x][SENT]
        r=normalize_sent(r,len(ws),self.avg_len)
      npr[x]=r
    '''
    npr=self.adjust_sent_ranks(self.pr)

    by_rank=rank_sort(npr)
    for i  in range(len(by_rank)):
      x,r=by_rank[i]
      if sk and isinstance(x,int) :
        ws=self.db[0][x][SENT]
        sk-=1
        sents.append((r,x,ws))
      elif wk and good_word(x) :
        x=nice_word(x)
        if x:
          wk -= 1
          words.add(x)
      elif wk and isinstance(x,tuple) :
          xs=tuple(map(nice_word,x))
          if all(xs) :
            #ppp('KWD', x, 1000 * r)

            wk -= 1
            words.add(xs)
    sents.sort(key=lambda x: x[1])
    summary=[(r,x,ws) for (r,x,ws) in sents]
    self.by_rank=by_rank # to be used when needed
    for xs in words.copy() :
      if isinstance(xs,tuple) :
        for w in xs:
          if w in words:
            words.remove(w)
    return summary,words

    def distill(self,q) :
      '''
      superclasses can do here additional
      processing of question q
      '''
      pass

  def to_svos(self):
    '''
    returns SVO relations as a dict associating to each
    SVO tuple the set of the sentences it comes from
    '''
    sent_data, l2occ = self.db
    d = defaultdict(set)
    for i, data in enumerate(sent_data):
      rels, svos = rel_from(data)
      comps = comps_from(i, data)  # or directly from deps
      ners = ners_from(data)
      for s, v, o in svos: #ok
        if s!=o and good_word(s) and good_word(o) :
           d[(s, v2rel(v), o)].add(i)
      for x, e in ners: #ok
        d[(e2rel(e), 'has_instance', x)].add(i)

      for a, b in comps: #ok
        c = join(a, b)
        d[(a, 'as_in', c)].add(i)
        d[(b, 'as_in', c)].add(i)

    for svo in wn_from(l2occ):
      s,v,o=svo
      if s==o : continue
      s_occs=set()
      o_occs=set()
      for  id,_ in l2occ.get(s) :
        s_occs.add(id)
      for id, _ in l2occ.get(o):
        o_occs.add(id)
      shared_occs=s_occs.intersection(o_occs)
      if shared_occs :
        d[svo]=s_occs.intersection(o_occs)

    return d

  def to_svo_graph(self):
    ''' exposes svo relations as a graph'''
    g=nx.DiGraph()
    for svo,occs in self.svos.items() :
      s,v,o=svo
      g.add_edge(s,o,rel=v,occs=occs)
    return g

  def to_edges_in(self,id,sd):
    '''yields edges from dependency structure of sentence id'''
    for dep in dep_from(id, sd):
      if self.params.subject_centered:
        yield from sub_centered(id, dep,all_to_sent=self.params.all_to_sent)
      else:
        yield from pred_mediated(id, dep)
    if self.params.compounds:
      for ft in comps_from(id, sd):
        f, t = ft
        yield f, ft  # parts to compound
        yield t, ft
        yield ft, id  # compound to sent


  def to_edges(self):
    '''yields all edges from syntactic dependency structure'''
    sent_data, l2occ = self.db
    for id, sd in enumerate(sent_data):
      yield from self.to_edges_in(id, sd)
    # nouns may also point to the first sent where they are "defined"
    if self.params.use_to_def:
      for lemma,occs in l2occ.items() :
        if occs and good_word(lemma):
          id,pos=occs[0]
          tag = sent_data[id][TAG][pos]
          if  good_tag(tag) : #,starts='N') :
            yield lemma,id
            # pumping senteces through word towards first
            # in which it occurs
            for i,occ in enumerate(occs) :
              if i>0:
                yield occ[0],lemma

  def to_graph(self, personalization=None):
    ''' builds document graph from several link types'''
    db=self.db
    svos=self.svos
    g = nx.DiGraph()
    for e in self.to_edges():
      f, t = e
      g.add_edge(f, t)
    if self.params.svo_edges:
      for s, v, o in svos:
        if s == o: continue
        if v == 'as_in':
          g.add_edge(s, o)
        elif v not in {'as_in'}  : #elif v in ('kind_of', 'part_of', 'is_like'):
          g.add_edge(o, s)
          g.add_edge(s, o)
          # ppp(s,v,o)

    try:
      pr = nx.pagerank(g, personalization=personalization)
    except:
      n = g.number_of_nodes()
      pr = dict()
      for l in db[1]: pr[l] = 1 / n
    return g, pr

  def to_prolog(self):
    ''' generates a Prolog representation of a document's content'''
    if not self.from_file : return
    fname=self.from_file[:-4]
    with open(fname+".pro",'w') as f :
      sent_data,l2occ=self.db
      f.write('% SENTENCES: \n')
      for i,data in enumerate(sent_data) :
        ws=list(data[SENT])
        f.write(f'sent({i},{ws}).\n')
      f.write('\n% LEMMAS: \n')
      for i, data in enumerate(sent_data):
        ws = list(data[LEMMA])
        f.write(f'lemma({i},{ws}).\n')
      f.write('\n% RELATIONS: \n')
      for svo,occs in self.svos.items() :
        s,v,o=svo
        occs=sorted(occs)
        f.write(f'svo{s,v,o,occs}.\n')

  def distill(self, q):
    pass

  def say(self,what):
    ''' prints and ptionally says it, unless set to quiet'''
    print(what)
    if not self.params.quiet: subprocess.run(["say", what])


  def show_summary(self):
    ''' prints/says summary'''
    self.say('SUMMARY:')
    for r,x,ws in self.summary:
      print(x,end=': ')
      self.say(nice(ws))
    print('')

  def show_keywords(self):
    ''' prints keywords'''
    print('KEYWORDS:')
    print(self.keywords)
    print('')


  def save_summary(self,out_file):
    with open(out_file,'w') as g:
      for _, _, ws in self.summary:
        print(nice(ws),file=g)

  def save_keywords(self,out_file):
    with open(out_file,'w') as g:
      for w in self.keywords:
        print(w,file=g)

  def show_rels(self):
    ''' prints extracted relations'''
    print('RELATIONS:')
    for svoi in self.svos.items():
       print(svoi)

  def show_svos(self):
    show = self.params.show_pics
    g = self.to_svo_graph()
    seeds = take(self.params.subgraph_size,
          [x for x, r in rank_sort(self.pr) if isinstance(x, str)])
    g = g.subgraph(seeds)
    self.show_svo_graph(g,file_name=self.from_file)

  def show_all(self):
    ''' prints out sevaral results'''
    if self.from_file :
      print('\n--------------  FILE:',self.from_file,'-----------\n')
    show = self.params.show_pics
    self.show_summary()
    self.show_keywords()
    self.show_stats()
    if self.params.show_rels:
      self.show_rels()
    if self.params.to_prolog :
      self.to_prolog()
    if show and self.from_file:
      pshow(self, file_name=self.from_file)
      self.show_svos()

  def show_stats(self):
    ''' prints out some staistics'''
    print('SENTENCES:',len(self.db[0]))
    print('LEMMAS:', len(self.db[1]))
    print('GRAPH NODES:', self.g.number_of_nodes())
    print('GRAPH EDGES:',self.g.number_of_edges())
    print('SVO RELATIONS:', len(self.svos))
    print('')

  def show_svo_graph(self,g,file_name='temp.txt'):
    ''' depicts the subgraph of the highest ranked nodes in the SVO graph'''
    size = self.params.subgraph_size
    show = self.params.show_pics
    if size > 0:
      pr = nx.pagerank(g)
      best = set(take(size, [x[0] for x in rank_sort(pr)]))
      g = g.subgraph(best)
    fname = file_name[:-4] + "_svo.gv"
    gshow(g, file_name=fname, attr='rel', show=show)


# helpers
def nice(ws) :
  ''' aggregates word lists into a nicer looking sentence'''
  ws=[cleaned(w) for w in ws]
  sent=" ".join(ws)
  #print(sent)
  sent=sent.replace(" 's","'s")
  sent=sent.replace(" ,",",")
  sent=sent.replace(" .",".")
  sent = sent.replace('``', '"')
  sent = sent.replace("''", '"')
  return sent


def normalize_sent(r,sent_len,avg_len):
  '''
  normalizes the ranking of sentences
  based on effect of their length on ranking
  also reduces chances that noisy short sentences that might have
  passed through the NLP toolkit make it into summaries or answers
  '''
  if not r:
    r=0
  if sent_len > 2*avg_len or sent_len < min(5,avg_len/4) :
    return 0
  factor =  1/(1+abs(sent_len-avg_len)+sent_len)
  #ppp("NORM:",factor,r,sent_len,avg_len)
  return r*factor

def good_word(w) :
  '''
  ensures that most noise words are avoided
  '''
  return isinstance(w,str) and len(w)>1 and w.isalpha() \
         and w not in stop_words

def good_tag(tag,starts="NVJA"):
  ''' true for noun,verb, adjective and adverb tags'''
  c=tag[0]
  return c in starts

def distinct(g) :
  '''ensures repetititions are removed from a generator'''
  seen=set()
  for x in g :
    if not x in seen :
      seen.add(x)
      yield x

def take(k,g) :
  ''' generates only the first k elements of a sequence'''
  for i,x in enumerate(g) :
    if i>=k : break
    yield x

# pdf to txt conversion with external tool - optional

def pdf2txt(fname) :
  subprocess.run(["pdftotext", fname])

# extracts file name from path
def path2fname(path) :
  return path.split('/')[-1]

# trimms suffix
def trimSuf(path) :
  return ''.join(path.split('.')[:-1])

def justFname(path) :
  return trimSuf(path2fname(path))


