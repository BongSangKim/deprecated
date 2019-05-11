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
ob.train(text, total_examples=len(text), epochs=1000) #epochs 반복횟수, 100으로 설정하기, test중은 10으로 설정

#print(ob.wv['war'])
#ob.wv.most_similar(positive='people')


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
dt.train(text, total_examples=len(text), epochs=1000) #오바마와 트럼프 학습 환경 일치시키기, epochs 100으로 설정하기

#print(dt.wv['war'])
#dt.wv.most_similar(positive='people')

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

ob_model = gensim.models.Word2Vec (document, size=10, window=10, min_count=2, workers=4) #size 변경
ob_model.train(document, total_examples=len(document), epochs=1000)

########################Trump 부분-.py파일 나눠야 하는지 공부####################################
file_list = []
current_path = "./Trump/"
for (dirpath, dirnames, filenames) in walk(current_path):
    file_list.extend(filenames)
    break

document = list(read_input(current_path, file_list))

tp_model = gensim.models.Word2Vec (document, size=10, window=10, min_count=2, workers=4) #size 변경
tp_model.train(document, total_examples=len(document), epochs=1000)

#print(ob_model.wv.vocab['america'].count) #특정 voca 갯수 체크하는 코드
#print(ob_model.wv['hate']) #특정 voca 벡터 체크하는 코드

#tp_model.wv.most_similar(positive = ['american'], topn=20) 
#특정 voca와 비슷한 wordvector들 출력 (voca,cos값)
#positive, negative, topn은 출력하는 벡터 갯수

'''
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

'''

'''

#=============================test- t-SNE=====================================
keys = ['america', 'korea', 'muslims', 'world']

embedding_clusters = []
word_clusters = []
for word in keys:
    embeddings = []
    words = []
    for similar_word, _ in tp_model.wv.most_similar(word, topn=50): ###model부분 바꾸기
        words.append(similar_word)
        embeddings.append(tp_model.wv[similar_word])                ##model 부분 바꾸기
    embedding_clusters.append(embeddings)
    word_clusters.append(words)
    
from sklearn.manifold import TSNE
import numpy as np

embedding_clusters = np.array(embedding_clusters)
n, m, k = embedding_clusters.shape
tsne_model_en_2d = TSNE(perplexity=15, n_components=2, init='pca', n_iter=3500, random_state=32)
embeddings_en_2d = np.array(tsne_model_en_2d.fit_transform(embedding_clusters.reshape(n * m, k))).reshape(n, m, 2)

import matplotlib.pyplot as plt
import matplotlib.cm as cm

def tsne_plot_similar_words(title, labels, embedding_clusters, word_clusters, a, filename=None):
    plt.figure(figsize=(16, 9))
    colors = cm.rainbow(np.linspace(0, 1, len(labels)))
    for label, embeddings, words, color in zip(labels, embedding_clusters, word_clusters, colors):
        x = embeddings[:, 0]
        y = embeddings[:, 1]
        plt.scatter(x, y, alpha = a, label = label)
        for i, word in enumerate(words):
            plt.annotate(word, alpha=0.5, xy=(x[i], y[i]), xytext=(5, 2),
                         textcoords='offset points', ha='right', va='bottom', size=8)
    plt.legend(loc=4)
    plt.title(title)
    plt.grid(True)
    if filename:
        plt.savefig(filename, format='png', dpi=300, bbox_inches='tight')
    plt.show()


tsne_plot_similar_words('Similar words', keys, embeddings_en_2d, word_clusters, 0.7,
                        'similar_words.png')
#=============================test- t-SNE=====================================

#return gram schmidt-basis 의미 찾기?????????????
import numpy as np
def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X,mode='complete')
    return Q
def stack(x,y):
    return np.column_stack((x,y))
A_a=stack(ob.wv['war'],ob.wv['america'])
print(gram_schmidt_columns(A_a))
print(ob.wv['war'])
'''
'''
가중치 행렬
obama, trump에 대해 동일한 10개의 단어 선정 
각각 obama, trump에 대해
행:단어 1~10
열:단어 1~10
america, korea, we, economy, global, hate, muslim, labor, world, people
np.array([])
행렬 A_ij= i와 j 사이의 거리
W행렬(가중치 행렬)
W_ij=exp(-A_ij/(2*sigma^2)) #https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/
#W_ij=유클리디안 거리를 가우시안 분포로 정규화한 수치, 각 벡터의 가중치를 나타낸다.
sigma^2=A_ij의 분산..
여기서 한 행이나 한 열만 가져오면 각 단어의 가중치를 얻는다.

'''
import numpy as np
def stack(x,y):
    return np.column_stack((x,y))
