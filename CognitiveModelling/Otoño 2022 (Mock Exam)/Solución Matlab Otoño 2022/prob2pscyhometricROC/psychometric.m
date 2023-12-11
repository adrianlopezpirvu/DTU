clear, close all
data = [15 3 2; 5 12 3; 4 2 14]; %data that I read off the table in the exam problem

% my standard options for the optimisation function
options  = optimset('MaxFunEval',1e5,'MaxIter',1e5,'largescale','on','TolFun',1e-6,'TolX',1e-6,'Display','off');

N_trials =20;

% my initial guess for [c_I sigma]
params0 = [2,1];

% model fitting uses the likelihood function in the file PsychoNegLL.m
[params3,NegLL3] = fminunc('PsychoNegLL',params0,options,data(:,3)') % fit the model for response category 3
[params23,NegLL23] = fminunc('PsychoNegLL',params0,options,sum(data(:,2:3),2)') % fit the model for response category 2+3

figure

% values for the x-axis
x = 0.5:1e-2:3.5;

plot(1:3,data(:,3)/N_trials,'ok') % plot the data for response category 3
hold on % don't delete the plot when I plot more on top

plot(x,normcdf(x,params3(1),params3(2)),'k') % plot the model psychometric function for response category 3

plot(1:3,sum(data(:,2:3),2)/N_trials,'or') % plot the data for response category 2+3

plot(x,normcdf(x,params23(1),params23(2)),'r') % % plot the model psychometric function for response category 2+3

legend('3','3','2-3','2-3') % add a legend to the plot