#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
from c430 import return_mecab
import matplotlib.pyplot as plt
#日本語フォントを導入してください
#参考:https://qiita.com/knknkn1162/items/be87cba14e38e2c0f656
plt.rcParams["font.family"] = "IPAGothic" 

freq={}#key:base,value:freq
for s in return_mecab():
    for t in s:
        if t["base"] in freq:
            freq[t["base"]]=freq[t["base"]]+1
        else:
            freq[t["base"]]=1
#sort by value
x=[]
for token in sorted(freq.items(), key=lambda x:-x[1]):
    x.append(token[1])
plt.hist(x)
plt.show()
        
