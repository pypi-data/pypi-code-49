import pyterrier as pt

pt.init(packages=["uk.ac.gla.dcs:ircourse:1.0-SNAPSHOT"])

path_dataset = "/home/alex/Documents/Еx/collections"
index_path = "/home/alex/Documents/gov_index"
trec_path = "/home/alex/Downloads/books/doc-text.trec"


index = pt.TRECIndex(index_path)
index_properties = {"indexer.meta.reverse.keys":"docno", "invertedfile.lexiconscanner":"pointers"}
files_path = pt.Utils.get_files_in_dir(path_dataset)
index.setProperties(**index_properties)
# index.index(files_path)

hp04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/HP04/topics")
np04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/NP04/topics")
td04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/TD04/topics")

hp04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/HP04/qrels")
np04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/NP04/qrels")
td04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/TD04/qrels")

retr = pt.BatchRetrieve(index.path)

retr.setControl("wmodel", "uk.ac.gla.dcs.models.MyTFIDF")
hp_04_MyTFIDF=retr.transform(hp04_topics)
np_04_MyTFIDF=retr.transform(np04_topics)
td_04_MyTFIDF=retr.transform(td04_topics)
hp_04_MyTFIDF_eval=pt.Utils.evaluate(hp_04_MyTFIDF,hp04_qrels)
np_04_MyTFIDF_eval=pt.Utils.evaluate(np_04_MyTFIDF,np04_qrels)
td_04_MyTFIDF_eval=pt.Utils.evaluate(td_04_MyTFIDF,td04_qrels)

retr.setControl("wmodel", "TF_IDF")
hp_04_TFIDF=retr.transform(hp04_topics)
np_04_TFIDF=retr.transform(np04_topics)
td_04_TFIDF=retr.transform(td04_topics)
hp_04_TFIDF_eval=pt.Utils.evaluate(hp_04_TFIDF,hp04_qrels)
np_04_TFIDF_eval=pt.Utils.evaluate(np_04_TFIDF,np04_qrels)
td_04_TFIDF_eval=pt.Utils.evaluate(td_04_TFIDF,td04_qrels)

retr.setControl("wmodel", "BM25")
hp_04_BM25=retr.transform(hp04_topics)
np_04_BM25=retr.transform(np04_topics)
td_04_BM25=retr.transform(td04_topics)
hp_04_BM25_eval=pt.Utils.evaluate(hp_04_BM25,hp04_qrels)
np_04_BM25_eval=pt.Utils.evaluate(np_04_BM25,np04_qrels)
td_04_BM25_eval=pt.Utils.evaluate(td_04_BM25,td04_qrels)

retr.setControl("wmodel", "PL2")
hp_04_PL2=retr.transform(hp04_topics)
np_04_PL2=retr.transform(np04_topics)
td_04_PL2=retr.transform(td04_topics)
hp_04_PL2_eval=pt.Utils.evaluate(hp_04_PL2,hp04_qrels)
np_04_PL2_eval=pt.Utils.evaluate(np_04_PL2,np04_qrels)
td_04_PL2_eval=pt.Utils.evaluate(td_04_PL2,td04_qrels)

print("MyTFIDF: HP, NP, TD")
print(hp_04_MyTFIDF_eval)
print(np_04_MyTFIDF_eval)
print(td_04_MyTFIDF_eval)
print("TF_IDF: HP, NP, TD")
print(hp_04_TFIDF_eval)
print(np_04_TFIDF_eval)
print(td_04_TFIDF_eval)
print("BM25: HP, NP, TD")
print(hp_04_BM25_eval)
print(np_04_BM25_eval)
print(td_04_BM25_eval)
print("PL2: HP, NP, TD")
print(hp_04_PL2_eval)
print(np_04_PL2_eval)
print(td_04_PL2_eval)
