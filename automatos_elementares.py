import numpy as np
import matplotlib.pyplot as plt

"""Projeto de criação de autômatos celulares elemetares"""

regra = int(input("Escolha qual regra aplicar: "))
regra = np.binary_repr(regra,8)
lista_regra = [int(i) for i in regra]


passos = input("digite quantos passos o autômato deve evoluir ")
passos = int(passos)
tam_gen = 200
matriz = np.zeros((passos,tam_gen),dtype=np.int0)

matriz[0][(tam_gen//2) + 1] = 1


for i in range(passos -1):
    for j in range(tam_gen):
        
        if(matriz[i][j-1] == 1 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = lista_regra[0]
            

        elif(matriz[i][j-1] == 1 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = lista_regra[1]
            

        elif(matriz[i][j-1] == 1 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = lista_regra[2]
         

        elif(matriz[i][j-1] == 1 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = lista_regra[3]
        

        elif(matriz[i][j-1] == 0 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = lista_regra[4]
           

        elif(matriz[i][j-1] == 0 and matriz[i][j]==1 and matriz[i][(j+1) % len(matriz[i])] == 0):
            matriz[i+1][j] = lista_regra[5]
            

        elif(matriz[i][j-1] == 0 and matriz[i][j]==0 and matriz[i][(j+1) % len(matriz[i])] == 1):
            matriz[i+1][j] = lista_regra[6]
            
        else:
            matriz[i+1][j] = lista_regra[7]


    plt.imshow(matriz, cmap='Greys')
    plt.pause(0.001)
plt.show()