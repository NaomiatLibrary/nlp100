from c541 import Morph,Chunk,return_chunk


for sentence in return_chunk():
    for num in range(len(sentence)):
        #名詞を含む文節の時
        if "名詞" not in [morph.pos for morph in sentence[num].morphs]:
            continue
        print("".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[num].morphs]),end=" ")
        next_chunk=sentence[num].dst
        while next_chunk!=-1 :
            print("->","".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[next_chunk].morphs]),end=" ")
            next_chunk=sentence[next_chunk].dst
        print("")
