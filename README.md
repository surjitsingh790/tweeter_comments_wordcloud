# tweeter_comments_wordcloud

# Word-Cloud-of-Tweets-Word
1. Introduction 
This assignment is based on social media analytics and here, we have done analyzing on Twitter tweets
using Twitter API. We have Twitter Developer Account and by using access token, access token secret, 
consumer api key and consumer api secret, fetch the tweets of Corona, ElonMusk, BillGates, and 
Rihanna. And collect the statistics of most common words in tweets and built the word cloud.
2. Data Collection Procedure 
The data collection process was done with Twitter API, where we have generated one Twitter API Key 
which is unique for every Twitter user. Here, we have Twitter Developer account, we have extracted 
the data and for this step tweepy library we used.

1. Introduction 
This assignment is based on social media analytics and here, we have done analyzing on Twitter tweets
using Twitter API. We have Twitter Developer Account and by using access token, access token secret, 
consumer api key and consumer api secret, fetch the tweets of Corona, ElonMusk, BillGates, and 
Rihanna. And collect the statistics of most common words in tweets and built the word cloud.
2. Data Collection Procedure 
The data collection process was done with Twitter API, where we have generated one Twitter API Key 
which is unique for every Twitter user. Here, we have Twitter Developer account, we have extracted 
the data and for this step tweepy library we used.
3. Data Cleansing Steps
This step is very important as the result will be dependent on this step because cleansing steps impact 
more on output. After data collection second task to cleansing the data and remove the unwanted 
characters like numbers, stopwords, and punctuation. After that LDA model apply on data for 
extracting topics.
Twitter API Crendentials
Create Authentication Object
Setup API
Extract Data
Save Data in CSV
4
Below is DataFrame view of stored data and remove the unwanted columns, Unnamed: 0.
4. Analysis Steps
This step is very important in our assignment as based on analysis only we can be able to reach our 
output and in the further steps we are going to see our output in both, statistical and graphical view. 
Here, after analysis steps only we can get the top-5 topics.
Read Saved CSV
Create DataFrame
Remove Unwanted Columns
Apply LDA
Extract Topics 
Word Cloud
5
5. Analysis Steps Using a bar diagram, showing the top-5 topics for any twitter handler of 
 your choice 
• Statistical View:
• Graphical View:
6. References 
• https://tweettopicexplorer.neoformix.com/#n=NYTimes
• https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python9bf156893c24
• https://github.com/c17hawke/flask-based-wordcloud-generato

![wordcloud](https://user-images.githubusercontent.com/54304418/170316403-11c49d45-9c58-42ad-bdff-c9f337cfc99b.jpg)
