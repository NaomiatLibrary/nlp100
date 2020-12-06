from c541 import Morph,Chunk,return_chunk
from graphviz import Digraph

G = Digraph(format='png')
G.attr('node', shape='circle')

sentence=return_chunk()[2]
for num in range(len(sentence)):
    #ノードの追加
    node_name="".join([morph.surface if morph.pos!="記号" else "" for morph in sentence[num].morphs])
    G.node(str(num),node_name)
for num in range(len(sentence)):
    if sentence[num].dst != -1:
        modifier=num
        modifiee=sentence[num].dst
        G.edge(str(modifier),str(modifiee))

G.render("tree")