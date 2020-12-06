#cabocha -f1 -o ai.ja.txt.parsed ai.ja.txt の結果を
class Morph:
    def __init__(self,cabocha_result):
        surfaces=cabocha_result.strip("\n").split("\t")
        infos=surfaces[1].split(",")
        self.surface=surfaces[0]
        self.base=infos[6] if infos[6]!="*" else surfaces[0]
        self.pos=infos[0]
        self.pos1=infos[1]
def return_morph():
    with open("ai.ja.txt.parsed") as f:
        lines=f.readlines()
        sentences=[]
        sentence=[]
        for line in lines:
            if(line.strip()=="EOS"):
                if(len(sentence)>0):
                    sentences.append(sentence)
                sentence=[]
            elif(line[0]=='*'):
                pass
            else:
                morph=Morph(line.strip())
                sentence.append(morph)
        return sentences

if __name__ == "__main__":
    for s in return_morph():
        for t in s:
            print(t.surface,end="/")
        print("")
