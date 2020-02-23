if __name__ == "__main__":
    # global properties
    # init(packages=["com.harium.database:sqlite:1.0.5"])
    # init()

    # JIR = autoclass('org.terrier.querying.IndexRef')
    # indexref = JIR.of("../index/data.properties")
    # index_path = "../index/data.properties"
    #
    # topics = Utils.parse_trec_topics_file("../vaswani_npl/query-text.trec")
    # topics_light = Utils.parse_trec_topics_file("../vaswani_npl/query_light.trec")

    # feat_retrieve = FeaturesBatchRetrieve(index_path, ["WMODEL:BM25","WMODEL:PL2"])
    # feat_res = feat_retrieve.transform(topics_light)
    # print(feat_res)

    # retr = BatchRetrieve(index_path)
    # batch_retrieve_results=retr.transform(topics)
    # print(batch_retrieve_results)

    # retr.saveLastResult("dph.res")
    # retr.saveResult(batch_retrieve_results,"/home/alex/Documents/Pyterrier/result.res")

    # qrels = Utils.parse_qrels("../vaswani_npl/qrels")
    # eval = Utils.evaluate(batch_retrieve_results,qrels)
    # print(eval)
    # lst = ["Doc1", "Doc2", "Doc3"]

    # dct = {"text": [
    # "He ran out of money, so he had to stop playing poker.",
    # "The waves were crashing on the shore; it was a lovely sight.",
    # "The body may perhaps compensates for the loss of a true metaphysics."],
    # "docno": ["1","2","3"],
    # "url": ["url1", "url2", "url3"]}
    # df = pd.DataFrame(dct)
    #
    # index_path2 = "/home/alex/Documents/index"
    #
    # path = "/home/alex/Documents/pyterrier/vaswani_npl/corpus/"
    # path2 = "/home/alex/Downloads/books"
    # path3 = "/home/alex/Downloads/books/doc-text.trec"
    #
    # path_dataset = "/home/alex/Documents/Еx/collections"
    #
    # path_trec_0 = "/home/alex/Documents/ex_test/00"
    # path_trec_1 = "/home/alex/Documents/ex_test/01"
    # path_trec_2 = "/home/alex/Documents/ex_test/02"
    # trec_list = [path_trec_0, path_trec_1, path_trec_2]

# TREC INDEX
    # all_files = Utils.get_files_in_dir(path_dataset)
    # print(all_files)
    # index = TRECIndex(index_path2, blocks=False)
    # # index.setProperties(**index_props)
    # index.index(all_files)
    # retr = BatchRetrieve(index.path)
    # batch_retrieve_results=retr.transform("file")
    # print(batch_retrieve_results)

#  DATAFRAME INDEX
    # meta_fields={"docno":["1","2","3"],"url":["url1", "url2", "url3"]}
    # index = DFIndex(index_path2)
    # index.index(df["text"],df["docno"])
    # # index.index(df["text"])
    # # index.index(df["text"], df["docno"])
    # # index.index(df["text"], df["docno"], df["url"])
    # # index.index(df["text"], df)
    # # index.index(df["text"], docno=["1","2","3"])
    # # index.index(df["text"], **meta_fields)
    # retr = BatchRetrieve(index.path)
    # batch_retrieve_results=retr.transform("sight")
    # print(batch_retrieve_results)

# TXT INDEX
    # index = FilesIndex(index_path2, blocks=False)
    # index_props={"blocks.size":2,"blocks.max":200000}
    # # index.setProperties(**index_props)
    # index.index(path2)
    # retr = BatchRetrieve(index.path)
    # batch_retrieve_results=retr.transform("file")
    # print(batch_retrieve_results)
