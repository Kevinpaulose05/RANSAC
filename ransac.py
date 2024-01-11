from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        # estimate E using the current random sample
        X1_sample = X1[sample_indices]
        X2_sample = X2[sample_indices]
        E = least_squares_estimation(X1_sample, X2_sample)
        
        e3 = np.array([0, 0, 1])

        #skew-symmetric matrix for [0,0,1]
        e3_prime = np.array([[0, -e3[2], e3[1]],
                             [e3[2], 0, -e3[0]],
                             [-e3[1], e3[0], 0]])

        # compute residuals for all points using E
        inliers_sample = []
        # inliers_sample = compute_residuals(E, e3_prime, X1_sample, X2_sample, test_indices, eps = 10**-4)

        for i in test_indices:
            # first epipolar constraint residual
            num1 = X2[i].T @ E @ X1[i]
            den1 = e3_prime @ E @ X1[i]
            residual_1 = (num1 ** 2) / ((np.linalg.norm(den1)) ** 2)
            
            # second epipolar constraint residual 
            num2 = X1[i].T @ E.T @ X2[i]
            den2 = e3_prime @ E.T @ X2[i]
            residual_2 = (num2 ** 2) / ((np.linalg.norm(den2)) ** 2)

            residuals = residual_1 + residual_2
            
            # check if the point is an inlier
            if residuals < eps:
                inliers_sample.append(i)
        
        # Convert the list of inliers to a numpy array and concatenate with the sample_indices
        inliers_sample = np.array(inliers_sample)
        inliers = np.concatenate((sample_indices, inliers_sample)).astype(int)

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers


    return best_E, best_inliers