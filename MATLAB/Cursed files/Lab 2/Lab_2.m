im = imread('lab2img.png');
% imtool(im)

dims = size(im);

red = im(:, :, 1);
blue = im(:, :, 2);
green = im(:, :, 3);

intensity = rgb2gray(im);

minPixels = min(min(intensity));
maxPixels = max(max(intensity));
avgPixels = mean(mean(intensity));

% imtool(intensity)
intensityDims = size(intensity);
% imtool(red)
% imtool(blue)
% imtool(green)
% imhist(intensity);
title('Frequency of Pixel Strength')
xlabel('Pixel Strength')
ylabel('Frequency')

% imtool(intensity(:, 2016:4032))
% imtool(intensity(1:1512, :))


binImage = imbinarize(intensity);

imtool(binImage)

smallImage = imresize(im, 0.5);

imtool(smallImage)

smallDims = size(smallImage);

cursedImg = imresize(im, [200, 200]);

imtool(cursedImg)