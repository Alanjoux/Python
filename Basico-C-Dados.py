import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
base = pd.read_csv('titanic_train.csv') # Importando o arquivo csv.

# Entendendo toda a base.

#print(base)
#print(base.head) 
#print(base.shape)
#print(base.dtypes) # Exibir os tipos de dados
#print(base.info()) # Mostrando os tipos de dados e valores vazios.
#print(base.isnull().sum()) # Contando os valores vazios por coluna.

# Tratando melhor os dados.

dados = {
    'X' : [1,2,3,4,5,6,7,8,9,10,11]
}
dados = pd.DataFrame(dados)
print(dados.mean()) # Mostrando a Média.
print(dados.count()) # Mostrando a quantidade de registro.
print(dados.median()) # Mediana.
print(dados.std()) # Desvio padrão.
print(dados.describe()) # Trazendo todo o resumo estatístico utilizando o describe.
print(base.describe()) # Trazendo o resumo estatístico para a base.
print(base.nunique()) # Verificando o número de valores únicos.

# Verificando histogramas.

# Verificando o histograma das tarifas
x = base.Fare

fig, ax = plt.subplots()

ax.hist(x, bins=40, linewidth=0.5, edgecolor="white")

plt.show() 

# Verificando o histograma das tarifas apenas para tarifas menores que 100.
x = base[base.Fare < 100].Fare

fig, ax = plt.subplots()

ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

plt.show() 

# Verificando o boxplot para coluna Fare
x = base[base.Fare < 100].Fare

fig, ax = plt.subplots()

ax.boxplot(x)

plt.show()

# Criando o pairplot

sns.pairplot(base,hue='Survived')