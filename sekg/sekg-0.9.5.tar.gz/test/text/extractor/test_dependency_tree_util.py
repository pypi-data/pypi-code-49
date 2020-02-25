from unittest import TestCase
from sekg.text.spacy_pipeline.pipeline import PipeLineFactory
from sekg.util.dependency_tree_util import DependencyTreeUtil


class TestEntityExtractor(TestCase):
    def print_nlp_analysis(self, sent_doc):
        np_chunk_detail = [chunk for chunk in sent_doc.noun_chunks]
        print("np_chunk_detail for sentence", np_chunk_detail)
        SEP = " - "
        for chunk in sent_doc.noun_chunks:
            print(chunk.text, SEP, chunk.root.text, SEP,
                  chunk.root.dep_, SEP,
                  chunk.root.head.text)
        print("----chunk detail")
        for chunk in sent_doc.noun_chunks:
            for token in chunk:
                print(token.text, SEP, token.pos_, SEP, token.tag_, SEP)
        print("-----------end chunk print----------")
        for token in sent_doc:
            print(token.text, SEP, token.pos_, SEP, token.tag_, SEP, token.dep_, SEP, token.head.text, SEP,
                  token.head.pos_, SEP,
                  [child for child in token.children],
                  SEP,
                  [child for child in token.lefts],
                  SEP,
                  [child for child in token.rights],
                  )
        print("-----------end tree print----------")
        print("-----------subtree----------")
        print("subject of is:", DependencyTreeUtil.get_subject(doc=sent_doc),
              DependencyTreeUtil.get_subject_text(sent_doc))
        print("predicate is:", DependencyTreeUtil.get_main_predicate(doc=sent_doc))
        print("-----------end subtree----------")

    def test_extract_condition(self):
        text = "File descriptor is modified by FileWriter when the thread starts."
        nlp = PipeLineFactory.full_pipeline()
        sent_doc = nlp(text)
        self.print_nlp_analysis(sent_doc)
        t = DependencyTreeUtil.get_main_predicate(doc=sent_doc)
        condition_text = DependencyTreeUtil.get_conditions_text_for_token(sent_doc, t)
        print(condition_text)

    def test_subject(self):
        text = "Object.finalize() is called by the garbage collector on an object when garbage collection determines."
        nlp = PipeLineFactory.full_pipeline()
        sent_doc = nlp(text)
        self.print_nlp_analysis(sent_doc)
        t = DependencyTreeUtil.get_subject(doc=sent_doc)
        print(t)
