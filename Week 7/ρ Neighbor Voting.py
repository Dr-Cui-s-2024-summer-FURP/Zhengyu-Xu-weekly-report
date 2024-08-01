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
