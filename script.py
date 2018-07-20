import numpy as n
import matplotlib.pyplot as plt

#blah = input("what's up")
#print(blah)

X = n.linspace(-n.pi, 2*n.pi, 256, endpoint=True)
C,S,K = n.sin(3*X), n.exp(-X/3)*n.sin(3*X), 2**(X/2)-3

plt.plot(X,C)
plt.plot(X,S)
plt.plot(X,K)

plt.gcf() # Get current figure

plt.show()
