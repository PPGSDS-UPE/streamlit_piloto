import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Hello Streamlit")
st.write("Este é o meu primeiro aplicativo com Streamlit")

data = {
    'Nome': ['Pedro', 'Carlos', 'Augusto'],
    'Idade': [20, 19, 18],
    'Salario': [1000, 2000, 20000]
}

df = pd.DataFrame(data)
st.dataframe(df)

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salario'])
st.pyplot(fig)

st.title('Uber New York')
""""""
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Carregando dados...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)


@st.cache_data
def load_data(nrows):
    data_load_state.text("Feito!")

st.subheader('Dados')
st.write(data)

st.subheader('Número de coletas por hora')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Mapa de todos os pontos de coleta')
st.map(data)