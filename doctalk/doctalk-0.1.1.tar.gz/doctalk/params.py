from inspect import getframeinfo, stack

annotators=['tokenize','ssplit','pos','lemma','depparse','ner']+\
           ['natlog','openie']
trace=0

class talk_params:
  def __init__(self):
    self.force = False

    self.sum_count = 9
    self.key_count = 10
    self.max_answers = 4
    self.cloud_size = 24
    self.subgraph_size = 38

    self.quiet = True
    self.answers_by_rank = True

    self.pers = True
    self.expand_query = 2
    self.guess_wh_word_NERs=0

    self.compounds = True
    self.svo_edges = True
    self.subject_centered = True
    self.all_to_sent=False
    self.use_to_def=True

    self.show_pics = 0  # 1 : just generate files, 2: interactive
    self.show_rels = 0
    self.to_prolog = 0
    
    self.think_depth=4

# decides between '_' and ' ' as separator
#def join(*xs) : return ' '.join(xs)
def join(*xs) : return xs

def ppp(*args) :
  if trace<1 : return
  caller = getframeinfo(stack()[1][0])

  print('DEBUG:',
        caller.filename.split('/')[-1],
        '->',caller.lineno,end=': ')
  print(*args)
