clear

data = [1 20; 6 12; 6 18; 5 20]; % data read off the tables in the assignment
Nparams     = 4;
params0     = rand(1,Nparams) - .5; %initial parameters
options  = optimset('MaxFunEval',1e5,'MaxIter',1e5,'largescale','on','TolFun',1e-6,'TolX',1e-6,'Display','off'); %standard optimization options

[params, NegLL] = fminunc('negLL_FLMP',params0,options,data); %optimization routine returns the optimal params and the negative log likelihood

% extract the parameters from the parameter vector

pa = exp(params(1:2))./(exp(params(1:2))+1) %softmax to get the auditory response probabilities
pv = exp(params(3:4))./(exp(params(3:4))+1) %softmax to get the visual response probabilities

% you could also just list the parameters without softmaxing and explain that they need to be
% softmaxed to get response probabilities. Either way is fine.

NegLL


