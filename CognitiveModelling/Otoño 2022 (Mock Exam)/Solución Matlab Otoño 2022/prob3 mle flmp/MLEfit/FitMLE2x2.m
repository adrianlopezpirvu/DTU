clear 

data = [1 20; 6 12; 6 18; 5 20]; % data read off the tables in the assignment
Nparams     = 4;
params0     = rand(1,Nparams) - .5; %initial parameters
options  = optimset('MaxFunEval',1e5,'MaxIter',1e5,'largescale','on','TolFun',1e-6,'TolX',1e-6,'Display','off'); %standard optimization options

[params, NegLL] = fminunc('negLL_MLE',params0,options,data); %optimization routine returns the optimal params and the negative log likelihood

% extract the parameters from the parameter vector
c_a = params(1)
c_v = params(2)

sigma_a = exp(params(3)) % exp ensures that sigma is positive
sigma_v = exp(params(4)) % exp ensures that sigma is positive

NegLL
