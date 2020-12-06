#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
from c430 import return_mecab
freq={}#key:base,value:freq
for s in return_mecab():
    for t in s:
        if t["base"] in freq:
            freq[t["base"]]=freq[t["base"]]+1
        else:
            freq[t["base"]]=1
#sort by value
for token in sorted(freq.items(), key=lambda x:-x[1]):
    print(token[0],token[1])
        
