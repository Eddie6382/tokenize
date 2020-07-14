import json
import sys
import os
import re


problemDir = sys.argv[1]
Dir = sys.argv[2]
problemList = []
DEBUG = False

def genEquations(content):
    content = re.sub('\n', '\n\n', content)
    content = '\n' + content + '\n'
    # print(content)
    foluma = r'\n.+[\+\-\*\/]+[\s]*[\w+\(\)\.]+[\s]*\=.+\n'
    lEquations = []
    for eq in re.findall(foluma, content):
        eq = eq.strip('\n')
        eq = re.sub('\s', '', eq)
        lEquations.append(eq)
    return lEquations

def createData(problemList):
    content = []
    for (iIndex, sQuestion, lSolutions, lEquations) in problemList:
        dictionary = {'iIndex':iIndex, 'sQuestion':sQuestion, 'lEquations':lEquations,'lSolutions':lSolutions}
        content.append(dictionary)
    # print(content)
    return content

with open(os.path.join(problemDir, 'cmwp__algebra1.json'), 'r') as json_file:
    data = json.loads(json_file.read())
    for question in data:
        problemList.append((question['pid'], question['problem'], question['answer'], genEquations(question['formula'])))
with open(os.path.join(problemDir, 'cmwp__algebra2.json'), 'r') as json_file:
    data = json.loads(json_file.read())
    for question in data:
        problemList.append((question['pid'], question['problem'], question['answer'], genEquations(question['formula'])))
# for (iIndex, sQuestion, lSolutions, lEquations) in problemList:
#     print(lEquations, sQuestion)

with open(os.path.join(Dir, 'questions.json'), 'w') as json_file:
    # print(json.dumps(problemList))
    json_file.write(json.dumps(createData(problemList), ensure_ascii=False, indent=2))



if DEBUG:
    text = "x:小偉幾歲; y:嬸嬸幾歲\nx+y=50\n(x+5)*3=y+5"
    text2 = "x:大球幾個; y:小球幾個\nx+y=40\n80*x+50*y=UnitTrans('2.9公斤', '公克')"
    print(genEquations(text2))