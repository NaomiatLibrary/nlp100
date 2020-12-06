#mecab neko.txt > neko.txt.mecab　の結果を読み込む
import re
def return_mecab():
    with open("neko.txt.mecab") as f:
        lines=f.readlines()
        sentences=[]
        sentence=[]
        for line in lines:
            if(line.strip()=="EOS"):
                if(len(sentence)>0):
                    sentences.append(sentence)
                sentence=[]
            else:
                #吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
                #surface\tpos,pos1,-,-,-,-,base,-,-
                surface=line.strip("\n").split("\t")
                infos=surface[1].split(",")
                dic={
                    "surface":surface[0],
                    "base":infos[6] if infos[6]!="*" else surface[0],
                    "pos": infos[0],
                    "pos1": infos[1]
                }
                sentence.append(dic)
        return sentences

if __name__ == "__main__":
    for s in return_mecab():
        print(s)
