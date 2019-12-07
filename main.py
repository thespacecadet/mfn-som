import getData
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
results = getData.data
corpus = []
for i in range(len(results)):
    corpus.append(results[i][0])
vectorizer = TfidfVectorizer(use_idf=True)
tfidf_result = vectorizer.fit_transform(corpus)

# get the first vector out (for the first document)
first_vector_tfidfvectorizer=tfidf_result[0]
 
# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names(), columns=["tfidf"])
df1 = df.sort_values(by=["tfidf"],ascending=False)
print(df1)
y = 4
