from c541 import Morph,Chunk,return_chunk


for sentence in return_chunk():
    for num in range(len(sentence)):
        #動詞を含む文節の時のみ
        if "動詞" not in [morph.pos if morph.pos!="記号" else "" for morph in sentence[num].morphs]:
            continue
        #動詞を抽出
        verb=[morph.base for morph in sentence[num].morphs if morph.pos=="動詞"][0]
        #掛かっている助詞を調べる
        pp=[]
        ppp=[]
        sahen=""
        for i in sentence[num].srcs:
            if "助詞" not in [morph.pos if morph.pos!="記号" else "" for morph in sentence[i].morphs]:
                continue
            #"サ変接続名詞+を"があるかどうか調べる
            if "サ変接続" == sentence[i].morphs[-2].pos1 and "を" == sentence[i].morphs[-1].surface:
                sahen=sentence[i].morphs[-2].surface + "を" + verb
            else:
                #助詞を抽出
                pp.append( [morph.base for morph in sentence[i].morphs if morph.pos=="助詞"][-1] )
                ppp.append( "".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[i].morphs]) )
        if sahen!="":
            print(sahen,*pp,*ppp)