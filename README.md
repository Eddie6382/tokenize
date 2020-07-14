這個資料夾主要與第一個baseline有關  

chinese/, english/存的是data base  
(training的順序與questions.json, 程式執行時會從這邊將所有題目讀進去-ReadFromJson())  

中文題目格式更正，需要將學長給的label題目的格式，更正成論文中所使用的data的格式  
需要注意的是，lSolutions需要自己手動改正
```bash
python genZhJson.py {origin format dir} {new format dir}
```
產生出.xml檔
```bash
python genXml.py {question dir} {parses dir} {language} 
```