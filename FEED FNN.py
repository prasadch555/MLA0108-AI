import numpy as np

sig = lambda x: 1/(1+np.exp(-x))

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

W1 = np.random.randn(2,2)
W2 = np.random.randn(2,1)

h = sig(X @ W1)
out = sig(h @ W2)

print(out)
