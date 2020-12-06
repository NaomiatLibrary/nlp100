#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
from c430 import return_mecab
for s in return_mecab():
    for i in range(1,len(s)-1):
        if s[i-1]["pos"]=="名詞" and s[i+1]["pos"]=="名詞" and s[i]["surface"]=="の":
            print(s[i-1]["surface"],s[i]["surface"],s[i+1]["surface"])