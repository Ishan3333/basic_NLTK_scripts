#IMPORT NECESSARY LIBRARIES
import nltk
from nltk import word_tokenize
from nltk.corpus import state_union
# PUNKTSENTENCETOKENIZER IS A BUILT IN UNSUPERVISED MACHINE LEARNING TOKENIZER. COMES PRE-TRAINED AND IT IS TRAINABLE AS WELL
from nltk.tokenize import PunktSentenceTokenizer

#PARSING THE TRAINING DATA
train_text = state_union.raw('2005-GWBush.txt')

#PARSING THE TESTING DATA
sample_text = state_union.raw('2006-GWBush.txt')

#TRAINING THE TOKENIZER WITH THE TRAINING DATA
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#SETTING UP THE TRAINED TOKENIZER WITH THE TESTING DATA SET
tokenized = custom_sent_tokenizer.tokenize(sample_text)

#FUNCTION TO RUN THROUGH TOKENIZED WORDS AND PARSE ALL THE ENTITY NAME
def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as e:
        print(str(e))

process_content()