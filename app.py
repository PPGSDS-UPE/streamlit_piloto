import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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



