### IMPORTANTE ###
# Para rodar o código, no terminal vá até o diretório onde se encontra a pasta scripts e posteriormente digite "python 3d_reconstruction.py"

# -*- coding: utf-8 -*-

# Bibliotecas utilizadas
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy.linalg import inv
from numpy.linalg import pinv
import sys

# Caminho completo dos arquivos, substituindo os parâmetros de entrada
# Altere os caminhos conforme necessário
path = r"C:\Users\mfmdo\OneDrive\Documentos\Tarefas - Biomecânica\Tarefa 2\tarefa 2\data\\"

# Definindo os parâmetros das câmeras do experimento
resolutionx = int(720 / 2)  # Arrumar a translação X do sist. ref do kinovea 0.9.4
resolutiony = int(220 / 2)  # Arrumar a translação Y do sist. ref do kinovea 0.9.4
freq = 120  # Frequência de amostragem

# Carregando os arquivos das câmeras do Kinovea
# Camera 1
bola1 = pd.read_csv(path + 'c1.txt', sep=r'\s+', header=None, decimal='.')
bola1[1] = bola1[1] - -resolutionx
bola1[2] = -1 * (bola1[2] - resolutiony)
bola1 = np.asarray(bola1[[1, 2]])
bola1b = bola1

# Camera 2
bola2 = pd.read_csv(path + 'c2.txt', sep=r'\s+', header=None, decimal='.')
bola2[1] = bola2[1] - -resolutionx
bola2[2] = -1 * (bola2[2] - resolutiony)
bola2 = np.asarray(bola2[[1, 2]])
bola2b = bola2

# Identificação de impacto
idx = np.asarray(list(range(len(bola1b))))
diffball = abs(np.diff(bola1b[:, 0])) > 5
diffball = np.insert(diffball, 0, False)
phitball = idx[diffball][0]
idxcimpact = idx[phitball - 2:phitball + 1]

print(f'Frame of impact = {phitball}')
print(f'Critical impact frames  = {idxcimpact}')

# Visualização
plt.subplot(2, 1, 1)
plt.grid(True)
plt.plot(bola1[:, 0], bola1[:, 1], 'o')
plt.xlabel('CAM 1 - Coordinate X')
plt.ylabel('CAM 1 - Coordinate Y')
resx = 2 * resolutionx
resy = 2 * resolutiony
plt.title(f'Pixels coordinates (resolution = {resx} X {resy})')

plt.subplot(2, 1, 2)
plt.plot(bola2[:, 0], bola2[:, 1], 'o')
plt.xlabel('CAM 2 - Coordinate X')
plt.ylabel('CAM 2 - Coordinate Y')
plt.grid(True)

# Carregar arquivos de calibração
datcal_c1 = np.asarray(pd.read_csv(path + 'c1cal.txt', sep=r'\s+', header=None))
datcal_c1[:, 0] = datcal_c1[:, 0] - -resolutionx
datcal_c1[:, 1] = -1 * (datcal_c1[:, 1] - resolutiony)

datcal_c2 = np.asarray(pd.read_csv(path + 'c2cal.txt', sep=r'\s+', header=None))
datcal_c2[:, 0] = datcal_c2[:, 0] - -resolutionx
datcal_c2[:, 1] = -1 * (datcal_c2[:, 1] - resolutiony)

# Referência
ref = np.asarray(pd.read_csv(path + 'calibrador_ref.txt', sep=r'\s+', header=None))
ref = ref[:, 1:]

print("Pronto para exibir o gráfico...")

# Exibir o gráfico
plt.show()  

print("Gráfico exibido (se o código chegar até aqui).")  # Confirma que chegou até a parte de visualização


