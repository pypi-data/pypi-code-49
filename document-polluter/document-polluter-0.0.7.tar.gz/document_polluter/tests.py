"""
Tests for Document Polluter
"""
import random
import unittest

from document_polluter import DocumentPolluterError, DocumentPolluter, genres, clusters, non_fungible_terms, fungibles

class TestFunctions(unittest.TestCase):
  def test_genres(self):
    actual = genres()
    expected = ['gender', 'us-race']
    self.assertTrue(actual == expected)

  def test_existing_cluster(self):
    actual = clusters('gender')
    expected = ['female', 'male']
    self.assertTrue(sorted(actual) == sorted(expected))

  def test_non_existant_cluster(self):
    with self.assertRaises(DocumentPolluterError) as cm:
      clusters('foo')
    self.assertTrue(str(cm.exception) == 'genre does not exist')

  def test_existing_non_fungible_terms(self):
    actual = non_fungible_terms('gender')
    expected = ['her', 'hers', 'him', 'his']
    self.assertTrue(sorted(actual) == sorted(expected))

  def test_non_existant_non_fungible_terms(self):
    with self.assertRaises(DocumentPolluterError) as cm:
      non_fungible_terms('foo')
    self.assertTrue(str(cm.exception) == 'genre does not exist')

  def test_existing_fungibles(self):
    actual = fungibles('gender')
    first = {'female': 'she', 'male': 'he'}
    last = {'female': 'grandmothers', 'male': 'grandfathers'}

    self.assertTrue(len(actual) == 22)
    self.assertTrue(actual[0] == first)
    self.assertTrue(actual[-1] == last)

  def test_non_existant_cluster(self):
    with self.assertRaises(DocumentPolluterError) as cm:
      fungibles('foo')
    self.assertTrue(str(cm.exception) == 'genre does not exist')

class TestDocumentPolluter(unittest.TestCase):
  def test_non_existant_genre(self):
    with self.assertRaises(DocumentPolluterError) as cm:
      DocumentPolluter(documents=['foo', 'bar'], genre='bar')
    self.assertTrue(str(cm.exception) == 'genre does not exist')

  def test_removes_documents_with_non_fungible_terms(self):
    documents = ['his face', 'he is']
    dp = DocumentPolluter(documents=documents, genre='gender')
    
    self.assertTrue(dp.ineligible_documents == ['his face'])
    self.assertTrue(dp.eligible_documents == ['he is'])

  def test_generates_polluted_documents(self):
    documents =              ['she shouted',  'my son']
    expected_female =        ['she shouted',  'my daughter']
    expected_male =          ['he shouted',   'my son']

    dp = DocumentPolluter(documents=documents, genre='gender')

    self.assertTrue(sorted(dp.polluted_documents['female']) == sorted(expected_female))
    self.assertTrue(sorted(dp.polluted_documents['male']) == sorted(expected_male))

  def test_multiple_word_documents_polluted(self):
    documents =       ['she was a mother to my sister']
    expected_female = ['she was a mother to my sister']
    expected_male =   ['he was a father to my brother']

    dp = DocumentPolluter(documents=documents, genre='gender')

    self.assertTrue(sorted(dp.polluted_documents['female']) == sorted(expected_female))
    self.assertTrue(sorted(dp.polluted_documents['male']) == sorted(expected_male))
 
  def test_punctuated_documents_polluted(self):
    documents =       ['she was a mother, to my sister.']
    expected_female = ['she was a mother, to my sister.']
    expected_male =   ['he was a father, to my brother.']

    dp = DocumentPolluter(documents=documents, genre='gender')

    self.assertTrue(sorted(dp.polluted_documents['female']) == sorted(expected_female))
    self.assertTrue(sorted(dp.polluted_documents['male']) == sorted(expected_male))
 
  def test_capitalized_documents_polluted(self):
    documents =       ['She was a Mother to my sister']
    expected_female = ['she was a mother to my sister']
    expected_male =   ['he was a father to my brother']

    dp = DocumentPolluter(documents=documents, genre='gender')

    self.assertTrue(sorted(dp.polluted_documents['female']) == sorted(expected_female))
    self.assertTrue(sorted(dp.polluted_documents['male']) == sorted(expected_male))

  def test_parts_of_words_not_polluted(self):
    documents =       ['she SHEd HEad']
    expected_female = ['she shed head']
    expected_male =   ['he shed head']

    dp = DocumentPolluter(documents=documents, genre='gender')

    self.assertTrue(sorted(dp.polluted_documents['female']) == sorted(expected_female))
    self.assertTrue(sorted(dp.polluted_documents['male']) == sorted(expected_male))

  def test_documents_with_no_polluting_terms_non_eligible(self):
    documents = ['no gendered words']
    dp = DocumentPolluter(documents=documents, genre='gender')
    self.assertTrue(dp.ineligible_documents == documents)

if __name__ == '__main__':
  unittest.main()