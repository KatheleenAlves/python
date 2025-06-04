import numpy as np
import matplotlib.pyplot as plt 

dados = {'jan':120, 'fev':300,'mar':100,'abr':300, 'mai':150, 'jun':500}
meses = list(dados.keys())
faturamento = list(dados.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(meses, faturamento, color ='darkblue', width = 0.8)
 
plt.xlabel("Meses")
plt.ylabel("Faturamento em milhões")
plt.title("RESULTADO DO 1º SEMESTRE")
plt.show()