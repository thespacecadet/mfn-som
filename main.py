import getDataSubjects
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
subject_data = getDataSubjects.data
#subject_results = getDataSubjects.subjects
corpus = []

#for i in 

# add all abstracts to the corpus list
for i in range(len(subject_data)):
    corpus.append(subject_data[i][0])

# produce tfidf vectorizer and transform the corpus to vectors
vectorizer = TfidfVectorizer(use_idf=True)
tfidf_result = vectorizer.fit_transform(corpus)

# get the first vector out (for the first document)
first_vector_tfidfvectorizer=tfidf_result[0]
 
# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names(), columns=["tfidf"])
df1 = df.sort_values(by=["tfidf"],ascending=False)
print(df1)
y = 4
