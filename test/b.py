from stanfordcorenlp import StanfordCoreNLP
from opencc import OpenCC

# Preset
nlp = StanfordCoreNLP('../stanford-corenlp-full-2018-10-05/', lang='zh', memory='8g')
cc = OpenCC('t2s')

# 要解析的句子
sentence = '我吃了一顆又紅又大的蘋果。'

# 詞性標記
print('Pos：', nlp.pos_tag(sentence))
# 斷詞
print('Tokenize：', nlp.word_tokenize(sentence))
# 命名實體識別
print('Ner：', nlp.ner(sentence))
# 解析器
print('Parse：')
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))

# 關閉 Stanford Parser
nlp.close()