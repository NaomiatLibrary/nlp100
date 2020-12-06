from c541 import Morph,Chunk,return_chunk


for sentence in return_chunk():
    for chunk in sentence:
        if chunk.dst != -1:
            modifier="".join([morph.surface if morph.pos!="記号" else "" for morph in chunk.morphs])
            modifiee="".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[chunk.dst].morphs])
            print(modifier,modifiee,sep="\t")