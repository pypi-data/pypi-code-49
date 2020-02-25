import pyterrier as pt
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-whitegrid")

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
# MyIDF = pt.BatchRetrieve(index.path, controls ={"wmodel":"uk.ac.gla.dcs.models.MyTFIDF", "qe":"on"}) to enable query expansion
# Alternative way  of selecting controls
# MyIDF.setControl("wmodel", "uk.ac.gla.dcs.models.MyTFIDF")
TFIDF = pt.BatchRetrieve(index.path, controls = {"wmodel": "TF_IDF"})
BM25 = pt.BatchRetrieve(index.path, controls={"wmodel":"BM25"})
PL2 = pt.BatchRetrieve(index.path, controls={"wmodel":"PL2"})
PL2_qe = pt.BatchRetrieve(index.path, controls={"wmodel":"PL2", "qe":"on"})

retr_systems = [MyIDF,TFIDF,BM25,PL2]
hp = pt.Experiment(td04_topics,[PL2],['map'],td04_qrels, perquery=True)
# hp_qe = pt.Experiment(td04_topics,[PL2_qe],['map'],td04_qrels, perquery=True)

PL2_items = hp["PL2"]
PL2_items_qe = hp_qe["PL2"]

# count=0
# for no_qe, qe in zip(PL2_items.values(),PL2_items_qe.values()):
#     # print(no_qe)
#     if no_qe["map"]<qe["map"]:
#         count+=1
    # print(no_qe, qe)
    # print()

# print(count)

# width = 0.5
#
# PL2_vals = []
# PL2_qe_vals = []
# PL2_keys = PL2_items.keys()
#
# print(PL2_items)
# print(PL2_items_qe)
#
# for val in PL2_items.values():
#     PL2_vals.append(val["map"])
#
# for val in PL2_items_qe.values():
#     PL2_qe_vals.append(val["map"])
#
# print(len(PL2_vals))
# print(PL2_vals)
# print(len(PL2_qe_vals))
# print(PL2_qe_vals)
#
# x_range = np.arange(len(PL2_keys))
#
# fig, ax = plt.subplots()
# rects = ax.bar(x_range - width/2, PL2_vals, width, label="No QE")
# rects_qe = ax.bar(x_range + width/2, PL2_qe_vals, width, label="QE")
#
# print(PL2_keys)
# ax.set_xticks(x_range)
# ax.set_xticklabels(PL2_keys)
# ax.legend()
# # fig.tight_layout()
# plt.show()


# print(hp)
# MyTFIDF_items = hp["uk.ac.gla.dcs.models.MyTFIDF"]
# TFIDF_items = hp["TF_IDF"]
# BM25_items = hp["BM25"]
# PL2_items = hp["PL2"]

# fig = plt.figure()
# ax = plt.axes()

# keys = ["0.0","0.1","0.2","0,3","0,4","0,5","0.6","0.7","0.8","0.9","1.0"]
# plt.plot(keys,MyTFIDF_items.values(), label="MyTFIDF")
# ax.plot(keys,TFIDF_items.values(), label="TF_IDF")
# ax.plot(keys,BM25_items.values(), label="BM25")
# ax.plot(keys,PL2_items.values(), label="PL2")
#
# plt.legend()
# plt.show()

# np = pt.Experiment(np04_topics,[MyIDF],['map'],np04_qrels)
# td = pt.Experiment(td04_topics,[MyIDF],['map'],td04_qrels)
# hp = pt.Experiment(hp04_topics,[MyIDF],['map'],hp04_qrels)

# print(hp)
# print(np)
# print(td)

# print(pt.Experiment(np04_topics,retr_systems,["map"],np04_qrels))
# print(pt.Experiment(td04_qrels,retr_systems,["map"],td04_qrels))
