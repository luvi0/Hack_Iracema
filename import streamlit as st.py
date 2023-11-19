import streamlit as st

st.title('Visir 4TAL')
st.sidebar.title('Menu')

import pandas as pd
import matplotlib.pyplot as plt
d_uber = pd.read_csv('uber_fortaleza.csv')
X = df_uber.iloc[:, 4] #preços
Y = df_uber.iloc[:, 5] #hora
plt.scatter(X, Y)
plt.show()
