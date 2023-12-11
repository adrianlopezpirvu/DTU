function [NegLL,params]=negLL_FLMP(params,data)


pa = exp(params(1:2))./(exp(params(1:2))+1); %softmax to get the auditory response probabilities
pv = exp(params(3:4))./(exp(params(3:4))+1); %softmax to get the visual response probabilities


for a = 1:2 % loop through auditory stimuli

    for v=1:2 % loop through visual stimuli
        pav(v,a) = pa(a) * pv(v) / (pa(a) * pv(v) + (1-pa(a)) * (1-pv(v))); %use the probability matching model to calculate response probabilities
    end
end

%Stack the response probabilities in the same way as the data matrix
p_est = [pa; pv; pav];

%first row is auditory
%second row is visual

%rows 3-4 is audiovisual
%the row number indicates visual stimulus
%the column number indicatees the auditory stimulus


% we now have the response probabilities so we
%loop through the data file and calculate the binomial negative log likelihood
NegLL = 0;
for r = 1:4
    for c=1:2
        NegLL = NegLL - log(binopdf(data(r,c),20,p_est(r,c)));
    end
end



