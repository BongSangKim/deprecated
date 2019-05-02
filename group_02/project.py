#original code 'spring19-se201-group-02.ipynb' from github.com/HyosangKang/LinearAlgebra/Project/Group_02
# Made by Prof. HyosangKang, edit. by BongSangKim
 
from gensim.models import Word2Vec
import gensim.utils

text = []
for ind in range(48):
    indstr = str(ind)
    filename = "obama_speeches_" + str(indstr.zfill(3)) + ".txt" #위치는 .py파일위치에 두기,  #zfill은 빈자리 0채우는 갯수
    with open(filename) as file:
        line = file.readline()
        while line:
            text.append(gensim.utils.simple_preprocess(line))
            line = file.readline()

ob = Word2Vec(text, size=10, window=5, min_count=1, workers=4) #size 벡터의 차원
ob.train(text, total_examples=len(text), epochs=10) #epochs 반복횟수, 100으로 설정하기, test중은 10으로 설정

print(ob.wv['war'])

ob.wv.most_similar(positive='people')


'''이제 trump 부분코드'''
#from gensim.models import Word2Vec 이거는 겹치니까 다시 import 안해도됨
#import gensim.utils

text = []
for ind in range(18):
    indstr = str(ind)
    filename = "trump_speeches_" + str(indstr.zfill(3)) + ".txt"
    with open(filename) as file:
        line = file.readline()
        while line:
            text.append(gensim.utils.simple_preprocess(line))
            line = file.readline()

dt = Word2Vec(text, size=10, window=5, min_count=1, workers=4) #오바마와 트럼프 학습 환경 일치시키기
dt.train(text, total_examples=len(text), epochs=10) #오바마와 트럼프 학습 환경 일치시키기, epochs 100으로 설정하기

print(dt.wv['war'])

dt.wv.most_similar(positive='people')



import gensim 
from os import walk

file_list = []
current_path = "./Obama/"
for (dirpath, dirnames, filenames) in walk(current_path):
    file_list.extend(filenames)
    break