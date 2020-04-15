import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk


#this files gives an overview of certains steps that could help to analyze the comments in one way or the other
#not every step is useful but can give an better overview of the text
df = pd.read_csv('comments-zb0LgL32rro.csv')

df.drop(['replies.id', 'replies.user', 'replies.date',
       'replies.timestamp', 'replies.commentText', 'replies.likes'], inplace=True, axis=1)
df.dropna(inplace = True)


df['word_count'] = df['commentText'].apply(lambda x: len(str(x).split(" ")))
#counting the number of words

df['char_count'] = df['commentText'].str.len()
#counting the number of characters in a comment. It'll include white spaces too.


from nltk.corpus import stopwords

#to count the number of stopwords used in the given comment
stop = stopwords.words('english')
df['stopwords'] = df['commentText'].apply(lambda x: len([x for x in x.split() if x in stop]))

#to count the number of hashtags used in the given comment
df['hastags'] = df['commentText'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))

#to count the number of numerics used in the given comment
df['numerics'] = df['commentText'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))

#to convert the complete text to the lower case
df['comment'] = df['commentText'].apply(lambda x: " ".join(x.lower() for x in x.split()))

#to remove certain patterns from the comments using regular expression
df['comment'] = df['comment'].str.replace('[^\w\s]','')

#to remove the stopwords from the comments
df['comment'] = df['comment'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
