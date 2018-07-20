import matplotlib.pyplot as plt
import numpy as n

N = 100
A = n.zeros(N,N,3)
pc = 0.6

#filling the matrix with green "trees"
for i in range(1:N):
    for j in range(1:N):
        if rand < pc:
            A[i,j,2] = 255;


#insert tree to BURN
A[50,50,1] = 255

#while loop to burn trees while fire == true
flame = 1

while flame > 0:
    flame = 0
    for i in range(1:N):
        for j in range(1:N):
            # if block is on fire make block brown [128,128,0]
            if A[i,j,1] == 255:
                A[i,j,1] = 128
                A[i,j,2] = 128

    #look for neighbors
    for i in range(1:N):
        for j in range(1:N):
            # if the block is brown
            if A[i,j,1] == 128:
                #making sure we are in the "frame" limits
                if i > 1 && i < N && j > 1 && j < N:
                    #going through k = -1 to k = 1
                    for k = -1:2:1:
                        #going through 'i' neighbors
                        if A[i+k,j,2] == 255
                            #setting block to red by [255,0,0]
                            A(i+k,j,2) = 0;
                            A(i+k,j,1) = 255;
                            flame = 1;

                        #going through 'j' neighbors
                        if A[i,j+k,2] == 255:
                            #setting block to red by [255,0,0]
                            A[i,j+k,2] = 0;
                            A[i,j+k,1] = 255;
                            flame = 1;

    plt.image(A)
    plt.gcf()
    plt.show()

    if flame == 0:
        break
