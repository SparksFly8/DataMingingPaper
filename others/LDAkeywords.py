# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/5/13 23:41'

from gensim.models.ldamodel import LdaModel
from gensim.models.ldaseqmodel import LdaSeqModel
from gensim import corpora
import xlrd
import nltk
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import time

def getList(openFile, sheetNumList, colx=1, start_rowx=1):
    '''
        获取excel指定sheet指定列指定范围行的数据
        :param openFile: excel路径
        :param sheetNumList: sheet序号列表
        :param colx: 获取指定列数
        :param start_rowx: 起始行数
        :return doc_list: 一个包含所有abstract的列表
        '''
    # 打开工作簿
    data = xlrd.open_workbook(openFile)
    doc_list = []
    for sheetNum in sheetNumList:
        # 选定sheet
        table = data.sheets()[sheetNum]
        # 获取excel表的指定列,start_rowx=1表示从第2行开始(从0计数)
        abstracts = table.col_values(colx=colx, start_rowx=start_rowx)
        doc_list.append("".join(abstracts))
    return  doc_list

def clean(doc):
    stopword = set(stopwords.words('english'))  # 设置停用词
    stopword.add('using')
    stopword.add('user')
    stopword.add('paper')
    stopword.add('problem')
    stopword.add('much')
    stopword.add('0')
    stopword.add('NaN')

    exclude = set(string.punctuation)       # 去除标点符号
    lemma = WordNetLemmatizer()             # 词性还原

    stop_free = " ".join([i for i in doc.lower().split() if i not in stopword])     # 小写化+去除用词
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)            # 去除标点符号
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())  # 词性还原
    return normalized

if __name__ == '__main__':
    openFile = r'/root/shiliang/2014-2018keywords.xlsx'
    doc_list = getList(openFile, [0,1,2,3,4])
    a = time.time()
    doc_clean = [clean(doc).split() for doc in doc_list]
    print('清洗数据耗时：%.5f秒' % float(time.time() - a))
    # 创建语料的词语词典，每个单独的词语都会被赋予一个索引
    b = time.time()
    dictionary = corpora.Dictionary(doc_clean)
    print('创建语料词典耗时：%.5f秒' % float(time.time() - b))
    # 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
    c = time.time()
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    print('转换DT矩阵耗时：%.5f秒' % float(time.time() - c))
    # 使用 gensim 来创建 LDA 模型对象,在 DT 矩阵上运行和训练 LDA 模型
    # ldamodel = LdaModel(corpus=doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)
    start = time.time()
    ldaseq = LdaSeqModel(corpus=doc_term_matrix, num_topics=6, chain_variance=10, id2word=dictionary, passes=50, time_slice=[1, 1, 1, 1, 1])
    end = time.time()
    # 输出结果
    print('2014年主题结果：')
    list1 = ldaseq.print_topics(time=4, top_terms=15)
    for index, topics in enumerate(list1):
        print('2014年第'+str(index+1)+'个topic的关键词如下：')
        tmp = 0
        for keywords in topics:
            tmp += keywords[1]
            print(keywords)
        print('2014年第'+str(index+1)+'个topic的关键词频率之和：'+str(tmp))

    print('2015年主题结果：')
    list2 = ldaseq.print_topics(time=3, top_terms=15)
    for index, topics in enumerate(list2):
        print('2015年第'+str(index+1)+'个topic的关键词如下：')
        tmp = 0
        for keywords in topics:
            tmp += keywords[1]
            print(keywords)
        print('2015年第' + str(index + 1) + '个topic的关键词频率之和：' + str(tmp))

    print('2016年主题结果：')
    list3 = ldaseq.print_topics(time=2, top_terms=15)
    for index, topics in enumerate(list3):
        print('2016年第' + str(index + 1) + '个topic的关键词如下：')
        tmp = 0
        for keywords in topics:
            tmp += keywords[1]
            print(keywords)
        print('2016年第' + str(index + 1) + '个topic的关键词频率之和：' + str(tmp))

    print('2017年主题结果：')
    list4 = ldaseq.print_topics(time=1, top_terms=15)
    for index, topics in enumerate(list4):
        print('2017年第' + str(index + 1) + '个topic的关键词如下：')
        tmp = 0
        for keywords in topics:
            tmp += keywords[1]
            print(keywords)
        print('2017年第' + str(index + 1) + '个topic的关键词频率之和：' + str(tmp))

    print('2018年主题结果：')
    list5 = ldaseq.print_topics(time=0, top_terms=15)
    for index, topics in enumerate(list5):
        print('2018年第' + str(index + 1) + '个topic的关键词如下：')
        tmp = 0
        for keywords in topics:
            tmp += keywords[1]
            print(keywords)
        print('2018年第' + str(index + 1) + '个topic的关键词频率之和：' + str(tmp))

    print('训练耗时：%.5f秒' % float(end - start))
