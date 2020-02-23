import pyterrier as pt
import pandas as pd

pt.init(packages=["uk.ac.gla.dcs:ircourse:1.0-SNAPSHOT"])

path_dataset = "/home/alex/Documents/Еx/collections"
index_path = "/home/alex/Documents/gov_index"
trec_path = "/home/alex/Downloads/books/doc-text.trec"

index = pt.TRECIndex(index_path)
# index_properties = {"indexer.meta.reverse.keys":"docno", "invertedfile.lexiconscanner":"pointers"}
# files_path = pt.Utils.get_files_in_dir(path_dataset)
# index.setProperties(**index_properties)
# index.index(files_path)

hp04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/HP04/topics")
np04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/NP04/topics")
td04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/TD04/topics")

hp04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/HP04/qrels")
np04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/NP04/qrels")
td04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/TD04/qrels")

MyIDF = pt.BatchRetrieve(index.path, controls ={"wmodel":"uk.ac.gla.dcs.models.MyTFIDF"})
TFIDF = pt.BatchRetrieve(index.path, controls = {"wmodel": "TF_IDF"})
PL2 = pt.BatchRetrieve(index.path, controls={"wmodel":"PL2",})
BM25 = pt.BatchRetrieve(index.path, controls={"wmodel":"BM25"})

out = pt.Experiment(hp04_topics,[MyIDF, TFIDF, PL2, BM25],['map', 'iprec_at_recall'],hp04_qrels, perquery=True, dataframe=False)
print(out)
