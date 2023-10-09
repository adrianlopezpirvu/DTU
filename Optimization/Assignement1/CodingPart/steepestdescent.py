import numpy as np

def steepestdescent(alpha,fundfun, x0, tol=1.0e-10, maxit=None, *args):
    # Solver settings and info
    maxit = maxit if maxit is not None else 100*len(x0)
    
    # Initialize
    stat = {"converged": False, "nfun": 0, "iter": 0, "X": [x0], "F": [], "dF": []}
    x = np.copy(x0)
    it = 0
    f, df, _ = fundfun(x, *args)
    converged = (np.linalg.norm(df, np.inf) <= tol)
    stat["nfun"] += 1
    
    # Store data for plotting
    stat["F"].append(f)
    stat["dF"].append(df)
    
    # Main loop of steepest descent
    while not converged and (it < maxit):
        it += 1
        
        p = - df / np.linalg.norm(df, 2)  
        x = x + alpha * p
        f, df, _ = fundfun(x, *args)
        converged = (np.linalg.norm(df, np.inf) <= tol)
        stat["nfun"] += 1
        
        # Store data for plotting
        stat["X"].append(np.copy(x))
        stat["F"].append(f)
        stat["dF"].append(df)
    
    # Prepare return data
    if not converged:
        x = [] 
    stat["converged"] = converged
    stat["iter"] = it
    
    return x, stat
