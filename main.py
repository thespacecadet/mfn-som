import getDataSubjects
import pandas as pd
from som import *
from sklearn.feature_extraction.text import TfidfVectorizer

subject_data = getDataSubjects.data
abstract_subject = getDataSubjects.abstract_subject
#subject_results = getDataSubjects.subjects
corpus = []

#for i in 

# add all abstracts to the corpus list
for i in range(len(subject_data)):
    corpus.append(subject_data[i][0])

# produce tfidf vectorizer and transform the corpus to vectors
vectorizer = TfidfVectorizer(use_idf=True,min_df=2,max_df=10)
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
som(tfidf_lists,term_list,len(term_list))
 
# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names(), columns=["tfidf"])
df1 = df.sort_values(by=["tfidf"],ascending=False)
print(df1)
y = 4
