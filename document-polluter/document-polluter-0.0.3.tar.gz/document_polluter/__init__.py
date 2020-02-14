import yaml
import os
import re

current_directory = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_directory, 'pollution.yaml')) as file:
  POLLUTION = yaml.load(file, Loader=yaml.FullLoader)

def genres():
  return list(POLLUTION.keys())

def clusters(genre):
  try:
    return list(POLLUTION[genre]['fungibles'][0].keys())
  except KeyError as exc:
    raise DocumentPolluterError('genre does not exist') from exc

def non_fungible_terms(genre):
  try:
    return POLLUTION[genre]['non-fungible-terms']
  except KeyError as exc:
    raise DocumentPolluterError('genre does not exist') from exc

def fungibles(genre):
  try:
    return POLLUTION[genre]['fungibles']
  except KeyError as exc:
    raise DocumentPolluterError('genre does not exist') from exc

class DocumentPolluterError(Exception):
    pass

class DocumentPolluter(object):
  def __init__(self, documents, genre):
    if genre not in genres():
      raise DocumentPolluterError('genre does not exist')
    self.genre = genre
    self.fungibles = POLLUTION[genre]['fungibles']
    self.all_polluting_terms = sum([list(f.values()) for f in self.fungibles], [])
    self.clusters = clusters(genre)

    self.documents = documents

    self.eligible_documents = []
    self.ineligible_documents = []

    self.__set_document_eligibility()

    self.polluted_documents = {}
    self.replacement_words = {}
    for cluster in self.clusters:
      self.polluted_documents[cluster] = []
      self.replacement_words[cluster] = {}

    for cluster in self.clusters:
      for fungible in self.fungibles:
        words = list(fungible.values())
        replacement_word = fungible[cluster]
        replacable_words = list(filter(lambda w: w != replacement_word, words))

        for replacable_word in replacable_words:
          self.replacement_words[cluster][replacable_word] = replacement_word

    self.__pollute_documents()

  def __set_document_eligibility(self):
    for document in self.documents:
      if self.__document_contains_non_fungible_terms(document.lower()) or not self.__document_contains_polluting_terms(document.lower()):
        self.ineligible_documents.append(document.lower())
      else:
        self.eligible_documents.append(document.lower())

  def __document_contains_non_fungible_terms(self, document):
    for non_fungible_term in POLLUTION[self.genre]['non-fungible-terms']:
      if bool(re.search(r'\b' + non_fungible_term + r'\b', document)):
        return True
    return False

  def __document_contains_polluting_terms(self, document):
    for term in self.all_polluting_terms:
      if bool(re.search(r'\b' + term + r'\b', document)):
        return True
    return False

  def __replace_words(self, document, dic):
    for replacable_word, replacement_word in dic.items():
      document = re.sub(rf"\b{replacable_word}\b", replacement_word, document)
    return document

  def __pollute_documents(self):
    for document in self.eligible_documents:
      for cluster in self.clusters:
        self.polluted_documents[cluster].append(self.__replace_words(document, self.replacement_words[cluster]))
