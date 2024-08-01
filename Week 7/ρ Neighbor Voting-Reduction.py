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
