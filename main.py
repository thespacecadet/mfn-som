import getDataSubjects
import json
import create_map_file
import pandas as pd
from som import *
from sklearn.feature_extraction.text import TfidfVectorizer


# make lists of german stopwords, english stopwords, and one list of all stopwords together
with open("Data/stopwords_de.json") as json_file:
    german_stopwords = json.load(json_file)
with open("Data/stopwords_eng.json") as json_file:
    english_stopwords = json.load(json_file)
all_stopwords = german_stopwords + english_stopwords

subject_data = getDataSubjects.data
abstract_subject = getDataSubjects.abstract_subject
weight_counter = getDataSubjects.weight_counter

#convert abstract subjects to list
# index 0 in each item is the subject name, index 1 is the addition of all abstracts
abstract_subject_list = []
abstract_subject_list = [[k, v] for k, v in abstract_subject.items()] 

#for key, value in abstract_subject.iteritems():
 #   temp = [key,value]
  #  abstract_subject_list.append(temp)

corpus = []

# add all abstracts to the corpus list.
for i in range(len(abstract_subject_list)):
    corpus.append(abstract_subject_list[i][1])

# produce tfidf vectorizer and transform the corpus to vectors
vectorizer = TfidfVectorizer(use_idf=True,min_df=2,max_df=10, stop_words=all_stopwords)
tfidf_result = vectorizer.fit_transform(corpus)


#turn to list of lists
tfidf_lists = []
for i in range(tfidf_result.shape[0]):
    dense_matrix = tfidf_result[i].todense()
    dense_list = dense_matrix.tolist()
    tfidf_lists.append(dense_list[0])

term_list = vectorizer.get_feature_names()

# get the first vector out (for the first document)
first_vector_tfidfvectorizer=tfidf_result[0]
som_data = som(tfidf_lists,term_list,len(term_list))
som_map = som_data[0]
#process data and create map file 
filename = "blae1"
s = create_map_file.create_map(filename,som_map,abstract_subject_list,weight_counter)


# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names(), columns=["tfidf"])
df1 = df.sort_values(by=["tfidf"],ascending=False)
print(df1)
y = 4
