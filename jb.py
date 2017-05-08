__author__ = 'owen'


import jieba , jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

path = r'/Users/owen/Desktop/result.txt'

jb = open(path,'w+')
jieba.analyse.set_stop_words('/Users/owen/Desktop/stopwords.txt')
for line in open('/Users/owen/Desktop/query_result.csv'):

    # item = line.strip('\n\r').split('\t')
    item = line.split(",")
    stra = ''.join(item)
    tags = jieba.analyse.extract_tags(stra)
    tagsw = ",".join(tags)
    # tags = jieba.analyse.extract_tags(item[1])
    # tagsw = ",".join(tags)
    print tagsw
    jb.write(tagsw)
jb.close()


word_lst = []
word_dict= {}
with open('/Users/owen/Desktop/result.txt') as wf ,open("/Users/owen/Desktop/word.txt",'w') as wf2:
    for word in wf:
        print word
        word_lst.append(word.split(','))
        for item in word_lst:
             for item2 in item:

                if item2 not in word_dict:
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1
                #print item2
    for key in word_dict:
        #print key,word_dict[key]
        wf2.write(key+' ,'+str(word_dict[key])+'\n')



