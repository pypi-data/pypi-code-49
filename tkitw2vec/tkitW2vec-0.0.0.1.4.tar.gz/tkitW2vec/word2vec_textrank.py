import os
import re
import math
import jieba
import numpy as np
import networkx as nx
from gensim.models import Word2Vec
from itertools import product,count

def cut_sents(content):
    sentences = re.split(r"([。!！?？；;\s+])", content)[:-1]
#     sentences = re.split(r"")
    sentences.append("")
    sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
    return sentences

def cut_word_test(context):
    parent = os.path.dirname(os.path.realpath(__file__))
    stopkey=[line.strip() for line in open(parent+'/resources/stopwords.txt',encoding='utf-8').readlines()] 
    total_cutword = []
    total_content = []
    for i in context:
        words=jieba.cut(i)
        words_filter=[word for word in words if word not in stopkey]
        if len(words_filter) !=0:
            total_cutword.append(words_filter)
            total_content.append(i)
    return total_cutword,total_content

def filter_model(sents,model):
    '''
    过滤词汇表中没有的单词
    '''
    total = []
    for sentence_i in sents:
        sentence_list = []
        for word_j in sentence_i:
            if word_j in model:
                sentence_list.append(word_j)
        total.append(sentence_list)
    return total


def two_sentences_similarity(sents_1,sents_2):
    '''
    计算两个句子的相似性
    '''
    counter = 0
    for sent in sents_1:
        if sent in sents_2:
            counter +=1
    return counter / (math.log(len(sents_1) + len(sents_2)))

def cosine_similarity(vec1,vec2):
    '''
    计算两个向量之间的余弦相似度
    '''
    tx =np.array(vec1)
    ty = np.array(vec2)
    cos1 = np.sum(tx * ty)
    cos21 = np.sqrt(sum(tx ** 2))
    cos22 = np.sqrt(sum(ty ** 2))
    cosine_value = cos1/float(cos21 * cos22)
    return cosine_value

def computer_similarity_by_avg(sents_1,sents_2,model):
    '''
    对两个句子求平均词向量
    '''
    if len(sents_1) ==0 or len(sents_2) == 0:
        return 0.0
    vec1_avg = sum(model[word] for word in sents_1) / len(sents_1)
    vec2_avg = sum(model[word] for word in sents_2) / len(sents_2)
        
    similarity = cosine_similarity(vec1_avg , vec2_avg)
    return similarity

def create_graph(word_sent,model):
    '''
    传入句子链表，返回句子之间相似度的图
    '''
    num = len(word_sent)
    board = np.zeros((num,num))
    
    for i,j in product(range(num), repeat=2):
        if i != j:
            board[i][j] = computer_similarity_by_avg(word_sent[i], word_sent[j],model)
    return board

def sorted_sentence(graph,sentences,topK):
    '''
    调用pagerank算法进行计算，并排序
    '''
    key_index = []
    key_sentences = []
    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank_numpy(nx_graph)
#     sorted_scores = scores.items()
    sorted_scores = sorted(scores.items(), key = lambda item:item[1],reverse=True)
    for index,_ in sorted_scores[:topK]:
        key_index.append(index)
    new_index = sorted(key_index)
    for i in new_index:
        key_sentences.append(sentences[i])
    return key_sentences


def do(text,model,topK):
    list_sents = cut_sents(text)
    data,sentences = cut_word_test(list_sents) 
    # 训练模型
    # model = Word2Vec(data, size=256, window=5,iter=10, min_count=1, workers=4)
    # outp1="model/word2vec_demo.model"
    # model = Word2Vec.load(model_file)
    sents2 = filter_model(data,model)
    graph = create_graph(sents2,model)
    result_sentence = sorted_sentence(graph,sentences,topK)
    return "".join(result_sentence)
if __name__ == '__main__':
    text ="""
    柯基犬可爱、勇敢的狗狗，是现在最流行的犬种，也是英女皇身边的爱宠，很多都喜欢柯基犬，那么怎么看柯基犬纯不纯，看这5点就够了。


    一、身材匀称

    柯基身材比较矮小，但也是匀称的，胸深而阔，胸骨突出，体长而壮，肋部稍曲，背部较平直，腹部不宜上收，不太较平稳，活泼轻快自如，显出悠然自得的样子。

    都知道柯基是小短腿，所以日常饲养的话，要知道不能让柯基爬楼梯，或者做些过于激烈的运动，这样很容易伤害到柯基的脊椎，老年时可能会影响走路。


    二、耳朵接近等边三角形

    柯基的耳朵较为坚硬，而且比较大又是直立的那种，从鼻尖穿过眼睛到耳尖交叉划直线，所形成的三角形接近等边三角形。

    所以购买的时候，可以注意观察一下柯基的耳朵，日常的话，也要注意清理狗狗的耳朵，虽然柯基耳朵是直立的，但如果没有经常清理的话，耳朵也会藏满污垢，会导致耳朵发炎。


    三、头部合理

    柯基头部形状和外貌很像狐狸，头盖大而平坦，额头、鼻架适中，脸部略浑圆，前脸面轮廓鲜明，牙齿剪式或钳式咬合。

    柯基颈部短而较粗，略成拱形，与肩部融合得很好。眼睛明亮有神，看起来非常的漂亮跟迷人。也要注意眼睛下方是否有泪痕，如果有不建议选择，狗狗有眼睛疾病。


    四、尾巴短而自然

    柯基一般都是断尾的，有些可能天生也是断尾的，尾巴短，很自然。未断尾与背线在同一直线，自然下垂，不弯曲到背。

    这个自己观察一下就能分辨出来，同时也要看看狗狗的肛门周边的毛发是否干净，如果沾有不干净的东西就是便便的话，证明这只狗狗肠道不好，不建议选择。


    五、毛发有质感

    柯基毛发一般都很光滑，有质感，金黄色或者乳黄色的毛皮呈平直或者波浪状，毛量越多越好，可以用手抓一把，感觉很舒适，松手后，毛发会恢复原状，说明柯基的毛质很好。

    想要保持柯基这样光滑有质感的毛发，除了每天梳毛之外，建议选择带有深海鱼油，低盐营养的天然粮喂食，有助美毛润发，健康皮肤。


    饲养柯基禁忌：

    1、刚到家的幼犬，最好是喂食狗粮为主，2个月前的幼犬可以将狗粮泡软再喂食，有利于消化，或者喂食羊奶粉，羊奶粉接近母乳，营养丰富，有助发育，增强骨骼，提高免疫力。不要给幼犬喂食人食或者是纯牛奶，不仅没营养，还容易导致幼犬拉稀哦。


    2、幼犬抱回家后先不要马上训练，不然小狗会容易生病。正确的是先把幼犬安置在合适的地方，让它安静的休息，让幼犬对新家产生信任感。这一段时期约维持一个星期，就可以开始让幼犬幼犬熟悉四周的环境及建立日常生活习惯。


    3、幼犬4~6个月是换牙期，宠主要事先准备好磨牙零食（鸡肉干，羊奶酪），或者是大块的骨头，小骨头不行哦，因为小骨头狗狗就会不啃直接吞咽，这样就会很容易导致卡喉咙，没有及时取出狗狗还可能会有生命危险，所以要注意。


    结语：你家可以纯吗？其实只要自己喜欢，狗狗纯不纯又有什么关系呢？
    """

    result_data = do(text,3)
    print(result_data)
