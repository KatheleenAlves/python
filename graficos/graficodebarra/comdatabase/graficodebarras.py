import pandas as pd
from IPython.display import display
import plotly.express as px

bancodedados = pd.read_excel(r"graficos\graficodebarra\comdatabase\bd.xlsx")

display(bancodedados)

grafico = px.bar(bancodedados, x="DESPESA", y="CUSTO", title="PONTO DE EQUILÍBRIO",  height=600, width=600)

grafico.show()