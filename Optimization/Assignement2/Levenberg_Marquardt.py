import numpy as np

def Levenberg_Marquardt(fun_rJ, x0, *args):

    def linearLSQ(A, y):
        Q, R = np.linalg.qr(A, mode='reduced')
        x = np.linalg.solve(R, np.dot(Q.T, y))
    
        return x

    # Solver settings and info
    maxit = 100 * len(x0)
    tol = 1.0e-10


    # Initial iteration
    x = np.array(x0)
    it = 0
    rx, Jx = fun_rJ(x, *args)
    f = 0.5 * np.linalg.norm(rx)**2
    df = np.dot(Jx.T, rx)
    converged = (np.linalg.norm(df, np.inf) <= tol)
    nfun = 1

    # Initial lambda
    lambda_val = np.linalg.norm(np.dot(Jx.T, Jx))

    # Store data for plotting
    X = [x]
    F = [f]
    dF = [df]

    # Main loop of L-M method
    while not converged and it < maxit:
        it += 1
        
        # Calculate the search direction by solving a linear LSQ problem
        A = np.vstack([Jx, np.sqrt(lambda_val)*np.eye(len(x))])
        b = np.hstack([-rx, np.zeros_like(x)])
        #p = np.linalg.lstsq(A, b, rcond=None)[0]
        p = linearLSQ(A, b)
        
        # Update the iterate, Jacobian, residual, f, df
        x_new = x + p
        rx_new, Jx_new = fun_rJ(x_new, *args)
        f_new = 0.5 * np.linalg.norm(rx_new)**2

        rho = (f - f_new) / (0.5 * np.dot(p, (lambda_val * p - np.dot(Jx.T, rx))))
        if rho > 0.75:
            lambda_val /= 3
        elif rho < 0.25:
            lambda_val *= 2
        
        # Accept or reject x_new
        if rho > 0:
            x = x_new
            rx = rx_new
            f = f_new
            Jx = Jx_new
            df = np.dot(Jx.T, rx)

        converged = (np.linalg.norm(df, np.inf) <= tol)
        nfun += 1

        # Store data for plotting
        X.append(x)
        F.append(f)
        dF.append(df)

    # Prepare return data
    if not converged:
        x = None  # Use None instead of empty for Python

    stat = {
        "converged": converged,
        "iter": it,
        "X": np.array(X),
        "F": np.array(F),
        "dF": np.array(dF),
        "nfun": nfun
    }
    
    return x, stat