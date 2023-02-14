#Importing spacy, using this time "nlp = spacy.load('en_core_web_md')"
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print("-----------------------------------------------------")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("-----------------------------------------------------")

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    print("-----------------------------------------------------")
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
print("-----------------------------------------------------")
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("-----------------------------------------------------")

'''Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own.

One of the first things I noticed is that there is some relationship between words and their class

Between Cat and monkey there is a lot of similarity not because the letters but that both designates animals.

Another curious one is between banana and monkey, that it is low "0.4041", but it is traditionaly one of the prefered
food for monkeys. Not happening the same with monkey and apple. '''

tokens = nlp('car wheel tyre cleaner')
for token3 in tokens:
    print("-----------------------------------------------------")
    for token4 in tokens:
        print(token3.text, token4.text, token3.similarity(token4))
print("-----------------------------------------------------")

'''I decided to check 'car wheel tyre cleaner':
There is some interesting similarities between car tyre and wheel
not so much with cleaner, just sligthly bigger between cleaner and car.'''

'''The difference between "en_core_web_sm" and 'en_core_web_md' is:

    - On 'en_core_web_sm' I get the following warning:

    UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, 
    which may not give useful similarity judgements. 
    This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
    You can always add your own word vectors, or use one of the larger models instead if available.

    -This is giving different values on the similarity rating. For example: Between car and cleaner
        - With md I obtained: 0.32639
        - With sm I obtained: 0.048241
    There is a big influence in this case.
'''