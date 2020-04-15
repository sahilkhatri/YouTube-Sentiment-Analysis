from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(sentence):
    
    sid_obj = SentimentIntensityAnalyzer()            #SentimentIntensityAnalyzer class has the function "polarity_scores()",
                                                      #which takes the sentence as input and retunrns the dictionary of scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)#This dictionary gives 4 values: Positive, Neutral, Negative, and Compound score  
                                                      #of the sentence given as input
    return sentiment_dict['compound']                 #This function specifically returns the Compound score
    
    
def positive_scores(sentence):
    
    sid_obj = SentimentIntensityAnalyzer()
    
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    return sentiment_dict['pos']                      #This function specifically returns the Positive score

def negative_scores(sentence):
    
    sid_obj = SentimentIntensityAnalyzer()
    
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    return sentiment_dict['neg']                      #This function specifically returns the Negative score

def neutral_scores(sentence):
    
    sid_obj = SentimentIntensityAnalyzer()
    
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    return sentiment_dict['neu']                      #This function specifically returns the Neutral score

    



"""

lets say 'data' is a dataframe which contains a column 'commentText'
we can get the VADER scores for the sentences in the 'commentText' column as below:
   
data['score']=data['commentText'].map(lambda com:sentiment_scores(com))
data['positive']=data['commentText'].map(lambda com:positive_scores(com))
data['negative']=data['commentText'].map(lambda com:negative_scores(com))
data['neutral']=data['commentText'].map(lambda com:neutral_scores(com))

"""



"""
Examples to get insight of the sentiment 
scores for various sentences are as below
"""


temp = "study is going on as usual"
sentiment_scores(temp) 

temp = "donald is not a good pm"
sentiment_scores(temp)

temp = "he is just good"
sentiment_scores(temp)

temp = "he is good"
sentiment_scores(temp)