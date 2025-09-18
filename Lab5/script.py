import spacy
from spacy import displacy

nlp = spacy.load("it_core_news_sm")


# Testo da analizzare
testo = "Commenta i risultati del 20 Settembre della squadra Juventus, specifica il numero di gol di Alessandro Del Piero."

# Analisi
doc = nlp(testo)
'''
# Output analisi
for token in doc:
    print(f"Token: {token.text:12} | Lemma: {token.lemma_:12} | POS: {token.pos_:10} | Dipendenza: {token.dep_:10} | Head: {token.head.text}")
'''

displacy.serve(doc, style="dep", port=8654, host="127.0.0.1")