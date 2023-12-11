%% load data
clear
close all;

load smile_intensity.txt
load images.txt
image_data = images;
mean_image_data = mean(image_data,1);
image_data_zeromean = image_data - mean_image_data;
image_files_numrows = 72;
image_files_numcols = 52;

%% Q4.1 Use PCA to find the number of PCs needed to keep 90% of the variance


[coeff,score,latent,tsquared,explained,mu] = pca(image_data_zeromean); %run pca

cumulated_variance = cumsum(explained); %calculate the cumulative variance

'Number of PCs needed'
Npc= min(find(cumulated_variance > 90)) %find the minimumum number of PCs to get over 90% variance


recon_image_indx = 23; % this is the image that we should reconstruct
image_data_recon =score(recon_image_indx,1:Npc)*coeff(:,1:Npc)' + mean_image_data; % reconstruct the image vector remembering to add the mean back

% this loop maps the image vector in image_data to a 2-D image
count = 0;
for r = 1:image_files_numrows
    for c = 1:image_files_numcols
        count = count + 1;
        image(r,c) = image_data(recon_image_indx,count); %original image
        image_recon(r,c) = image_data_recon(count); % reconstructtion
    end
end

% display the images
subplot(1,2,1)
imshow(image)
title('Original')
colormap gray
subplot(1,2,2)
imshow(image_recon)
title('econstruction')
colormap gray

%% Q4.2
pc_indx = [1 16]; % these are the two PCs we are interested in

'Image 1 and 16 account for the following proportion of the variance'
latent(pc_indx) / sum(latent) % calculate the proportion of the variance that each image accounts for


%% Q4.3 visualise min  - max face for pc1 / pc 16

pc_indx = [1 16]; % these are the two PCs we are interested in


for p=1:numel(pc_indx) %looping through the two PCs
    [M,recon_image_indx(1)] = min(score(:,pc_indx(p))); %finding the min score value for one image
    [M,recon_image_indx(2)] = max(score(:,pc_indx(p))); %finding the max score value for one image
    figure

    for i=1:2 %looping through the min and max score value
        subplot(1,2,i)

        image_data_recon =score(recon_image_indx(i),pc_indx(p))*coeff(:,pc_indx(p))' + mean_image_data; %reconstructing the image vector

        % this loop maps the image vector in image_data to a 2-D image
        count = 0;
        for r = 1:image_files_numrows
            for c = 1:image_files_numcols
                count = count + 1;
                image_recon(r,c) = image_data_recon(count);
            end
        end

        imshow(image_recon) %display the image
        colormap gray %in greyscale
        title(['PC ' num2str(pc_indx(p))])
    end

end


%% Q4.4 Calculate the covariance between the smile intensity and PC 1 and 16

for n = 1:55 %looping through 55 principal components

    cov_mtrix = cov(score(:,n),smile_intensity); %calculating the covariance matrix between the two vectors
    PcSmileCov(n) = cov_mtrix(1,2); %element (1,2) (and also element (2,1)) of the covariance matrix contains the covariance.
end

'Image 1 and 16 covariance with smile score'

PcSmileCov(pc_indx) %selecting the covariance of PC1 and PC16 with the smile intensity



%% Q4.6  10 pcs with numerically greatest covariance with the smile score
[~,I_covpc]=sort(abs(PcSmileCov),'descend'); %sort the absolute covariances

'Three PCs with the highest covariance with the smile intensity'
predictor_names(1,:) =I_covpc(1:3) %the 3 pc with greater absolute covariance. save the values for being predictors in a linear model


%% Q4.6-7 Fit linear model and synthesize images
predictor_names(2,:) =(1:3); % the competing model uses PC 1,2 and 3 as predictors

for s = 1:2 %loop through the two models
    figure
    model_data = score(:, predictor_names(s,:)); %the scores of the PCs that are predictors in the model
    linear_model = fitlm(model_data, smile_intensity); %fit a model
    model_coefficients = table2array(linear_model.Coefficients(:, 1)) % get the parameters of the linear model. 

    % generate faces
    synth_smile_intensities = -0.5 : 0.5 : 1.5; %The smile intensities i will use for the synthetic images

    for i = 1:length(synth_smile_intensities) %loop through the smile intensities of the synthetic faces
        target_smile_intensity = synth_smile_intensities(i);
        alpha = (target_smile_intensity - model_coefficients(1)) / sum(model_coefficients(2 : length(model_coefficients)).^2); %calculate alpha. the intercept is the first element of model_coefficients

        target_scores = alpha * model_coefficients(2 : length(model_coefficients));

        target_image_data(:, i) = coeff(:, predictor_names(s,:)) * target_scores + mean(image_data)'; %reconstruct the image vector and add the mean back
   
        subplot(1, length(synth_smile_intensities), i);

        % this loop maps the image vector in image_data to a 2-D image
        count = 0;
        for r = 1:image_files_numrows
            for c = 1:image_files_numcols
                count = count + 1;
                image_synth(r,c) = target_image_data(count, i);
            end
        end

        imshow(image_synth);
        title(sprintf("Score %.1f", synth_smile_intensities(i)));
    end

end



