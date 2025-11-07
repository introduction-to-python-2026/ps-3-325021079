def approximate_pi(n_terms):
   
    phi = 0
    
    for i in range(n_terms) :
       phi += ((-1)**i) / ((2 * i) + 1)
    return (4 * phi)
