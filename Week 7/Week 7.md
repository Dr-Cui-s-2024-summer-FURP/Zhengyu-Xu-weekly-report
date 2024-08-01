# WEEK 7
Reproduce ScatterHough
## $\rho$ Neighbor Voting
def rho_neighbor_voting(A, d):

    A_prime = np.zeros_like(A)  
    
    for rho in range(A.shape[0]): 
    
        for theta in range(A.shape[1]):  
            if A[rho, theta] > 0:  
                sum_votes = 0  
                for n in range(-d, d + 1):  
                    rho_prime = rho + n  
                    if 0 <= rho_prime < A.shape[0]:  
                        sum_votes += A[rho_prime, theta]  
                A_prime[rho, theta] = sum_votes  
    return A_prime  

## $\rho$ Neighbor Voting-Reduction
def rho_neighbor_vote_reduction(A, d, threshold):

    lines = []  
    while True:
        max_votes = np.max(A)  
        if max_votes < threshold:  
            break
        rho, theta = np.unravel_index(np.argmax(A), A.shape)  
        lines.append((rho, theta))  
        for x in range(A.shape[0]):
            for y in range(A.shape[1]):                
                if abs(x * np.cos(theta) + y * np.sin(theta) - rho) < d:
                    A[x, y] = 0
    return lines 
# Problem
1.Unable to obtain pandaset dataset.
2.If increasing the threshold can increase the accuracy of line judgment, why is the threshold in the paper only 4 instead of larger?
3.ρ Neighbor Vote-Reduction removes points around detected lines. Suppose there are lines A and B that are close and both important, and I delete the points around A after detecting A, will this affect my subsequent calculation of votes around B?

