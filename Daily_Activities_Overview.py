import streamlit as st
import pandas as pd

def spl (a):
    return a.split(' ')[1]

st.title('Daily Activities Overview')
cola, colb = st.columns([0.5,0.5])
date_ = colb.date_input('Date')

df = pd.read_csv('activities.csv')
# df['Counter'] = df['Counter'] - 1820

def act(activities,df,con):
    df = df[df['Activity'].isin(activities)]
    con.scatter_chart(df,x='Time',y='Place',x_label='Time',color='Activity',height=300)
con = st.container()
activities = st.multiselect('Select the actvities you want to see on the graph',options=['Sitting', 'Standing','Walking', 'Laying'],default=['Sitting', 'Standing','Walking', 'Laying'])
act(activities,df,con)