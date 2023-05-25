% Jacob Gampa
% CMPSC 497 Lab #3

RGB = imread('case3.png');
% imshow(RGB);

gray = rgb2gray(RGB);
threshold = graythresh(gray);
% figure, imshow(gray)

bw = imbinarize(gray, threshold);
% figure, imshow(bw)

bw1 = bwareaopen(bw, 10);
% figure, imshow(bw1)

se = strel('disk', 20);
bw2 = imclose(bw1, se);
% figure, imshow(bw2);

bw3 = imfill(bw2, 'holes');
% figure, imshow(bw3)

[B, L] = bwboundaries(bw3, 'noholes');

imshow(label2rgb(L, @jet, [.5 .5 .5]))

hold on

for k = 1 : length(B)
    boundary = B{k};
    plot(boundary(:, 2), boundary(:, 1), 'black', 'LineWidth', 2)
end

stats = regionprops(L, 'Area', 'Centroid');

threshold = 0.85;

count = 0;

for k = 1 : length(B)

    boundary = B{k};

    delta_sq = diff(boundary).^2;
    perimeter = sum(sqrt(sum(delta_sq,2)));

    area1 = perimeter ^2/(4*pi);

    area2 = stats(k).Area;

    metric = area2/area1;

    metric_string = sprintf('%2.2f', metric);

    if metric > threshold
        count = count + 1;
        centroid = stats(k).Centroid;
        plot(centroid(1), centroid(2), 'ko');
    end

    text(boundary(1, 2)-35, boundary(1, 1) + 13, metric_string, 'Color', 'black', 'FontSize', 14, 'FontWeight', 'bold');
end

fprintf("Number of objects is %d\n", length(B))
fprintf("Number of round objects %d\n", count)
