import pyterrier as pt

pt.init()
index_path = "/home/alex/Documents/gov_index"
index = pt.TRECIndex(index_path)

hp04_topics = pt.Utils.parse_trec_topics_file("/home/alex/Documents/Еx/TopicsQrels/HP04/topics")

feat_retrieve = pt.FeaturesBatchRetrieve(index.path, ["WMODEL:BM25","WMODEL:PL2"])
feat_res = feat_retrieve.transform(hp04_topics)
print(feat_res)
