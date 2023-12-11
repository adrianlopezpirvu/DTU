clear, close all
data = [15 3 2; 5 12 3; 4 2 14]; %data that I read off the table in the exam problem


N_trials =20;

data = data/N_trials;

% false positives are based on stimulus 1 flash
ZFp3 = norminv(data(1,3)); %Probit transformed false positives for response category 2
ZFp2 = norminv(sum(data(1,2:3),2)); %Probit transformed false positives for response category 2+3

%true positives for stimulus 2 flashes 
ZTp32 = norminv(data(2,3)); %Probit transformed true positives for response category 3
ZTp22 = norminv(sum(data(2,2:3),2)); %Probit transformed true positives for response category 2+3

%true positives for stimulus 3 flashes 
ZTp33 = norminv(data(3,3)); %Probit transformed true positives for response category 3
ZTp23 = norminv(sum(data(3,2:3),2));%Probit transformed true positives for response category 2+3

slope12 = (ZTp32-ZTp22) / (ZFp3-ZFp2); %ROC slope for stimulus 1 vs 2
slope13 = (ZTp33-ZTp23) / (ZFp3-ZFp2); %ROC slope for stimulus 1 vs 3

intrcpt12 = ZTp32 - slope12*ZFp3; % ROC intercept for stimulus 1 vs 2
intrcpt13 = ZTp33 - slope13*ZFp3; % ROC intercept for stimulus 1 vs 3

sigma12 = 1/slope12 % sigma for stimulus 1 vs 2
sigma13 = 1/slope13 % sigma for stimulus 1 vs 3

mu12 = intrcpt12*sigma12 % mu for stimulus 1 vs 2
mu13 = intrcpt13*sigma13 % mu for stimulus 1 vs 3

%% plot

figure

x = -2:1e-2:0; %create an x-axis

subplot(1,2,1)
title('Probit coordinates')
hold on

%% plot probit transformed ROC for stimulus 1 vs 2
plot(x,slope12*x+intrcpt12,'k'); %plot the model line
plot(ZFp2,ZTp22,'ko'); %plot data point for response category 2+3
plot(ZFp3,ZTp32,'ko'); %plot data point for response category 3

%% plot probit transformed ROC for stimulus 1 vs 3
plot(x,slope13*x+intrcpt13,'b'); %plot the model line
plot(ZFp2,ZTp23,'bo'); %plot data point for response category 2+3
plot(ZFp3,ZTp33,'bo'); %plot data point for response category 3

axis square

subplot(1,2,2)
title('Probability coordinates')
hold on

%% plot ROC (not probit transformed) for stimulus 1 vs 2

plot(normcdf(x),normcdf(slope12*x+intrcpt12),'k'); %plot the model curve
plot(normcdf(ZFp2),normcdf(ZTp22),'ko'); %plot data point for response category 2+3
plot(normcdf(ZFp3),normcdf(ZTp32),'ko'); %plot data point for response category 3

%% plot ROC (not probit transformed) for stimulus 1 vs 3

plot(normcdf(x),normcdf(slope13*x+intrcpt13),'b'); %plot the model curve
plot(normcdf(ZFp2),normcdf(ZTp23),'bo'); %plot data point for response category 2+3
plot(normcdf(ZFp3),normcdf(ZTp33),'bo'); %plot data point for response category 3

axis square


