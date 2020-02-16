'''
Created on 2019年7月30日

@author: Administrator
'''
#基于TF-IDF来做抽取式摘要
import pickle
import re
import numpy as np
# from word_segment_viterbi import ViterbiSegment
import pkuseg
class ExtractiveSummary():
    
    def __init__(self, mode='work'):
        if mode=="train":
            self.IDF = None
        else:
            self.IDF = pickle.load(open("model/IDF_model.pkl", 'rb'))
    
    #加载人民日报语料https://pan.baidu.com/s/1gd6mslt,形成每个句子的词语列表，用于后面统计词语频数
    def load_corpus(self, file='train.txt', default_corpus_size = None):
        documents = []
        words_in_doc = []
        with open(file, 'r', encoding='utf8') as f:
            lines = f.readlines()
            if default_corpus_size!=None: lines = lines[:default_corpus_size]#测试阶段截取较小的语料
            print("文档总行数是", len(lines))
            for line in lines:
                
                line = line.replace('\n', '').split("  ")[1:]
                words = list(map(lambda x: x.split('/')[0], line))
                words = list(filter(lambda x: len(x)>0, words))
                words_in_doc += words
                if len(words)==0:#原始语料用空行来将文档分隔开
                    documents.append(words_in_doc)
                    words_in_doc = []
        return documents
    
    def train(self,file):
        self.IDF = {}
        document_freq = {}#词语的文档频率，即包含特定词语的文档个数
        documents = self.load_corpus(file=file,default_corpus_size=None)
        for doc in documents:
            for word in set(doc):
                document_freq[word] = document_freq.get(word, 0) + 1
        
        corpus_size = len(documents)
        for word in document_freq:
            self.IDF[word] = np.log(corpus_size/(document_freq[word] + 1))
        pickle.dump(self.IDF, open("model/IDF_model.pkl", 'wb'))

    def cut_sent(self,para):
        # para = re.sub('([，。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
        para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
        para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
        para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
        para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
        para = para.rstrip()  # 段尾如果有多余的\n就去掉它
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
        return para.split("\n")

    def summary(self, text):
        # sentences = text.split("，")#将文本切分为句子。
        sentences=self.cut_sent(text)
        new_sentences = []
        sentence_score = {}
        words_in_sentences = []
        # 训练语料与IDF的训练语料相同(分词粒度统一)。
        segmentor = pkuseg.pkuseg(user_dict = "dict.txt",postag=False)  # 
        word_weight = {}#存储本文档中各个词语的term freq
        print("计算次词语权重")
        for sentence in sentences:
            if len(sentence)>100 or len(sentence)<2: continue
            words = segmentor.cut(sentence)#对句子分词，得到词语list
            for word in words:
                word_weight[word] = word_weight.get(word, 0) + 1
            words_in_sentences.append(words)
            new_sentences.append(sentence)
        # print("计算句子权重", word_weight)
        for i in range(len(new_sentences)):
            sentence_score[new_sentences[i]] = np.sum([word_weight[word]*self.IDF.get(word, 0.01) for word in words_in_sentences[i]])
        print("对句子排序")
        sentence_sorted = sorted(sentence_score.items(), key=lambda x: x[1], reverse=True)[:5]
        # summary = "。".join(map(lambda x: x[0], sentence_sorted))
        summary=map(lambda x: x[0], sentence_sorted)
        return list(summary)

