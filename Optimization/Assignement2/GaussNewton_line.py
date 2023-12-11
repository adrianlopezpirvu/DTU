import numpy as np


def GaussNewton_line_md(fun_rJ, x0, flag_line, *args):
    def linearLSQ(A, y):
        Q, R = np.linalg.qr(A, mode='reduced')
        x = np.linalg.solve(R, np.dot(Q.T, y))
        
        return x
    
    # Solver settings and info
    if type(x0) == float:
        maxit = 100
    else:
        maxit = 100*len(x0)
        
    #print(maxit)

    tol = 1.0e-10
    
    # Parameters for backtracking line search
    rho = 0.5  
    c = 0.1

    # Initial iteration
    if type(x0) == float:
        x = x0
    else:
        x = np.array(x0)
    #x = x0
    #x = np.array(x0)
    it = 0
    rx, Jx = fun_rJ(x, *args)
    f = 0.5 * np.linalg.norm(rx)**2
    #df = np.dot(Jx.T, rx)
    df = Jx.T @ rx
    converged = (np.linalg.norm(df, np.inf) <= tol)
    nfun = 1

    # Store data for plotting
    X = [x]
    F = [f]
    dF = [df]
    alpha_values = []

    # Main loop of Gauss-Newton
    while not converged and it < maxit:
        it += 1
        
        # Calculate the search direction by solving a linear LSQ problem
        #p = linearLSQ(Jx, -rx)[0,...]
        p = linearLSQ(Jx, -rx)

        if flag_line == 1:
            # Backtracking line search
            alpha = 1
            x_new = x + alpha * p
            rx_new, _ = fun_rJ(x_new, *args)
            f_new = 0.5 * np.linalg.norm(rx_new)**2

            while f_new > (f + c * alpha * np.dot(df, p)):
                alpha *= rho
                x_new = x + alpha * p
                rx_new, _ = fun_rJ(x_new, *args)
                f_new = 0.5 * np.linalg.norm(rx_new)**2    
            alpha_values.append(alpha)
        else:
            # Fixed alpha
            alpha = 1
        
        # Update the iterate, Jacobian, residual, f, df
        x = x + alpha * p
        rx, Jx = fun_rJ(x, *args)
        f = 0.5 * np.linalg.norm(rx)**2
        df = np.dot(Jx.T, rx)
        #df = Jx.T @ rx
        converged = (np.linalg.norm(df, np.inf) <= tol)
        nfun += 1

        # Store data for plotting
        X.append(x)
        F.append(f)
        dF.append(df)

    # Prepare return data
    stat = {
        "converged": converged,
        "iter": it,
        "X": np.array(X),
        "F": np.array(F),
        "dF": np.array(dF),
        "alpha": np.array(alpha_values),
        "nfun": nfun
    }
    
    return x, stat

def GaussNewton_line_1d(fun_rJ, x0, flag_line, *args):
    def linearLSQ(A, y):
        Q, R = np.linalg.qr(A, mode='reduced')
        x = np.linalg.solve(R, np.dot(Q.T, y))
        
        return x
    
    # Solver settings and info
    maxit = 100
    tol = 1.0e-10
    
    # Parameters for backtracking line search
    rho = 0.5  
    c = 0.1

    # Initial iteration
    x = x0
    it = 0
    rx, Jx = fun_rJ(x, *args)
    f = 0.5 * np.linalg.norm(rx)**2
    df = np.dot(Jx.T, rx)
    converged = (np.abs(df) <= tol)
    nfun = 1

    # Store data for plotting
    X = [x]
    F = [f]
    dF = [df]
    alpha_values = []

    # Main loop of Gauss-Newton
    while not converged and it < maxit:
        it += 1
        
        # Calculate the search direction by solving a linear LSQ problem
        p = linearLSQ(Jx, -rx)[0,...]
        
        if flag_line == 1:
            # Backtracking line search
            alpha = 1
            x_new = x + alpha * p
            rx_new, _ = fun_rJ(x_new, *args)
            f_new = 0.5 * np.linalg.norm(rx_new)**2

            while f_new > (f + c * alpha * np.dot(df, p)):
                alpha *= rho
                x_new = x + alpha * p
                rx_new, _ = fun_rJ(x_new, *args)
                f_new = 0.5 * np.linalg.norm(rx_new)**2    
            alpha_values.append(alpha)
        else:
            # Fixed alpha
            alpha = 1
        
        # Update the iterate, Jacobian, residual, f, df
        x += alpha * p
        rx, Jx = fun_rJ(x, *args)
        f = 0.5 * np.linalg.norm(rx)**2
        df = np.dot(Jx.T, rx)
        converged = (np.linalg.norm(df, np.inf) <= tol)
        nfun += 1

        # Store data for plotting
        X.append(x)
        F.append(f)
        dF.append(df)

    # Prepare return data
    stat = {
        "converged": converged,
        "iter": it,
        "X": np.array(X),
        "F": np.array(F),
        "dF": np.array(dF),
        "alpha": np.array(alpha_values),
        "nfun": nfun
    }
    
    return x, stat


