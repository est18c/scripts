import matplotlib.pyplot as plt
import numpy as n

R1 = 6;
R2 = 2;
dt = 0.001;
N = 1000;
A = n.zeros(N);
A[0] = 1;
B = n.zeros(N);
B[0] = 0.8;
C = n.zeros(N);
C[0] = 0;

t = n.linspace(1,N,N);

for i in range(1,N):
    A[i] = A[i-1] - A[i-1]*B[i-1]*dt*R1 + C[i-1]*dt*R2;
    B[i] = B[i-1] - A[i-1]*B[i-1]*dt*R1 + C[i-1]*dt*R2;
    C[i] = C[i-1] + A[i-1]*B[i-1]*dt*R1 - C[i-1]*dt*R2;

plt.plot(t,A)
plt.plot(t,B)
plt.plot(t,C)
plt.show()
