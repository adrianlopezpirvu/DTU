import numpy as np

def linearLSQ(A, y):
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ y)