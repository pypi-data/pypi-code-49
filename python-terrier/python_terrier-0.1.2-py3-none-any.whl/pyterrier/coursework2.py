import pyterrier as pt

pt.init(packages=["uk.ac.gla.dcs:ircourse:1.0-SNAPSHOT"])

path_dataset = "/home/alex/Documents/Еx/collections"
index_path = "/home/alex/Documents/gov_index"
trec_path = "/home/alex/Downloads/books/doc-text.trec"

index = pt.TRECIndex(index_path)
hp04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/HP04/topics")
hp04_qrels = pt.Utils.parse_qrels("/home/alex/Documents/Еx/TopicsQrels/HP04/qrels")
retr = pt.BatchRetrieve(index.path)
retr.setControl("wmodel", "uk.ac.gla.dcs.models.MyTFIDF")

hp_04=retr.transform(hp04_topics)
print(pt.Utils.evaluate(hp_04,hp04_qrels, metrics=["iprec_at_recall","map"], perquery=False))
