import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly_express as px

st.header('Чаевые в ресторане  💁‍♀️')
st.write('#### Данные о посетителях в ресторане')

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
sea_tips = sns.load_dataset('tips')
st.dataframe(sea_tips)

st.write('#### Гистограмма размера счёта')
fig, ax = plt.subplots()
sns.histplot(data=sea_tips, x='total_bill')
st.pyplot(fig)

st.write('#### График, показывающий связь между размером счёта и чаевыми')
fig, ax = plt.subplots()
sns.scatterplot(data=sea_tips, x='total_bill', y='tip')
st.pyplot(fig)

st.write('#### График, связывающий размер счёта, чаевые и размер стола')
fig, ax = plt.subplots()
sns.scatterplot(data=sea_tips, x='total_bill', y='tip', hue="size", size='size', sizes=(20, 200))
st.pyplot(fig)

st.write('#### График, показывающий связь между днем недели и размером счета')
fig, ax = plt.subplots()
sns.barplot(data=sea_tips, x="day", y="total_bill", estimator=np.sum)
st.pyplot(fig)

st.write('#### График, показывающий связь между размером чаевых, днем недели и пола посетителя')
fig, ax = plt.subplots()
sns.scatterplot(data=sea_tips, x='tip', y='day', hue="sex")
st.pyplot(fig)

st.write('#### График, показывающий сумму всех счетов за каждый день и разбивающий по времени посещения (Обед/Ужин)')
fig, ax = plt.subplots()
sns.boxplot(data=sea_tips, x="total_bill", y="day", hue="time")
st.pyplot(fig)

st.write('#### График, показывающий размер чаевых на ужине и на обеде')
fig, ax = plt.subplots()
two1 = sns.FacetGrid(tips, col="time")
two1.map_dataframe(sns.histplot, 'tip')
st.pyplot(two1)

st.write('#### График, показывающий связь размера счета и чаевых, дополнительно разбивший по курящим/некурящим')
two2 = sns.FacetGrid(tips, col="sex", hue="smoker")
two2.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
st.pyplot(two2)
