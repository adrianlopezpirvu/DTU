clear

image_folder = 'faces';

imagererscaling = 0.2;

%%
% Question 1

% file extension of your files
file_pattern = '*.jpg';

smile_data = readtable("smile_intensity_and_imagenames.txt");
% get the list of the file from the smile scores list, so that the order
% matches
image_files = smile_data.filename;

smile_intensity = smile_data.smile_intensity;

a = rgb2gray(imread(fullfile(image_folder, char(image_files(1)))));
a = imresize(a,imagererscaling);

[image_files_numrows, image_files_numcols] = size(a);
num_pixels = numel(a);

image_data = zeros(length(image_files), num_pixels);

for i = 1 : length(image_files)
    x = double(imread(fullfile(image_folder, char(image_files(i))))) / 255;
    x = 0.2126 * x(:,:,1) + 0.7152 * x(:,:,2) + 0.0722 * x(:,:,3);
    x = imresize(x,imagererscaling);
    count = 0;
    for r = 1:image_files_numrows
        for c = 1:image_files_numcols
            count = count + 1;
            image_data(i,count) = x(r,c);
        end
    end
        image_data(i,:) = (image_data(i,:) - min(image_data(i,:))) / (max(image_data(i,:)) - min(image_data(i,:)));

  
end

count = 0;

i=41;
for r = 1:image_files_numrows
    for c = 1:image_files_numcols
        count = count + 1;
        test_image(r,c) = image_data(i,count);
    end
end

imagesc(test_image)
colormap gray

save('image_data.txt','image_data','-ascii')
save('smile_intensity.txt','smile_intensity','-ascii')