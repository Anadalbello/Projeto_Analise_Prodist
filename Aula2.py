import pandas as pd
import numpy as np
df = pd.read_excel('C:/CAMINHO_ONDE_FOI_SALVA_A_PLANILHA/planilha.xlsx')

Adequada = df.loc[(202 <= df['medicao']) & (df['medicao'] <= 231)]
Precaria = df.loc[(231 < df['medicao']) & (df['medicao'] <= 233)]
Critica = df.loc[(191 < df['medicao']) & (df['medicao'] > 233)]

coditions = [((202 <= df['medicao']) & (df['medicao'] <= 231)),
             ((231 < df['medicao']) & (df['medicao'] <= 233)),
             ((191 < df['medicao']) & (df['medicao'] > 233))]

choices = ['Adequada', 'Precaria', 'Critica']
df['TA'] = np.select(coditions, choices, default='Não definido')

df.to_excel('C:/Users/Anabe/Desktop/Ensino_dirigido/planilha.xlsx',index=False)
