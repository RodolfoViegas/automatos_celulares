import numpy as np
import matplotlib.pyplot as plt

"""Projeto de criação de autômatos celulares elemetares"""

passos = input("digite quantos passos o autômato deve evoluir ")
passos = int(passos)

matriz = np.zeros((passos,105),dtype=np.int0)

matriz[0][53] = 1


for i in range(passos -1):
    for j in range(105):
        #print((j-1),j,(j+1) % len(matriz[i]))
        if(matriz[i][j-1] == 1 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = 0
            #print(matriz[i+1][j])

        elif(matriz[i][j-1] == 1 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = 0
            #print(matriz[i+1][j])

        elif(matriz[i][j-1] == 1 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = 0
         #   print(matriz[i+1][j])

        elif(matriz[i][j-1] == 1 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = 1
          #  print(matriz[i+1][j])

        elif(matriz[i][j-1] == 0 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = 1
           # print(matriz[i+1][j])

        elif(matriz[i][j-1] == 0 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = 1
            #print(matriz[i+1][j])

        elif(matriz[i][j-1] == 0 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = 1
            #print(matriz[i+1][j])
        else:
            matriz[i+1][j] = 0

print(matriz)
plt.imshow(matriz, cmap='gray')
plt.show()