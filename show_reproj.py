import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  """ YOUR CODE HERE
  """
  # K_inv = np.linalg.inv(K)
  # uncalibrated_1 = K_inv @ uncalibrated_1
  # uncalibrated_2 = K_inv @ uncalibrated_2
  
  T = T.reshape(3,1)
  
  """ Camera 1 to 2 (World coordinates to Image coordinates in Camera 2):
  """
  # World to Camera (3D to 3D):
  # Rotate P1 using R
  P1proj = (R @ P1.T)
  # Translate it by T
  P1proj = P1proj + T
  # Camera to Image C1 (3D to 2D):
  P1proj = K @ P1proj
  P1proj = P1proj.T
  
  """ Camera 2 to 1 (World coordinates to Image coordinates in Camera 1):
  """
  # World to Camera (3D to 3D):
  # Rotate P2 using R.T
  P2proj = (R.T @ P2.T)
  # Translation by -R.T @ T 
  P2proj = P2proj - (R.T @ T)
  # Camera to Image C2 (3D to 2D):
  P2proj = K @ P2proj
  P2proj = P2proj.T
  
  """ END YOUR CODE
  """

  if (plot):
    plt.figure(figsize=(6.4*3, 4.8*3))
    ax = plt.subplot(1, 2, 1)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image1[:, :, ::-1])
    plt.plot(P2proj[:, 0] / P2proj[:, 2],
           P2proj[:, 1] / P2proj[:, 2], 'bs')
    plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

    ax = plt.subplot(1, 2, 2)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image2[:, :, ::-1])
    plt.plot(P1proj[:, 0] / P1proj[:, 2],
           P1proj[:, 1] / P1proj[:, 2], 'bs')
    plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')
    
  else:
    return P1proj, P2proj