#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pdfplumber
import spacy
from spacy.tokens import doc
import enchant
nlp = spacy.load('en_core_web_sm')
directory=os.listdir(r'C:\Users\Ralph\Downloads\Ralph NLP')
is_pdf=[]
for pdfs in directory:
    if pdfs.endswith('.pdf'):
        is_pdf.append(pdfs)
print(is_pdf)

for i in range(0, len(is_pdf)-1, 1):
    pdf = pdfplumber.open(is_pdf[i])
    for page in pdf.pages:
        text = str(page.extract_text())
       
        with open(str(''.join(e for e in is_pdf[i] if (e.isalnum() or e.isspace()))) +".txt", 'a', encoding='utf-8') as fp:
            fp.write(str(text))

is_txt_file=[]
directory=os.listdir(r'C:\Users\Ralph\Downloads\Ralph NLP')
for txt_file in directory:
    if txt_file.endswith('.txt'):
        is_txt_file.append(txt_file)

for k in range(0, len(is_txt_file)-1, 1):
    
    myfile = open(str(is_txt_file[k]), 'r' , encoding='utf-8')
    print(myfile)
   

    raw_txt = myfile.read()

    doc = nlp(raw_txt)

    word_count_dict = {}
    word_count_dict['NOUN'] = {}
    word_count_dict['PROPN'] = {}
    word_count_dict['ADJ'] = {}
    word_count_dict['VERB'] = {}

    for token in doc: 
        
        part_of_speech = token.pos_
        if part_of_speech in ['NOUN', 'PROPN', 'ADJ', 'VERB'] and token.is_stop == False:
            word_lemma = token.lemma_

            new_word=''.join(e for e in word_lemma if (e.isalnum() or e.isspace()))
            American_English= enchant.Dict("en_US")
            British_English= enchant.Dict("en_GB")
            

            if len(new_word)<=2:
                pass
            elif new_word.isdigit()==True:
                pass

            elif British_English.check(new_word)==True or American_English.check(new_word)==True:
                current_count = word_count_dict[part_of_speech].get(new_word, 0)

                current_count += 1
                word_count_dict[part_of_speech][new_word] = current_count


            else:
                pass

    print(word_count_dict)


# In[ ]:




