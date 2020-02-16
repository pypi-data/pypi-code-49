from .talk import *

def extend_wh(lemmas) :
  ''' ads possible NER targets for wh words'''
  xs=set()
  if 'who' in  lemmas:
    xs.update({'person', 'title', 'organization'})
  if 'when' in lemmas:
    xs.update({'time', 'duration', 'date'})
  if 'where' in lemmas:
    xs.update({'location', 'organization', 'city', 'state_or_province', 'country'})
  if 'how' in lemmas and ('much' in lemmas or 'many' in lemmas):
    xs.update({'money', 'number', 'ordinal'})
  if 'what' in lemmas and 'time' in lemmas:
    xs.update({'time', 'duration', 'date'})
  return xs

class Thinker(Talker) :
  '''
  extends Talker with multi-hop resoning over SVOs
  using graph algorithms
  '''
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.svo_graph = self.to_svo_graph()
    self.rels= (
      'as_in','is_like','kind_of', 'part_of','has_instance'
      'subject_in', 'object_in', 'verb_in')
    self.no_rels=() #'kind_of',) #('object_in', 'verb_in','kind_of')


  def distill(self,q):
    ''' handler for question q asked from this Thinker'''
    ppp('QUESTION:',q,'\n')
    answers,answerer=self.answer_quest(q)
    #show_answers(self,answers)
    self.reason_about(answers,answerer)

  def extract_rels(self,G,good_lemmas):
    depth = self.params.think_depth
    xs = reach_from(G, depth, good_lemmas)
    R = G.reverse(copy=False)
    ys = reach_from(R, depth, good_lemmas, reverse=True)
    rels = xs.union(ys)
    return rels

  def get_roots(self,lems,tags):
    lts = zip(lems, tags)
    good_lemmas = {l for (l, t) in lts if good_word(l) and good_tag(t)}

    G = without_rels(self.svo_graph, self.no_rels)

    rels=self.extract_rels(G,good_lemmas)

    good_nodes = {a for x in rels for a in (x[0], x[2])}
    shared = {x for x in good_lemmas if self.get_occs(x)}
    good_nodes.update(shared)
    return G,good_lemmas,good_nodes,rels

  def rerank_answers(self,G,good_nodes,answerer):
    ids = self.to_ids(good_nodes)
    reached = good_nodes.union(ids)
    ReachedG = self.g.subgraph(reached)
    pers_dict = {x: r for (x, r) in answerer.pr.items() if good_word(x)}
    pr = nx.pagerank(ReachedG, personalization=pers_dict)
    ppp('HERE')
    npr=self.adjust_sent_ranks(pr)
    best = take(self.params.max_answers,
                [x for x in rank_sort(npr) if isinstance(x[0], int)])

    return best,ReachedG

  def reason_about(self,answers,answerer):
    ''' adds relational resoning, shows  answers and raltions'''
    lems = answerer.get_lemma(0)
    tags=answerer.get_tag(0)

    SVO_G,good_lemmas,good_nodes,rels=self.get_roots(lems,tags)

    best,ReachedG=self.rerank_answers(SVO_G,good_nodes,answerer)
    ReachedNodesG = ReachedG.subgraph(good_nodes)
    #S = G.subgraph(good_nodes)
    #ppp(SVO_G.number_of_edges())
    #for x,y in SVO_G.edges() : ppp(x,y,SVO_G[x][y]['rel'])
    #ppp(ReachedG.number_of_edges())
    #ppp(ReachedNodesG.number_of_edges())
    for x in good_lemmas:
      if x in ReachedNodesG.nodes():
       for ps in nx.single_source_shortest_path(ReachedNodesG,x,
                 cutoff=self.params.think_depth):
         if isinstance(ps, tuple) :
           tprint('REASONING_PATH:',x,':',ps)
       tprint('')
    tprint('')


    tprint('ROOT LEMMAS:')
    tprint(good_lemmas,'\n')

    tprint('RELATIONS FROM QUERY TO DOCUMENT:\n')
    for r in rels: tprint(r)
    tprint('')

    tprint('RELATION NODES:',len(good_nodes),
      good_nodes,'\n')

    print('\nDISTILLED ANSWERS:\n')
    for x in best :
      print(x[0],nice(self.get_sentence(x[0])),'\n')

    if self.params.show_pics>0 :
      self.show_svo_graph(SVO_G)
      gshow(ReachedG,file_name='reached.gv',show=self.params.show_pics)




def reach_from(g,k,roots,reverse=False):
    edges=set()
    for x in roots :
      if not x in g.nodes() : continue
      xs = nx.bfs_edges(g,x,depth_limit=k)
      for e in xs :
        a,b=e
        #ppp(e)
        if b in roots or a in roots :
          rel=g[a][b]['rel']
          edge= (b,rel,a) if reverse  else  (a,rel,b)
          edges.add((a,rel,b))
    return edges

def chain(g, here, there):
    try:
      p = list(nx.all_shortest_paths(g, here, there,method='bellman-ford'))
    except :
      p = []
    return p

def near_in(g,x) :
  '''
  returns all 1 or 2 level neighbors of x in g
  '''
  xs1=nx.neighbors(g,x)
  return xs1
  xs2=set(y for x in xs1 for y in nx.neighbors(g,x))
  return xs2.union(xs1)

def as_undir(g) :
  '''view of g as an undirected graph'''
  return g.to_undirected(as_view=True)

def with_rels(G,rels) :
  ''''view of G that follows only links in rels'''
  return nx.subgraph_view(G,
    filter_edge=lambda x,y:G[x][y]['rel'] in rels )

def without_rels(G,rels) :
  ''''view of G that follows only links NOT in rels'''
  return nx.subgraph_view(G,
    filter_edge=lambda x,y:G[x][y]['rel'] not in rels )

# unused
'''
  def walks(self, lemmas, g):
    lemmas = list(lemmas)
    paths = []
    l = len(lemmas)
    for i in range(l):
      for j in range(i):
        p = chain(g, lemmas[i], lemmas[j])
        if p: paths.extend(p)
    return paths
'''


def reason_with(fname,query=True) :
  '''
  Activates dialog about document in <fname>.txt with questions
  in <fname>_quests.txt
  Assumes stanford corenlp server listening on port 9000
  with annotators listed in params.py  available.
  '''
  t = Thinker(from_file=fname+'.txt')
  show =t.params.show_pics

  t.show_all()
  if query:
    t.query_with(fname+'_quest.txt')
    pshow(t,file_name=fname+"_quest.txt",
          cloud_size=t.params.cloud_size,
          show=t.params.show_pics)
