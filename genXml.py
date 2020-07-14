from stanfordcorenlp import StanfordCoreNLP
import json
import sys
import os
from tqdm import tqdm
import random

# arguments:   ../chinese_algebra, parses, zh/en
if len(sys.argv) != 4:
    print('Please Provide the Data Dir(1), Saving Dir(2), language(en/zh 3)')
    exit()

problemDir = sys.argv[1]
Dir = sys.argv[2]
language = sys.argv[3]
problemList = []
with open(os.path.join(problemDir, 'questions.json'), 'r') as json_file:
    data = json.loads(json_file.read())
    for question in data:
        problemList.append((question['iIndex'], question['sQuestion']))

print('\n\n======  READING FILE =======')
for (pid, question) in problemList:
    # print(pid, question)
    # print(pid)

    save_file = ''.join(('question-', str(pid)))
    path = os.path.join('questions', save_file)
    with open(path, 'w') as f:
        f.write(question)

print('\n\n====== STANFORD PARSING =======')
with StanfordCoreNLP('http://140.109.19.191', port=9000, lang=language, memory='8g') as nlp:
    props={'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,coref','pipelineLanguage':language,'outputFormat':'xml'}
    for (pid, question) in tqdm(problemList):
        save_file = ''.join(('question-', str(pid), '.xml'))
        path = os.path.join(Dir, save_file)
        with open(path, "w") as f:
            f.write(nlp.annotate(question, properties=props))