if __name__ == '__main__':
    work=input("work or train :")
    S = ExtractiveSummary(mode=work)
    if work=="work":

    #     S.train()
        text ="""
柯基犬简介
柯基犬简介

    柯基犬共分两种：卡迪根威尔士柯基犬和彭布罗克威尔士柯基犬。两者比较，彭布罗克柯基犬的体形较短，腿骨更直、更轻，而背毛的质地更好；但在性情上，彭布罗克柯基犬显得不安分，容易激动，没有卡迪根威尔士柯基犬那么驯服。从12世纪的理查一世到现在的女王伊丽莎白二世，柯基犬一直是英国王室的宠物。
 
    柯基犬虽然属于小型犬，但性格非常稳健，完全没有一般小型犬的神经质，是非常适合小孩的守护犬。它们的胆子很大，也相当机警，能高度警惕地守护家园，是最受欢迎小型护卫犬之一。对该犬，我们标准地描述是：外表英勇无畏惧，内心很温和，表现聪慧，凡事充满兴趣，从不羞怯或凶狠，有着小狗的外表，却拥有大狗的灵魂。
 
    步态自如流畅。前肢伸展自如，抬不太高，与后躯的驱动动作和谐一致。合适的肩部位置，加上合适的肘部动作使得犬能向前大步自如地行走。从前面观看，四肢行走时并不在一个平行的平面上，而是稍微内收，以弥补腿短与宽胸的缺陷。后肢伸展自如，并且与前肢位于一直线上，使得动作运行连续有力，跗关节既不内收也不外翻。爪子的运动与运动路线平行，不能左右摇摆、交叉、相互干扰。不连贯的短运动、身体摇摆或高抬腿行走，来回行走时步态太紧凑或太张开是都是不正确的步态。本牧羊犬的行动必须敏捷、自如，对工作有耐力。
阅读更多
2 柯基犬怎样训练
柯基犬怎样训练

    宠爱不是宠溺，你要实时的给他教训，让他知道什么是可以做的，什么是不可以的，狗狗是要管教的，该打还是要打的。教训是有目的的不是盲目的，每次针对这种行为的教训，反复个几次他就知道什么是不可以做的啦，这是一个很短的过程，交会了就好啦，你不要一时的不舍得就弄的以后有更大的麻烦。
 
    训练手段：包括诱导、强迫、禁止和奖励等。
 
    诱导，是指饲主使用犬喜爱的食品和物品诱使犬做出某种动作，或利用犬自发性动作，通过与口令、手势的结合使用，以使其建立条件反射或增强训练效果的一种手段
 
    在犬的训练中，必须遵循“循序渐进、由简入繁、因犬制宜、分别对待”的原则。
 
    训练犬做每一个完整的动作，不是一下就能完成的，必须循序渐进、由简入繁地进行训练，由各种单一条件反射组合成一个动力定型。如在“衔取”动作中，它包括了“左侧坐、去、衔、来”等一系列条件反射，形成一个固定的动力定型，以后只要犬听到“衔”的口令，就会完成这一系列动作。
 
    由于各种犬的神经类型、性格特点和训练目的不同，所以，在训练中，应因犬制宜，分别对待，否则，采取最好的训练方法也是无效的。例如：对食物反应较强的，可多用食物刺激；对凶猛好斗的犬，要严格要求，加强其服从性和依恋性的培养；对胆小的犬，要用温和的语调调教，轻巧的动作接近，并耐心诱导。总之，要针对犬的特点训练。
 
    禁止，是指饲主为了制止其不良行为而采用的一种手段。禁止，实质上是一种对犬的惩罚，只能用于犬发生不良行为时，而当犬延缓执行口令时，只能采取强迫手段，而不能用禁止方法。在使用禁止手段时，态度要严肃，语气要坚定，但不得体罚犬。制止要及时，只有在犬有犯禁的欲求行为时或犯禁初期，制止才有效。事后禁止，非但无用，反而会使犬神经发生混乱，不知所措。在犬停止犯禁后，应立即奖励，以缓和犬的紧张状态。
 
    奖励，是为了强化犬的正确动作，巩固已养成的行为，调整犬的神经状态而采取的一种手段。奖励的方法有喂食物、抚摸、放游和叫“好”的口头表扬等。奖励在犬的训练中极为重要，但要运用得法，否则，收不到良好的效果。
阅读更多
3 柯基犬如何喂养
柯基犬如何喂养

    柯基犬共威尔士柯基犬分两种：卡迪根威尔士柯基犬和彭布罗克威尔士柯基犬。两者比较，彭布罗克柯基犬的体形较短，腿骨更直、更轻，而威尔士柯基犬背毛的质地更好；但在性情上，彭布罗克柯基犬显得不安分，容易激动，没有卡迪根威尔士柯基犬那么驯服。从12世纪的理查一世到现在的女王伊丽莎白二世，柯基犬一直是英国王室的宠物。
 
    柯基身体矮小，力气较大，给人一种体格结实，充满活力、优质的骨骼及优秀的耐力的印象，是最受欢迎的小型看家犬之一，本性友好，勇敢大胆，既不胆怯也不凶残。性格温和，但不要强迫它接受不愿意接受的事物。
 
柯基犬的饲养要点
 
    每天喂饲食物的量要适度，过多过少都不利健康成长。每天的饲料中，应含肉类及等量的各种杂粮、蔬菜、胡萝卜等素食。要定期更换品种，以确保摄食的营养全面。
 
    柯基犬容易患眼疾，应每隔3～5天，用2%的硼酸水为它洗眼，以防止眼疾发生。还应定期为它洗澡、清除耳垢、牙垢，修剪爪子等。威尔士柯基犬属于短毛犬，但也应经常为它梳刷清理，以保持其清洁美观。柯基犬无体臭，一个月洗一次澡就可以了。犬舍要选择通风、干净和干燥的地方，并每隔半个月或一个月做一次消毒处理，以防滋生细菌。
 
    柯基犬与同类能很好地相处，但却不能与其他犬类保持融洽，所以必须从幼犬时期开始，对它进行训练和调教，使它改掉这种恶习。同时也要训练它不用牙和爪撕咬家中衣服、窗帘、沙发、床单、被子等物件，训练它爱清洁卫生，不在有污泥的地上乱躺，特别要让它在规定的地方大小便。柯基犬早期为畜牧犬，所以生性活泼好动，不能老关在室内，而应给予适当的时间让它在户外活动，以保持其健康活跃的特性。
 
    如果你想养柯基犬，那么你就要注意对幼犬的教养，如果柯基犬在年幼时，不加强对其正确的调驯，小狗长大后就较难管教。在小狗眼中，如果你不对其进行约束，它会反过来认为它是主人，漠视你对它的命令，行动随便，令你感到困扰和产生厌恶心理，甚至抛弃幼犬！所以，要从小注意对幼犬的教养，这样才能使主人与幼犬建立良好的关系，互相之间的沟通更顺畅，才会产生更亲昵的感情。幼犬的教养法则其实就是：“是”与“否”这两个字，对幼犬教养的关键就是让其掌握这两条命令。
 
    当小狗将做错事时，主人必须用简短、明确的禁止用语，如“否”！、“No”！等，用严厉的口气配合手势制止幼犬的行为。如果发出了“否”的命令后，幼犬停止了原本要做的动作，主人就应该立即对其赞扬，发出“好的”或“是”的温柔声音，给予幼犬鼓励。同时，可用手轻抚幼犬的头和背部，让幼犬感到舒适。幼犬只要掌握了这两条基本命令，主人就能明确地控制幼犬的行为，对幼犬其它方面的训练就容易和方便的多了！
阅读更多
4 柯基犬多少钱一只
柯基犬多少钱一只

    柯基犬多少钱一只？为了更好的了解柯基的市场价格，给大家在购买宠物狗的时候带来便利，我们市场调研组的工作人员在经过中国北京，上海，天津，江苏等众多地区的犬舍和私人家的宠物狗的出售价格，按照宠物狗所在的地区、毛量、颜色，骨量、血统等众多因素产生的不同价格，进行分析、统计、得出现在市场上各种宠物狗的销售价格，整理出狗狗的销售价格表。下面就来给大家总结一下：
 
柯基犬的价格：
 
一、成都柯基犬的价格
 
    迷你柯基：约2300左右
 
    纯种柯基：约3000左右
 
二、深圳柯基犬的价格
 
    迷你柯基：约1300至2000左右
 
    纯种柯基：约2500左右
 
三、沈阳柯基犬的价格
 
    迷你柯基：约1200至2000左右
 
    纯种柯基：约2500左右
 
    柯基是一个活泼的狗狗，因为狗狗很可爱，在调查中我们发现，柯基很受欢迎，因为市场交易量逐渐变大，狗狗的市场价格和质量都有差异。在血统上，如果柯基的父母是有赛级资格的，其幼犬价格会同比增高500元左右；性别也是导致狗狗价格差异的一个因素，比如，北京一只母的柯基比公的柯基犬的价格上会高出300元左右；狗狗的年龄也会影响狗狗的价格，幼犬在2-3个月的时候，其价格会比成犬便宜500元；毛量和骨量也是影响狗狗价格的因素，尤其是选择种狗时，其毛量和骨量是宠物狗质量上很重要的参考指标，往往毛量好、骨量大的狗狗会比毛量、骨量一般的狗狗贵500元左右。
        
        """
        print(S.summary(text))
    elif work=="train":
        text = input("txt文件路径 :")
        S.train(text)
