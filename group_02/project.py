#original code 'spring19-se201-group-02.ipynb' from github.com/HyosangKang/LinearAlgebra/Project/Group_02
# Made by Prof. HyosangKang, edit. by BongSangKim
# 파일명은 github data 기반


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


def read_input(current_path, file_list):
    for i in range(len(file_list)):
        with open(current_path + file_list[i]) as file:
            for j, line in enumerate(file):
                yield gensim.utils.simple_preprocess(line)

document = list(read_input(current_path, file_list))


ob_model = gensim.models.Word2Vec (document, size=50, window=10, min_count=2, workers=4)
ob_model.train(document, total_examples=len(document), epochs=100)

########################Trump 부분-.py파일 나눠야 하는지 공부####################################
file_list = []
current_path = "./Trump/"
for (dirpath, dirnames, filenames) in walk(current_path):
    file_list.extend(filenames)
    break

document = list(read_input(current_path, file_list))

tp_model = gensim.models.Word2Vec (document, size=50, window=10, min_count=2, workers=4)
tp_model.train(document, total_examples=len(document), epochs=500)

print(ob_model.wv.vocab['america'].count) #특정 voca 갯수 체크하는 코드

print(ob_model.wv['america']) #특정 voca 벡터 체크하는 코드

tp_model.wv.most_similar(positive = ['american'], topn=20) 
#특정 voca와 비슷한 wordvector들 출력 (voca,cos값)
#positive, negative, topn은 출력하는 벡터 갯수

####
wordlist = []
count = []
for word, obj in ob_model.wv.vocab.items():
    wordlist.append(word)
    count.append(obj.count)
for _ in range(100):
    idx = count.index(max(count))
    print(wordlist[idx], max(count))
    del count[idx]
    del wordlist[idx]
####
#최빈출 워드 출력 코드
    
    
###추가할 코드###
'''그람 슈미츠 코드'''    