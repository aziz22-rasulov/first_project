import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborClassifier
import category_encoders as ce
import plotly.express as px

st.set_page_config(page_title='ff', layout='wide')
st.title('🎈 App Name')

st.write('Работа с датасетом Пингвинов')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
