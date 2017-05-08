__author__ = 'owen'


import jieba , jieba.analyse
from os import path
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



path1 = r'/Users/owen/Documents/tensor/static/result1.txt'

jb = open(path1,'w+')
jieba.analyse.set_stop_words('/Users/owen/Desktop/stopwords.txt')
for line in open('/Users/owen/Desktop/query_result.csv'):

    # item = line.strip('\n\r').split('\t')
    item = line.split(",")
    item2 = []
    # for i in item :
    #     print i
    #     if u'\u4e00' <= i <= u'\u9fff':
    #         item2.append(i)

    # if item.encode('UTF-8').isalpha():
    #     continue
    # else:
    #     stra = ''.join(item)
    stra = ''.join(item)

    tags = jieba.analyse.extract_tags(stra)
    tags2 = []

    for tag in tags:
        if u'\u4e00' <= tag <= u'\u9fff':
            tags2.append(tag)
            print tag.encode('UTF-8')
    tagsw = ','.join(tags2)
    # tags = jieba.analyse.extract_tags(item[1])
    # tagsw = ",".join(tags)
    jb.write(tagsw)
jb.close()

d = path.dirname('.')
back_coloring = imread(path.join(d, "./image/alice_mask.png"))
with open('/Users/owen/Documents/tensor/static/result1.txt') as f:

    text = f.readlines()
    text = r''.join(text)
    seg_list = jieba.cut(text)
    seg_list = r' '.join(seg_list)
    print seg_list
    wc = WordCloud(font_path='/Users/owen/Documents/tensor/static/simhei.ttf',mask=back_coloring, background_color="black", margin=5, width=1800, height=800)

    wc.generate(seg_list)

    wc.to_file(path.join(d, "alice.png"))

    # show
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

