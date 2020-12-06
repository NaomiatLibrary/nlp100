#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
from c430 import return_mecab

for s in return_mecab():
    for token in s:
        if token["pos"]=="動詞":
            print(token["surface"],token["base"])