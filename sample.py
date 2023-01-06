from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

This webpage shows you an interesting set of mutliple choice questions generated through NLP on your favourite topics.
We hope it would be interesting :)
Please take a look.
"""

"""
MCQ generated on the iconic Hollywood Movie "The God Father":

"""

data1 = pd.read_csv('Godfather_MCQ.csv')

    
#"""
#st.altair_chart(alt.Chart(pd.DataFrame(data1), height=500, width=500)
 #   .mark_circle(color='#0068c9', opacity=0.5)
  #  .encode(x='x:Q', y='y:Q'))
#"""

st.dataframe(data1)

"""
Hope this one is interesting!!!

Take a look at another set of MCQ generated on the Maratha King Chatrapathi Shivaji"
"""

data2 = pd.read_csv('MCQ.csv')


st.dataframe(data2)

"""
We hope you enjoyed seeing this output played as part of MCQ Demo

"""
