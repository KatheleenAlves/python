import plotly.express as px

meses = ['jan', 'fev','mar','abr', 'mai', 'jun']
faturamento = [120, 100, 80, 300, 150, 220]

grafico=px.pie(names=meses, values=faturamento, title="Faturamento da empresa em milhões", height=400, width=400)

grafico.show()