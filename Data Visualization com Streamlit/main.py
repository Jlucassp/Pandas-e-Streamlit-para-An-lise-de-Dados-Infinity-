import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Minha primeira página :alien:") # st.write("<h1><center>Minha primeira página 👽</center></h1>", unsafe_allow_html=True)

# st.write("""
#     Hello world
# """)

# st.write("""
#     # Hello *world* :sunglasses:
# """)

# df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")
# df

# st.dataframe(df) # st.write(df)

# df = pd.DataFrame({
#     "Pessoa": ["Fulano", "Ciclano", "Deltrano"],
#     "Forma de contato": ["Email", "Outros", "Telefone"]
# })

# st.write(df)

# escolha = st.selectbox("Qual a linguagem você quer selecionar?", pd.unique(df["Linguagem"]))

# click = st.button("Clique em mim")

# if click:
#     df_filtrado = df.loc[df["Linguagem"] == escolha]
#     st.dataframe(df_filtrado)

arquivo = st.file_uploader("Clique aqui para selecionar o seu arquivo", type=["csv"])

if arquivo:
    if "csv" in arquivo.type:
        data = pd.read_csv(arquivo)
        st.write(data)

escolha = st.selectbox("Qual linguagem você quer selecionar?", pd.unique(data["Linguagem"]))

click = st.button("Clique em mim")

if click:
    df_filtrado = data.loc[data["Linguagem"] == escolha]
    st.dataframe(df_filtrado)

# foto = st.file_uploader("Escolha o arquivo") # accept_multitle_files=True

# if foto:
#     if "png" in foto.type:
#         st.image(foto)

st.bar_chart(data, x="Linguagem", y="Desenvolvedores")
st.bar_chart(data, x="Popularidade", y="Desenvolvedores")
st.scatter_chart(data, x="Linguagem", y="Desenvolvedores")
px.bar(data, x="Linguagem", y="Desenvolvedores")
px.bar(data, x="Popularidade", y="Desenvolvedores")
px.scatter(data, x="Linguagem", y="Desenvolvedores")