import stanza

nlp = stanza.Pipeline(lang='zh', processors='tokenize')
doc = nlp('我就爛')
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')