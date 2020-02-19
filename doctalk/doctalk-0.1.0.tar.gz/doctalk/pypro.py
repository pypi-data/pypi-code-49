from natlog.natlog import natlog,Int
from natlog.db import db

from .params import *
from .talk import *


class NatTalker(Talker) :
  def __init__(self,natscript=None,**kwargs):
    super().__init__(**kwargs)
    self.engine=natlog(text=natscript)
    self.engine.db=self.to_nat_db()

  def to_nat_db(self):
    nd=db()
    for svo, occs in self.svos.items():
      s, v, o = svo
      for id in sorted(occs) :
        c=(s,v,o,id) # should be Int
        nd.add_db_clause(c)
    return nd

  def query_with_goal(self,natgoal):
      for answer in distinct(self.engine.solve(natgoal)):
        yield answer

  def ask(self,q):
    answers,answerer=self.answer_quest(q)

    ids=dict()
    shareds=set()
    for answer in answers:
       id, sent,rank,shared=answer
       ids[id]=rank
       shareds.update(shared)

    inferred=set()
    targets=set()
    for shared in shareds :
       for res in self.query_with_goal("tc_search "+shared+" Rel What Where?") :
         _,_shared,rel,what,where=res
         id=where.val
         if id in ids:
            targets.add(what)
            inferred.add(id)
    for id in inferred :
       ids[id]=ids[id]*2

    yield rank_sort(ids),list(take(10,inferred)), shareds,targets

  def natrun(self, q):
     print('QUESTION:',q)
     for x in self.ask(q):
        ids,inferred,shareds,targets=x
        print('')
        print('SHARED:',shareds)
        print('')
        print('MINED: ',targets)
        print('')
     print('ANSWERS:')
     for i, r in take(5, ids):
       print(i, r, end=': ')
       self.say(nice(self.get_sentence(i)))
     print('-----------------------\n')


def nrun() :
  natscript = '''
  
  rel 'is_like'.
  rel 'as_in'.
  rel 'kind_of'.
  
  tc_search A Rel B Res : rel Rel, tc A Rel B (s (s 0)) _ Res.
  
  tc A Rel C (s N1) N1 Res : ~ A Rel B Id, tc1 B Rel C N1 N2 Id Res.

  tc1 B _Rel B N N Id Id.
  tc1 B Rel C N1 N2 _Id Res : tc B Rel C N1 N2 Res.

  similar A B Id:
    ~ A R B Id,
    ~ T R A Id1,
    ~ T R B Id1.
  '''

  N=NatTalker(from_file='examples/geo.txt',
              natscript=natscript)
  with open('examples/geo_quest.txt','r') as f:
    for q in f.readlines():
      N.natrun(q)
  #N.natrun("What deposits can be found in the Permian basin?")

  '''
  goals=[
    #'similar deposit B Id?',
    'tc_search permian Rel B Where ?'
  ]
  
  for goal in goals:
    print('GOAL:',goal)
    print('')
    ids=set()
    for answer in N.natrun(goal):
      print('ANSWER', answer)
      continue
      _,s,v,o,I=answer
      ids.add(I.val)
    return
    for id in ids :
      print(id,nice(N.get_sentence(id)))
    print('')
   '''

