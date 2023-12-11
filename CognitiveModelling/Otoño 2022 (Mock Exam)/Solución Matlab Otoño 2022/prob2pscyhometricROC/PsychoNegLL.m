function [NegLL,params]=PsychoNegLL(params,data)


P = normcdf(1:3,params(1),params(2)); % Calculate the response probabilities. params are [c_I sigma]

NegLL = -sum(log(binopdf(data,20,P))); %calculate the binomial negative log likelihood