###############OBAMA 단어 가중치 행렬 구하기###########################
def list_word_obama(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10):
    print("Priority order of President Obama", end='\n\n')
    word_list=[w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
    word=[ob.wv[w1],ob.wv[w2],ob.wv[w3],ob.wv[w4],ob.wv[w5],ob.wv[w6],ob.wv[w7],ob.wv[w8],ob.wv[w9],ob.wv[w10]]
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=[],[],[],[],[],[],[],[],[],[]
    for i in range(len(word)):
        c1.append((sum(word[0]-word[i])**2)) #row vector
        c2.append((sum(word[1]-word[i])**2)) 
        c3.append((sum(word[2]-word[i])**2)) 
        c4.append((sum(word[3]-word[i])**2)) 
        c5.append((sum(word[4]-word[i])**2)) 
        c6.append((sum(word[5]-word[i])**2)) 
        c7.append((sum(word[6]-word[i])**2)) 
        c8.append((sum(word[7]-word[i])**2)) 
        c9.append((sum(word[8]-word[i])**2)) 
        c10.append((sum(word[9]-word[i])**2)) 
        var=np.var(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10)
    for i in range(10):
        c1[i]=np.exp(-c1[i]/(2*var))
        c2[i]=np.exp(-c2[i]/(2*var))
        c3[i]=np.exp(-c3[i]/(2*var))
        c4[i]=np.exp(-c4[i]/(2*var))
        c5[i]=np.exp(-c5[i]/(2*var))
        c6[i]=np.exp(-c6[i]/(2*var))
        c7[i]=np.exp(-c7[i]/(2*var))
        c8[i]=np.exp(-c8[i]/(2*var))
        c9[i]=np.exp(-c9[i]/(2*var))
        c10[i]=np.exp(-c10[i]/(2*var))
    W=stack(stack(stack(stack(stack(stack(stack(stack(stack(c1,c2),c3),c4),c5),c6),c7),c8),c9),c10) #row vector를 10 by 10 matrix로 결합
    #각각의 c_n column은 가중치 column vector이다.
    CoUnt=[ob_model.wv.vocab[w1].count,ob_model.wv.vocab[w2].count,ob_model.wv.vocab[w3].count,ob_model.wv.vocab[w4].count,ob_model.wv.vocab[w5].count,ob_model.wv.vocab[w6].count,ob_model.wv.vocab[w7].count,ob_model.wv.vocab[w8].count,ob_model.wv.vocab[w9].count,ob_model.wv.vocab[w10].count]
    result=list(np.dot(W,CoUnt))
    sunseo=sorted(result)
    idx=sunseo.copy()
    for i in range(len(result)):
        idx[i]=result.index(sunseo[i])
    for i in range(len(word_list)):
        print(word_list[idx[i]])
        #단어 10개를 넣으면 해당 대통령이 중요하게 생각하는 것으로 추측되는 순서대로 열 개 출력
    print('\n')
    return None

###############TRUMP 단어 가중치 행렬 구하기###########################
def list_word_trump(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10):
    print("Priority order of President Trump", end='\n\n')
    word_list=[w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
    word=[dt.wv[w1],dt.wv[w2],dt.wv[w3],dt.wv[w4],dt.wv[w5],dt.wv[w6],dt.wv[w7],dt.wv[w8],dt.wv[w9],dt.wv[w10]]
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=[],[],[],[],[],[],[],[],[],[]
    for i in range(len(word)):
        c1.append((sum(word[0]-word[i])**2)) #row vector
        c2.append((sum(word[1]-word[i])**2)) 
        c3.append((sum(word[2]-word[i])**2)) 
        c4.append((sum(word[3]-word[i])**2)) 
        c5.append((sum(word[4]-word[i])**2)) 
        c6.append((sum(word[5]-word[i])**2)) 
        c7.append((sum(word[6]-word[i])**2)) 
        c8.append((sum(word[7]-word[i])**2)) 
        c9.append((sum(word[8]-word[i])**2)) 
        c10.append((sum(word[9]-word[i])**2)) 
        var=np.var(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10)
    for i in range(10):
        c1[i]=np.exp(-c1[i]/(2*var))
        c2[i]=np.exp(-c2[i]/(2*var))
        c3[i]=np.exp(-c3[i]/(2*var))
        c4[i]=np.exp(-c4[i]/(2*var))
        c5[i]=np.exp(-c5[i]/(2*var))
        c6[i]=np.exp(-c6[i]/(2*var))
        c7[i]=np.exp(-c7[i]/(2*var))
        c8[i]=np.exp(-c8[i]/(2*var))
        c9[i]=np.exp(-c9[i]/(2*var))
        c10[i]=np.exp(-c10[i]/(2*var))
    W=stack(stack(stack(stack(stack(stack(stack(stack(stack(c1,c2),c3),c4),c5),c6),c7),c8),c9),c10) #row vector를 10 by 10 matrix로 결합
    #각각의 c_n column은 가중치 column vector이다.
    CoUnt=[tp_model.wv.vocab[w1].count,tp_model.wv.vocab[w2].count,tp_model.wv.vocab[w3].count,tp_model.wv.vocab[w4].count,tp_model.wv.vocab[w5].count,tp_model.wv.vocab[w6].count,tp_model.wv.vocab[w7].count,tp_model.wv.vocab[w8].count,tp_model.wv.vocab[w9].count,tp_model.wv.vocab[w10].count]
    result=list(np.dot(W,CoUnt))
    sunseo=sorted(result)
    idx=sunseo.copy()
    for i in range(len(result)):
        idx[i]=result.index(sunseo[i])
    for i in range(len(word_list)):
        print(word_list[idx[i]])
        #단어 10개를 넣으면 해당 대통령이 중요하게 생각하는 것으로 추측되는 순서대로 열 개 출력
    print('\n')
    return None
###############
list_word_obama('america','korea','we','economy','global','hate','muslim','labor','world','people')
list_word_trump('america','korea','we','economy','global','hate','muslim','labor','world','people')
