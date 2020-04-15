import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import json

#for using the API library of IBM Watson designed tone analysis segment
from ibm_watson import ToneAnalyzerV3 
from watson_developer_cloud import ToneAnalyzerV3
from deepsegment import DeepSegment

#apikey that a user creates. This code is a by default segment
#that is used to use the service of IBM Watson by individual APIKEY
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='v1qLTU-4zIIN70V1b6q4YA9p8FcyTqX6SY_a1VGwYPCe',
    url='https://gateway-syd.watsonplatform.net/tone-analyzer/api'
   	)

#Example to show the working of the api
text = 'When bin laden was sending his videos and making his threats against the USA, the videos were being examined and medical experts said that he was getting weaker and if does not get medical treatment, will die very soon.'

#result
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))

#importing the generated dataset
df = pd.read_csv('comments-zb0LgL32rro.csv')

#removing the unwanted rows and columns
df.drop(['replies.id', 'replies.user', 'replies.date',
       'replies.timestamp', 'replies.commentText', 'replies.likes'], inplace=True, axis=1)
df.dropna(inplace = True)
df.info()

#The limitation of this API is that it can analyse only 50 comments at a time with a character count of 500 only.
#This loop is used in a way that can evaluate the comments automaticallly. it evaluates the comments in the chunk of 50 comments each.
#the (j<4) analyses 200 comments. Accordingly it can be set to value that analyses the entire dataset at once.
toneData = []
j=0
while(j<4):
    utterances = []
    for i in range(j*50,(j*50)+50):        
        utterances.append({
            "text": str(data_json.iloc[i,1]),
            "user": str(data_json.iloc[i,0])
         })
		      
    utterance_analyses = tone_analyzer.tone_chat(utterances).get_result()
    toneData.append(utterance_analyses)
    j=j+1

print(json.dumps(toneData, indent=2))
type(utterance_analyses)
type(toneData)

#the following snippet will select certain field from the utterance analyses will generate a dataframe
#that will contain the score, tone and comment id respectively.
temp = []
count = 0
for i in toneData:
    x=pd.DataFrame(i['utterances_tone'])
    for j,k in zip(x['utterance_id'], x['tones']):
        #print(j)
        #print(k)
        #break
        for l in k:
            l.update({'utterance_id': str(count)+'_'+str(j)})
            temp.append(l)
    count += 1

            
tone_df = pd.DataFrame(temp)
print(tone_df)

#dumping the result into csv
tone_df.to_csv('./tone_df.csv')