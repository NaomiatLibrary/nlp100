from c541 import Morph,Chunk,return_chunk


for sentence in return_chunk():
    for chunk in sentence:
        if chunk.dst != -1:
            #名刺を含む分節かどうかチェック
            if "名詞" not in [morph.pos if morph.pos!="記号" else "" for morph in chunk.morphs]:
                continue
            if "動詞" not in [morph.pos if morph.pos!="記号" else "" for morph in sentence[chunk.dst].morphs]:
                continue
            modifier="".join([morph.surface if morph.pos!="記号" else "" for morph in chunk.morphs])
            modifiee="".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[chunk.dst].morphs])
            print(modifier,modifiee,sep="\t")