#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
from c430 import return_mecab
for s in return_mecab():
    cnt=0
    for i in range(len(s)-1):
        if s[i]["pos"]!="名詞":
            if cnt>=2:
                print(*[s[j]["surface"] for j in range(i-cnt,i)])
            cnt=0
        else:
            cnt+=1
