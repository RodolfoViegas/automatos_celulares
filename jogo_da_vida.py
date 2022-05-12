"""Jogo da Vida"""


import numpy as np
import matplotlib.pyplot as plt

passos = int(input("Quantidade de passos para o autômato evoluir: "))
individuos = int(input("Quantidade inicial de indivíduos em tela: "))

tam_matriz = passos*2

# Matriz para evolução
grid = np.zeros((tam_matriz,tam_matriz))

#Popula a matriz com celulas vivas alocadas de modo aleatório
for i in range(individuos):
    linha = np.random.randint(low=0,high=(passos*2)-1)
    coluna = np.random.randint(low=0,high=(passos*2)-1)
    grid[linha][coluna] = 1



# A regra de atualização da celula está quase pronta,falta ainda testar um modo de
for k in range(passos): 
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            if (grid[i][j]==0 and (grid[i][j-1] + grid[i][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j] + grid[i-1][j] + grid[(i+1) % len(grid[i])][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j-1] + grid[i-1][j-1] + grid[i-1][(j+1) % len(grid[i])] == 3)):
                grid[i][j] = 1
            elif (grid[i][j]==1 and ((grid[i][j-1] + grid[i][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j] + grid[i-1][j] + grid[(i+1) % len(grid[i])][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j-1] + grid[i-1][j-1] + grid[i-1][(j+1) % len(grid[i])] == 2) or 
            (grid[i][j-1] + grid[i][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j] + grid[i-1][j] + grid[(i+1) % len(grid[i])][(j+1) % len(grid[i])] + grid[(i+1) % len(grid[i])][j-1] + grid[i-1][j-1] + grid[i-1][(j+1) % len(grid[i])] == 3))):
                grid[i][j] = 1

            else:
                grid[i][j] = 0
    plt.imshow(grid, cmap='Greys')
    plt.pause(0.0001)
plt.show()
