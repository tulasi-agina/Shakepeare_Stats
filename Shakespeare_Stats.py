import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
# from wordcloud import WordCloud, STOPWORDS
import glob, nltk, os, re
from nltk.corpus import stopwords 
import nltk
nltk.download('punkt')
import string
nltk.download('stopwords')

# Create a dictionary (not a list)
books = {" ":" ","A Mid Summer Night's Dream":"data/summer.txt","The Merchant of Venice":"data/merchant.txt","Romeo and Juliet":"data/romeo.txt"}

## Select text files
image = st.selectbox("Choose a text file", books.keys())

## Get the value
image = books.get(image)
tab1, tab2, tab3 = st.tabs(['Word Cloud', 'Bar Chart', 'View Text'])

if image != " ":
    stop_words = []
    raw_text = open(image,"r").read().lower()
    nltk_stop_words = stopwords.words('english')
    
    stop_words = set(nltk_stop_words)
    tokens = nltk.word_tokenize(raw_text)
    
    with tab2:
            st.subheader("Bar Chart")
            # Tokenization without punctuation and tokens starting with an apostrophe
            tokens = [word for word in nltk.word_tokenize(raw_text) if word not in string.punctuation and not word.startswith("'")]

            # Remove stopwords from the tokens if the checkbox is unchecked
            stop_words = set(nltk_stop_words)
            tokens = [word for word in tokens if word.lower() not in stop_words]

            # Calculate word frequencies
            word_frequencies = nltk.FreqDist(tokens)

            # Filter the words based on the minimum count specified in the sidebar
            filtered_word_frequencies = {word: count for word, count in word_frequencies.items() if count >= min_countwords}

            # Create a dataframe from the filtered word frequencies
            word_freq_df = pd.DataFrame(list(filtered_word_frequencies.items()), columns=['word', 'count'])

            # Create a bar chart using Altair
            bar_chart = alt.Chart(word_freq_df).mark_bar().encode(
                y=alt.Y('word:N', sort=None, title='Word'),
                x=alt.X('count:Q', title='Count'),
                text=alt.Text('count:Q')
            ).properties()

            # Create a text layer to display the count above each bar
            text_layer = alt.Chart(word_freq_df).mark_text(align='left', baseline='bottom', dy=5).encode(
                y=alt.Y('word:N', sort='-x'),
                x=alt.X('count:Q'),
                text=alt.Text('count:Q')
            )

            # Combine the bar chart and the text layer
            combined_chart = bar_chart + text_layer

            st.altair_chart(combined_chart, use_container_width=True)
