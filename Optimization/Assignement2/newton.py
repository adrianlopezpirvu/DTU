import numpy as np

def newton_1d(alpha, fundfun, x0, varargin):
    # Solver settings and info
    maxit = 100
    tol = 1.0e-10

    # Initial iteration
    x = x0
    it = 0
    f, df, d2f = fundfun(x, varargin)
    converged = (np.abs(df) <= tol)

    # Store data for plotting
    stat = {'X': [x], 'F': [f], 'dF': [df], 'converged': converged, 'nfun': 1, 'iter': it}

    # Main loop of Newton's method
    while not converged and (it < maxit):
        it += 1

        p = - df / d2f
        x = x + alpha * p

        f, df, d2f = fundfun(x, varargin)
        converged = (np.abs(df) <= tol)
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


def newton_md(alpha, fun_rJ_exe, x0, *varargin):

    # Solver settings and info
    maxit = 1000 * len(x0)
    tol = 1.0e-10

    # Initial iteration
    x = x0
    it = 0
    r, J = fun_rJ_exe(x)
    converged = (np.linalg.norm(r, np.inf) <= tol)

    # Store data for plotting
    stat = {'X': [x], 'R': [r], 'J': [J], 'converged': converged, 'nfun': 1, 'iter': it}

    # Main loop of Newton's method
    while not converged and (it < maxit):
        it += 1

        p = - np.linalg.solve(J, r)
        x = x + alpha * p

        r, J = fun_rJ_exe(x)
        converged = (np.linalg.norm(r, np.inf) <= tol)
        stat['nfun'] += 1

        # Store data for plotting
        stat['X'].append(x)
        stat['R'].append(r)
        stat['J'].append(J)

    # Prepare return data
    if not converged:
        x = None
    stat['converged'] = converged
    stat['iter'] = it

    return x, stat

