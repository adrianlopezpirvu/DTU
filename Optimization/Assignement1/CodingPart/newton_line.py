def newton_line_md(alpha, fundfun, x0, rho=0.5, c=0.1, *varargin):
    import numpy as np

    # Solver settings and info
    maxit = 100 * len(x0)
    tol = 1.0e-10

    # Initial iteration
    x = x0
    it = 0
    f, df, d2f = fundfun(x, *varargin)
    converged = (np.linalg.norm(df, np.inf) <= tol)

    # Store data for plotting
    stat = {'X': [x], 'F': [f], 'dF': [df], 'converged': converged, 'nfun': 1, 'iter': it}

    # Main loop of Newton's method
    while not converged and (it < maxit):
        it += 1

        p = - np.linalg.solve(d2f, df)
        # backtracking line search
        alpha = 1
        fnew, _, _ = fundfun(x + alpha * p, *varargin)
        while fnew > (f + c * alpha * np.dot(df.T, p)):
            alpha = rho * alpha
            fnew, _, _ = fundfun(x + alpha * p, *varargin)
        stat["alpha"].append(alpha)
        x = x + alpha * p

        f, df, d2f = fundfun(x, *varargin)
        converged = (np.linalg.norm(df, np.inf) <= tol)
        stat['nfun'] += 1

        # Store data for plotting
        stat['X'].append(x)
        stat['F'].append(f)
        stat['dF'].append(df)

    # Prepare return data
    if not converged:
        x = None
    stat['converged'] = converged
    stat['iter'] = it

    return x, stat
