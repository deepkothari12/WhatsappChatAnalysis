from urlextract import URLExtract
import string as str
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from collections import Counter


Extract = URLExtract()

def fetch_states(selected_user , dataframe):
    if selected_user == "Overall":
        num_messages = dataframe.shape[0] 
        word = []
        for i in dataframe['User_messages']:
            word.extend(i.split())
        
        #count the mediaa
        mediaa_message = dataframe[dataframe['User_messages'] == "<Media omitted>\n"].shape[0]

        #fetch the number of links 
        links = []
        for message in dataframe['User_messages']:
            links.extend(Extract.find_urls(message))
        
        
        
        return  num_messages , len(word) , mediaa_message , len(links)
    
    else:
        word = []
        new_df = dataframe[dataframe['User'] == selected_user]
        specific_user_mesaages = dataframe[dataframe['User'] == selected_user].shape[0]  #maskinggg
        
        for i in dataframe[dataframe['User'] == selected_user]['User_messages']:
            word.extend(i.split())
        #print(word)

        #count the mediaa
        mediaa_message = dataframe[(dataframe['User'] == selected_user) & (dataframe['User_messages'] == "<Media omitted>\n")]
        
        #fetch link from apecific person
        links = dataframe[(dataframe['User'] == selected_user) & (dataframe['User_messages'].str.startswith("https:"))]['User_messages']
        
        return specific_user_mesaages , len(word) , len(mediaa_message) , len(links) 
    
def most_active(df):
     
     x = df['User'].value_counts().head()
     user_percen = ((df['User'].value_counts() / df.shape[0])*100).reset_index().rename(columns = {'count' : "Percentages"})

     return x , user_percen

def word_clod( df): 
    #word cloude 
    wc = WordCloud(width=500 , height=500 , min_font_size=10 , background_color='white')
    df_wc = wc.generate(df['User_messages'].str.cat(sep=" "))
    #plt.imshow(df_wc)
    return df_wc
    


def most_comman_words(selected_user , df):
     #now i used stop_hinglish file for remove the stops word like "the" , "i" etc...
     if selected_user == "Overall":
        f = open('stop_hinglish.txt' , 'r')
        stop_words = f.read()
        #print(stop_words)
        temp = df[df['User'] != "Group Notification"]
        temp = temp[temp['User_messages'] != "<Media omitted>\n"]
        #temp

        words = []

        for i in temp['User_messages']:
            for word in i.lower().split(): #split-> split word by word if we dont used then they do charchert charachter 
                if word not in stop_words:
                    words.append(word)

        
        return_df =  pd.DataFrame(Counter(words).most_common(20)) 
        
        return return_df
     else:
            
            new_df = df[df['User'] == selected_user]
            f = open('stop_hinglish.txt' , 'r')
            stop_words = f.read()
            #print(stop_words)
            temp = new_df[new_df['User'] != "Group Notification"]
            temp = temp[temp['User_messages'] != "<Media omitted>\n"]
            #temp

            words = []
            for i in temp['User_messages']:
                for word in i.lower().split(): #split-> split word by word if we dont used then they do charchert charachter 
                    if word not in stop_words:
                        words.append(word)

            
            return_df =  pd.DataFrame(Counter(words).most_common(30)) 
            
            return return_df



