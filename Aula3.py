import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
df = pd.read_excel('C:/CAMINHO_ONDE_FOI_SALVA_A_PLANILHA/planilha.xlsx', sheet_name='Sheet1')
#Alterar o caminho no codigo acima para o diretorio onde foi salva em sua maquina
plt.hist(df["TA"], bins=5 )
plt.show()
