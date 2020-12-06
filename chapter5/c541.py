#cabocha -f1 -o ai.ja.txt.parsed ai.ja.txt の結果を
class Morph:
    def __init__(self,cabocha_result):
        surfaces=cabocha_result.strip("\n").split("\t")
        infos=surfaces[1].split(",")
        self.surface=surfaces[0]
        self.base=infos[6] if infos[6]!="*" else surfaces[0]
        self.pos=infos[0]
        self.pos1=infos[1]
class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morphs=morphs
        self.dst=dst
        self.srcs=srcs
def return_chunk():
    with open("ai.ja.txt.parsed") as f:
        lines=f.readlines()
        sentences=[]
        chunk_morphs={}
        chunk_dst={}
        chunk_srcs={}
        cnt=-1
        for line in lines:
            if line.strip()=="EOS":
                #文の最後でまとめて処理
                if(cnt<0):
                    continue
                sentence=[]
                for i in range(cnt+1):
                    chunk=Chunk(chunk_morphs[i],chunk_dst[i],chunk_srcs[i])
                    sentence.append(chunk)
                if(len(sentence)>0):
                    sentences.append(sentence)
                chunk_morphs={}
                chunk_dst={}
                chunk_srcs={}
                cnt=-1
            elif(line[0]=='*'):
                infos=line.strip().split(" ")
                num=int(infos[1])
                dst=int(infos[2][:-1])
                chunk_dst[num]=dst
                if num not in chunk_srcs:
                    chunk_srcs[num]=[]
                if dst!=-1:
                    if dst in chunk_srcs:
                        chunk_srcs[dst].append(num)
                    else:
                        chunk_srcs[dst]=[num,]
                chunk_morphs[num]=[]
                cnt=num
            else:
                morph=Morph(line.strip())
                chunk_morphs[cnt].append(morph)
        return sentences

if __name__ == "__main__":
    for s in return_chunk():
        cnt=0
        for chunk in s:
            print(cnt,end=":")
            for morph in chunk.morphs:
                print(morph.surface,end="/")
            print(chunk.dst,end="/")
            print(chunk.srcs,end="\n")
            cnt+=1
        print("\n")
