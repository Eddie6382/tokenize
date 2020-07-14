from stanfordcorenlp import StanfordCoreNLP
from opencc import OpenCC

# Preset
# 用with就不必使用nlp.close()
with StanfordCoreNLP('../stanford-corenlp-full-2018-10-05/', lang='zh', memory='8g') as nlp:
    text = '姐姐和淑慧共做了52朵緞帶花，姐姐做的緞帶花數量是淑慧做的3倍，淑慧做了多少朵緞帶花？' \
       '好喝果汁店今天賣出的蘋果汁數量是芭樂汁的5倍，今天共賣出250杯芭樂汁，好喝果汁店今天賣出的蘋果汁和芭樂汁數量相差多少杯？'
    props={'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse','pipelineLanguage':'zh','outputFormat':'xml'}
    # print(nlp.annotate(text, properties=props))
    with open("output.xml", "w") as f:
        f.write(nlp.annotate(text, properties=props))