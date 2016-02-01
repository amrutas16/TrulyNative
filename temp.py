from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize as wt
from nltk.stem import PorterStemmer
from collections import OrderedDict
from textblob import TextBlob as tblob
from sklearn.feature_extraction.text import CountVectorizer as CV
import sys
import math
ps = PorterStemmer()
filtered_array = []
filtered_doc = ''
list_of_docs = []

def initial_work():
    with open('C:/Users/Isha/Desktop/AldaSampling/data/StopWords.txt', 'rb') as infile:
            splitwordslist = infile.read().decode('UTF-8')
    myfilehtml = open('C:/Users/Isha/Desktop/AldaSampling/output/Processed/unsponsored/1010023_raw_html.txt')
    soup = BeautifulSoup(myfilehtml,'html.parser')
    for scriptdata in soup.findAll('script'):
        scriptdata.extract()
    result = soup.get_text().lower()
    output=open("output.txt","w")
    output.write(result)
    tokenized_text = wt(result)
    stop_words = wt(splitwordslist)
    for words in tokenized_text:
        if words not in stop_words:
            if words.isalpha():
                filtered_array.append(ps.stem(words))
    print(len(filtered_array))
    print(filtered_array)

    filtered_doc = ' '.join(filtered_array)
    print(filtered_doc)
    list_of_docs.append(tblob(filtered_doc))
    list_of_docs.append(tblob('experi unicorn astro table'))
    print(list_of_docs)

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, list_of_docs):
    return sum(1 for blob in list_of_docs if word in blob)

def idf(word, list_of_docs):
    return math.log(len(list_of_docs) / (1 + n_containing(word, list_of_docs)))

def tfidf(word, blob, list_of_docs):
    return tf(word, blob) * idf(word, list_of_docs)

def main(argv):
    '''
    :param argv:
    :return
    '''
    initial_work()

    for i, blob in enumerate(list_of_docs):
        print("Top words in document {}".format(i + 1))
        scores = {eachword: tfidf(eachword, blob, list_of_docs) for eachword in blob.words}
        print(scores)
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        print(sorted_words)
        for eachword, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(eachword, round(score, 5)))

if __name__ == "__main__":
    main(sys.argv)