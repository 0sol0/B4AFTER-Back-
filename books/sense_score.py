import pandas as pd
from books.models import Review

book_sense = pd.read_csv('sense.csv')

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 300)


sentence = "모처럼 책을 읽고 따뜻했습니다. 아버지는 산에서 내려와 민중을 위한 사회주의를 완성했습니다. 그 아버지의 따뜻함을 받은 사람들의 마음을 통해 딸과 아버지는 화해를 이루게 되고 암데나 뿌레라는 아버지의 말처럼 이제 암데나 뿌려진 아버지의 정신을 느끼며 살아가겠지요. 전라도 사투리가 이렇게 구수한지 정말 재미있습니다."

sentence_words_strip = []
sentence_split = sentence.split()
for sentence_words in sentence_split:
    sentence_words_strip.append(sentence_words.rstrip("."",""!""?""을""를""은""는""의""으로""있게""에서""하게""입니다""했습니다""들""과""할""정도""으로의""이었다""그냥""그러나""하셔서"
    "합니다""일본""군대""한국""김훈""들에게""하고""와""뿐""되어""된""이네요""들이""하는""으로나마"))

print(sentence_words_strip)

positive_score = 0
nagative_score = 0
for i in sentence_words_strip:

    if book_sense[book_sense['term'] == i].empty == True:
        pass
    else:
        words = book_sense[book_sense['term'] == i]

        print(words, words['positive_score'].values)
        positive_score += words['positive_score'].values[0]
        nagative_score += words['nagative_score'].values[0]

print(positive_score)
print(nagative_score)

positive_per = positive_score / (positive_score + nagative_score) * 100
nagative_per = nagative_score / (positive_score + nagative_score) * 100

print(positive_per)
print(nagative_per)