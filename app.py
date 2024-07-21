import streamlit as st
from  preprocessing import preprocessing
import pandas as pd
import helperfile
import useranaly
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Analyzer!")
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8') #conver bytes into utf string
    df = preprocessing(data)

    

    #fetch the uniqe user
    user_data = df['User'].unique().tolist()
    user_data.sort()
    user_data.insert(0,"Overall" )
    selected_user = st.sidebar.selectbox("Showw Analyisi with specific User",user_data)

    if st.sidebar.button("Showw Analyais"):
        st.title("TOP STATISTIC")

        number_of_messages , words , media_word , links = helperfile.fetch_states(selected_user=selected_user , dataframe = df)

        col1 , col2 , col3   , col4 = st.columns(4)
        
        with col1:
            st.header("Total Meassages")
            st.title(number_of_messages)
    
        with col2:
            st.header("Total Wordss")
            st.title(words)

        with col3:
            st.header("Total Media")
            st.title(media_word)

        with col4:
            st.header("Total Links")
            st.title(links)
        
       


        #print(df)
 
        if selected_user == "Overall":
            
            st.header("Top Five  Most active Persons")
            plot , user_percen = helperfile.most_active(df = df)
            fig, ax = plt.subplots()
            #print(plot)
            col1 , col2 = st.columns(2)

            with col1:
                ax.bar(plot.index , plot.values )
                st.pyplot(fig=fig)

            with col2:
                #st.header("User Messages by %")
                st.dataframe(user_percen)
        else:
            pass
        
        #wordcloude
        st.header("Word Cloud")
        df_wc = helperfile.word_clod(df=df)
        fig , ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig=fig)


        #show the mostt comman namess 
        st.header("Most 20 Common Words")
        col1 , col2 = st.columns(2)
        most_common_df = helperfile.most_comman_words(selected_user=selected_user , df=df)
        
        fig , ax = plt.subplots()
        ax.barh(most_common_df[0] , most_common_df[1])
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig=fig)  


        st.title("MOST ACTIVE MONTHS")
        usertime = useranaly.useractive(selected_user=selected_user , df=df)
        fig , ax = plt.subplots()
        ax.plot(usertime['Month_year'] , usertime['User_messages'])
        plt.xticks(rotation = 'vertical'  )
        
        st.pyplot(fig=fig)