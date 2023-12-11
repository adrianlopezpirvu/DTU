function [NegLL,params]=negLLMassaroMLE(params,data)

% get the response probabilities p_est from the model

% in data file and response probabilities p_est
%first row is auditory
%second row is visual

%rows 3-4 is audiovisual
%the row number indicates visual stimulus
%the column number indicatees the auditory stimulus

mu_a_tilde = (1:2)-params(1);
mu_v_tilde = (1:2)-params(2);

sigma_a = exp(params(3)); %exp ensures that sigma is positive
sigma_v = exp(params(4));

p_est(1,:)=normcdf(mu_a_tilde/sigma_a); %auditory response probabilities
p_est(2,:)=normcdf(mu_v_tilde/sigma_v); %visual response probabilities

w_a = sigma_v^2 / (sigma_a^2+sigma_v^2); %w_a according to MLE
sigma_av = sqrt((sigma_a^2*sigma_v^2)/(sigma_a^2+sigma_v^2)); %sigma_av according to MLE

for a = 1:2
    
    for v=1:2
        
        mu_av_tilde(v,a) = w_a * mu_a_tilde(a) + (1-w_a)*mu_v_tilde(v); %mu_av according to MLE
        p_est(v+2,a) = normcdf(mu_av_tilde(v,a)/sigma_av); %audio-visual response probabilities
        
    end
end

% we now have the response probabilities so we
%loop through the data file and calculate the binomial negative log likelihood 
NegLL = 0;
for r = 1:4
    for c=1:2
        NegLL = NegLL - log(binopdf(data(r,c),20,p_est(r,c)));        
    end
end




