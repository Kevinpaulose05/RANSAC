import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  # A matrix for least-squares
  A = np.zeros((len(X1), 9))
  for i in range(len(X1)):
    A[i] = np.kron(X1[i], X2[i])
  
  # SVD on A
  U,S,V = np.linalg.svd(A)
  Vt = V.T
  
  E = Vt[:,-1]  # column 9 extraction
  E = E.reshape((3,3))
  E = E.T  # E-matrix

  
  U, S, Vt = np.linalg.svd(E)   # redecompose

  # construct the corrected essential matrix
  diag = np.array([1, 1, 0])
  E = U @ np.diag(diag) @ Vt

  """ END YOUR CODE
  """
  return E