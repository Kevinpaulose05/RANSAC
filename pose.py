import numpy as np

def pose_candidates_from_E(E):
    transform_candidates = []
    ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
    """ YOUR CODE HERE
    """
    # rotation matrices for 90 and -90 degrees about z-axis
    Rz_90 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    Rz_minus90 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
  
    U, S, Vt = np.linalg.svd(E)  # SVD of E matrix
    
    # translation candidates
    T1 = U[:, 2]
    T2 = -U[:, 2]
    
    # rotation candidates
    R1 = U @ Rz_90 @ Vt
    R2 = U @ Rz_minus90 @ Vt
  
    # create dictionaries for each candidate
    candidate1 = {"T": T1, "R": R1}
    candidate2 = {"T": T1, "R": R2}
    candidate3 = {"T": T2, "R": R1}
    candidate4 = {"T": T2, "R": R2}

    # Append candidates to the list
    transform_candidates.extend([candidate1, candidate2, candidate3, candidate4])

    """ END YOUR CODE
    """
    return transform_candidates