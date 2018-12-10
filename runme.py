
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:27:25 2018
generating a word cloud
@author: zengzhang
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
import jieba
import numpy as np
from os import path
d = path.dirname(__file__)

#import matplotlib as mpl
#mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
#mpl.rcParams['axes.unicode_minus'] = False

text_ = open(path.join(d,'apple letter.txt')).read()
wordlist = jieba.cut(text_,cut_all=True)
wordlist_space_split = ' '.join(wordlist)
apple_musk = np.array(Image.open(path.join(d,'apple_logo.png')))
stopwords = set(STOPWORDS)
stopwords.add('said')
wc = WordCloud(background_color='white',max_words=500,mask=apple_musk,\
               stopwords = stopwords)
#wc = WordCloud().generate(wordlist_space_split)
wc.generate(text_)
wc.to_file(path.join(d,'app.png'))

plt.figure(figsize=(15,10),dpi=150)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')


