import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is US 1 trillion dollor company")
